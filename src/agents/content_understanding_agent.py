import os
from .base_agent import BaseAgent
from typing import Dict, Any, List, Set
from src.utils.json_parser import extract_json_from_string
from src.services.llm_service import generate_text_sync, generate_text_async
import asyncio
from requests.exceptions import ReadTimeout
from src.utils.text_splitter import recursive_text_splitter
import json

class ContentUnderstandingAgent(BaseAgent):
    def __init__(self, name: str, description: str, api_key: str = None, api_url: str = None):
        super().__init__(name, description, api_key, api_url)
        self.concurrency_limit = 10

    async def execute(self, initial_context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Processes raw text data using the EDC (Extract-Define-Canonicalize) method
        to generate structured "knowledge point drafts".
        """
        course_name = initial_context.get("course_name", "a generic course")
        self._log(f"Understanding content for '{course_name}' using EDC method.")

        # --- 1. Combine and Split Text ---
        self._log("Combining and splitting data from multiple sources.")
        internet_content = initial_context.get("internet_scraped_content", "")
        academic_content = initial_context.get("academic_scraped_content", "")
        multimodal_content = initial_context.get("multimodal_parsed_content", [])

        full_text = "\n\n---\n\n".join(multimodal_content)
        if internet_content:
            full_text += "\n\n---\n\n" + internet_content
        if academic_content:
            full_text += "\n\n---\n\n" + academic_content

        if not full_text.strip():
            self._log("No content to understand.")
            initial_context["knowledge_point_drafts"] = []
            return initial_context

        text_chunks = recursive_text_splitter(full_text)
        self._log(f"Split content into {len(text_chunks)} chunks.")

        # --- Stage 1: Extract (OIE) ---
        self._log("Stage 1: Starting Open Information Extraction (OIE) to extract raw triplets.")
        raw_triplets = await self._extract_oie(text_chunks, course_name)
        if not raw_triplets:
            self._log("OIE finished but no triplets were extracted.")
            initial_context["knowledge_point_drafts"] = []
            return initial_context
        self._log(f"Extracted {len(raw_triplets)} raw triplets.")

        # --- Post-Extraction Filtering ---
        self._log("Applying post-extraction filters to remove noise and irrelevant data.")
        filtered_triplets = self._filter_raw_triplets(raw_triplets)
        self._log(f"Filtered down to {len(filtered_triplets)} triplets after cleaning.")


        # --- Stage 2: Define ---
        self._log("Stage 2: Defining unique relations.")
        unique_relations = list(set([t[1] for t in filtered_triplets]))
        self._log(f"Found {len(unique_relations)} unique relations to define.")
        relation_definitions = await self._define_relations(unique_relations, course_name)
        self._log(f"Generated definitions for {len(relation_definitions)} relations.")

        # --- Stage 3: Canonicalize ---
        self._log("Stage 3.1: Canonicalizing relations using generative LLM.")
        relation_canonical_map = await self._canonicalize_relations_with_llm(relation_definitions)
        self._log("Relation canonicalization complete.")

        # Apply relation canonicalization
        canonical_triplets = [[t[0], relation_canonical_map.get(t[1], t[1]), t[2]] for t in filtered_triplets]

        self._log("Stage 3.2: Canonicalizing entities using generative LLM.")
        entity_canonical_map = await self._canonicalize_entities_with_llm(canonical_triplets)
        self._log("Entity canonicalization complete.")

        # Apply entity canonicalization
        final_triplets = [
            [entity_canonical_map.get(t[0], t[0]), t[1], entity_canonical_map.get(t[2], t[2])]
            for t in canonical_triplets
        ]
        self._log(f"Applied entity canonicalization. Triplets count: {len(final_triplets)}.")

        # --- Final Deduplication ---
        self._log("Deduplicating final set of triplets.")
        unique_triplets_set = set(tuple(t) for t in final_triplets)
        deduplicated_triplets = [list(t) for t in unique_triplets_set]
        self._log(f"Deduplication complete. Final triplet count: {len(deduplicated_triplets)}.")


        # --- Final Conversion to Knowledge Points ---
        self._log("Converting canonical triplets to knowledge point drafts.")
        knowledge_points = await self._convert_triplets_to_knowledge_points(deduplicated_triplets, course_name)
        self._log(f"Generated {len(knowledge_points)} final knowledge point drafts.")
        
        self._save_drafts_to_json(knowledge_points, course_name)

        initial_context["knowledge_point_drafts"] = knowledge_points
        return initial_context

    def _filter_raw_triplets(self, triplets: List[List[str]]) -> List[List[str]]:
        """Filters out low-quality, noisy, or irrelevant triplets."""
        
        # Keywords to identify and filter out example-specific data
        EXAMPLE_KEYWORDS = [
            'civic', 'corolla', 'camry', 'toyota', 'nissan', 'honda', 
            'maxima', 'altima', 'prius', 'car', 'vehicle', 'dealer', 
            'price', '$', 'id#', 'vin'
        ]
        
        # Pronouns and other vague phrases to filter from the head of a triplet
        VAGUE_HEADS = [
            'it', 'its', 'they', 'this', 'that', 'these', 'those', 
            'he', 'she', 'we', 'a key component', 'this approach', 'the curriculum',
            'this course'
        ]

        filtered = []
        for triplet in triplets:
            if len(triplet) != 3:
                continue

            head, _, tail = triplet
            head_lower = head.lower()
            tail_lower = tail.lower()

            # Rule 1: Filter out triplets with vague heads
            if any(head_lower.startswith(vh) for vh in VAGUE_HEADS):
                continue
            
            # Rule 2: Filter out triplets containing example-specific keywords
            if any(keyword in head_lower or keyword in tail_lower for keyword in EXAMPLE_KEYWORDS):
                continue

            # Rule 3: Filter out triplets where head or tail are likely just noisy numbers/codes
            if head.isnumeric() or (head.startswith('$') and head[1:].isnumeric()):
                continue
            if tail.isnumeric() or (tail.startswith('$') and tail[1:].isnumeric()):
                continue
                
            # Rule 4: Filter out triplets with very short, uninformative heads or tails
            if len(head) < 3 or len(tail) < 3:
                continue

            filtered.append(triplet)
            
        return filtered

    async def _extract_oie(self, text_chunks: List[str], course_name: str) -> List[List[str]]:
        # Checkpoint file setup
        sanitized_course_name = "".join(c for c in course_name if c.isalnum() or c in (' ', '_')).rstrip().replace(' ', '_')
        checkpoint_filename = f"{sanitized_course_name}-Extracting triplets from.json"
        
        all_triplets = []
        start_chunk = 0

        # Try to load from checkpoint
        # Forced to start from 0 by disabling checkpoint loading
        if False and os.path.exists(checkpoint_filename):
            try:
                with open(checkpoint_filename, "r", encoding="utf-8") as f:
                    checkpoint_data = json.load(f)
                last_processed = checkpoint_data.get("last_processed_chunk", -1)
                if last_processed > -1:
                    start_chunk = last_processed + 1
                    all_triplets = checkpoint_data.get("extracted_triplets", [])
                    self._log(f"Checkpoint found. Resuming OIE from chunk {start_chunk + 1}/{len(text_chunks)}.")
            except (json.JSONDecodeError, FileNotFoundError) as e:
                self._log(f"Could not read checkpoint file {checkpoint_filename}, starting from scratch. Error: {e}")
                start_chunk = 0
                all_triplets = []
        
        if start_chunk >= len(text_chunks):
            self._log("All chunks have already been processed according to checkpoint.")
            return all_triplets

        # Process chunks sequentially
        for i in range(start_chunk, len(text_chunks)):
            chunk = text_chunks[i]
            prompt = f"""
            From the text provided below, which is part of a course on "{course_name}", perform Open Information Extraction (OIE).
            Your task is to extract core theoretical concepts, principles, and definitions as triplets in the format [subject, relation, object].

            **CRITICAL INSTRUCTIONS**:
            1.  **Focus on Core Concepts**: Only extract triplets that define or explain fundamental principles of the main topic.
            2.  **Ignore Illustrative Examples**: Do NOT extract information from specific, non-generalizable examples. For instance, if the text uses a dataset of cars or products to illustrate a point, do NOT extract triplets about specific car models, prices, colors, or IDs.
            3.  **Generalize Knowledge**: The extracted triplets should represent general knowledge about the subject, not facts about the examples used to teach it.
            
            The 'relation' should be a concise verb phrase. Return a valid JSON array of arrays.
            Example of what to extract: [["Parallel Algorithm Design", "involves", "task generation"], ["Decomposition", "is a key technique in", "Parallel Computing"]]
            Example of what NOT to extract: [["Civic Model 4523", "has color", "blue"], ["Product ID 7623", "costs", "$21,000"]]

            Content:
            {chunk}
            """
            self._log(f"Extracting triplets from chunk {i + 1}/{len(text_chunks)}")
            
            try:
                response_str = await generate_text_async(prompt, 0.5)
                new_triplets = extract_json_from_string(response_str)
                
                if isinstance(new_triplets, list) and all(isinstance(t, list) and len(t) == 3 for t in new_triplets):
                    all_triplets.extend(new_triplets)
                else:
                    self._log(f"Could not parse valid triplets from chunk {i + 1}. Raw output: {response_str}")

            except Exception as e:
                self._log(f"Error processing chunk {i + 1}: {e}")
            
            # Save checkpoint after each chunk
            try:
                checkpoint_data = {
                    "last_processed_chunk": i,
                    "extracted_triplets": all_triplets
                }
                with open(checkpoint_filename, "w", encoding="utf-8") as f:
                    json.dump(checkpoint_data, f, indent=4)
            except Exception as e:
                self._log(f"Error saving checkpoint file {checkpoint_filename}: {e}")

        return all_triplets

    async def _define_relations(self, relations: List[str], course_name: str) -> Dict[str, str]:
        semaphore = asyncio.Semaphore(self.concurrency_limit)
        relation_definitions = {}

        async def get_definition(relation):
            async with semaphore:
                prompt = f"""
                Provide a concise definition for the relation predicate "{relation}" in the context of "{course_name}".
                The definition should explain what it means for a subject to be related to an object by this predicate.
                Return only the definition as a single string.

                Example for "is a subfield of":
                "The subject entity is a specific area of study or practice within the broader field of the object entity."
                
                Relation to define: "{relation}"
                """
                try:
                    definition = await generate_text_async(prompt, 0.5)
                    relation_definitions[relation] = definition.strip().strip('"')
                except Exception as e:
                    self._log(f"Error defining relation '{relation}': {e}")
                    relation_definitions[relation] = "" # Provide empty definition on error

        tasks = [get_definition(relation) for relation in relations]
        await asyncio.gather(*tasks)
        return relation_definitions

    async def _canonicalize_relations_with_llm(self, relation_definitions: Dict[str, str]) -> Dict[str, str]:
        if not relation_definitions:
            return {}

        # Prepare the list of relations and their definitions for the prompt
        relations_text = "\n".join([f'- "{relation}": {definition}' for relation, definition in relation_definitions.items()])

        prompt = f"""
        Below is a list of relation predicates and their definitions. Your task is to group these relations into clusters based on their semantic meaning.
        For each cluster, choose the most representative and concise relation name as the canonical name.

        **CRITICAL INSTRUCTIONS**:
        1.  **Prefer Descriptive Verbs**: The canonical name should be an active, descriptive verb phrase.
        2.  **Avoid Generic Terms**: Avoid using generic verbs like "is", "are", "has", or "includes" as the canonical name if a more specific alternative exists within the cluster. For example, for a cluster containing "is a type of" and "is a kind of", prefer "is a type of". For a cluster containing "is composed of" and "has parts", prefer "is composed of".

        Respond with a single valid JSON object. The keys of the object should be the canonical relation names. 
        The value for each key should be an array of the original relation names that belong to that cluster (including the canonical name itself).

        Example:
        If you are given:
        - "is a kind of": The subject is a specific type of the object.
        - "is a type of": The subject belongs to the class represented by the object.
        - "is located in": The subject is geographically situated within the object.

        Your output should be:
        {{
            "is a type of": ["is a kind of", "is a type of"],
            "is located in": ["is located in"]
        }}

        Here is the list of relations to cluster:
        {relations_text}

        Return only the JSON object.
        """
        
        self._log(f"Asking LLM to cluster {len(relation_definitions)} relations.")
        try:
            response_str = await generate_text_async(prompt, 0.2)
            clusters = extract_json_from_string(response_str)
            
            if not isinstance(clusters, dict):
                self._log(f"LLM did not return a valid dictionary for clustering. Raw output: {response_str}")
                # Fallback: return a 1:1 mapping
                return {r: r for r in relation_definitions.keys()}

            # Convert the cluster dictionary into the canonical map
            canonical_map = {}
            for canonical, originals in clusters.items():
                if isinstance(originals, list):
                    for original in originals:
                        canonical_map[original] = canonical
                else:
                    self._log(f"Warning: Invalid cluster format for canonical='{canonical}'. Expected a list.")
            
            # Ensure all original relations are mapped
            for original_relation in relation_definitions.keys():
                if original_relation not in canonical_map:
                    canonical_map[original_relation] = original_relation # Self-map if not clustered

            self._log(f"LLM created {len(clusters)} clusters.")
            return canonical_map

        except Exception as e:
            self._log(f"Error during LLM-based canonicalization: {e}")
            # Fallback: return a 1:1 mapping
            return {r: r for r in relation_definitions.keys()}

    async def _canonicalize_entities_with_llm(self, triplets: List[List[str]]) -> Dict[str, str]:
        """
        Uses an LLM to find a canonical representation for semantically similar entities.
        """
        if not triplets:
            return {}

        # Extract unique entities from head and tail of triplets
        unique_entities = list(set([t[0] for t in triplets] + [t[2] for t in triplets]))
        
        entities_text = "\n".join([f'- "{entity}"' for entity in unique_entities])

        prompt = f"""
        Below is a list of entities extracted from a text on a technical subject. Your task is to group these entities into clusters based on their semantic meaning.
        For each cluster, choose the most representative and comprehensive name as the canonical name for that cluster.

        Respond with a single valid JSON object. The keys of the object should be the canonical entity names. 
        The value for each key should be an array of the original entity names that belong to that cluster (including the canonical name itself).

        Example:
        If you are given:
        - "Decomposition"
        - "Problem decomposition"
        - "Task decomposition"
        - "Parallel Algorithm"
        - "Parallel Algorithms"

        Your output should be:
        {{
            "Task Decomposition": ["Decomposition", "Problem decomposition", "Task decomposition"],
            "Parallel Algorithm": ["Parallel Algorithm", "Parallel Algorithms"]
        }}

        Here is the list of entities to cluster:
        {entities_text}

        Return only the JSON object.
        """
        
        self._log(f"Asking LLM to cluster {len(unique_entities)} entities.")
        try:
            response_str = await generate_text_async(prompt, 0.2)
            clusters = extract_json_from_string(response_str)
            
            if not isinstance(clusters, dict):
                self._log(f"LLM did not return a valid dictionary for entity clustering. Raw output: {response_str}")
                # Fallback: return a 1:1 mapping
                return {e: e for e in unique_entities}

            # Convert the cluster dictionary into the canonical map
            canonical_map = {}
            for canonical, originals in clusters.items():
                if isinstance(originals, list):
                    for original in originals:
                        canonical_map[original] = canonical
                else:
                    self._log(f"Warning: Invalid cluster format for canonical entity='{canonical}'. Expected a list.")
            
            # Ensure all original entities are mapped
            for original_entity in unique_entities:
                if original_entity not in canonical_map:
                    canonical_map[original_entity] = original_entity # Self-map if not clustered

            self._log(f"LLM created {len(clusters)} entity clusters.")
            return canonical_map

        except Exception as e:
            self._log(f"Error during LLM-based entity canonicalization: {e}")
            # Fallback: return a 1:1 mapping
            return {e: e for e in unique_entities}

    async def _convert_triplets_to_knowledge_points(self, triplets: List[List[str]], course_name: str) -> List[Dict[str, Any]]:
        semaphore = asyncio.Semaphore(self.concurrency_limit)

        async def process_triplet_group(group_num, total_groups, triplet_group):
            async with semaphore:
                self._log(f"Processing knowledge point {group_num}/{total_groups} (Subject: '{triplet_group[0][0]}')...")
                prompt = f"""
                Convert the following list of knowledge triplets about "{course_name}" into a structured knowledge point.
                The knowledge point should be a JSON object with 'title', 'explanation', and 'keywords'.
                - 'title' should be the main subject entity.
                - 'explanation' should be a well-written paragraph summarizing the information in the triplets.
                - 'keywords' should be a list of important entities and concepts from the triplets.

                Triplets:
                {json.dumps(triplet_group, indent=2)}
                
                Return a single JSON object.
                """
                try:
                    response_str = await generate_text_async(prompt, 0.5)
                    kp = extract_json_from_string(response_str)
                    if isinstance(kp, dict) and 'title' in kp and 'explanation' in kp:
                        return kp
                    else:
                        self._log(f"Failed to convert triplet group {group_num}/{total_groups}. Raw output: {response_str}")
                        return None
                except Exception as e:
                    self._log(f"Error converting triplet group {group_num}/{total_groups}: {e}")
                    return None
        
        # Group triplets by subject to form coherent knowledge points
        triplets_by_subject = {}
        for subj, rel, obj in triplets:
            if subj not in triplets_by_subject:
                triplets_by_subject[subj] = []
            triplets_by_subject[subj].append([subj, rel, obj])

        total_groups = len(triplets_by_subject)
        self._log(f"Grouped triplets into {total_groups} knowledge points. Starting conversion...")

        tasks = [process_triplet_group(i + 1, total_groups, group) for i, group in enumerate(triplets_by_subject.values())]
        results = await asyncio.gather(*tasks)

        return [kp for kp in results if kp is not None]

    def _save_drafts_to_json(self, knowledge_points: List[Dict[str, Any]], course_name: str):
        if not knowledge_points:
            return
            
        sanitized_course_name = "".join(c for c in course_name if c.isalnum() or c in (' ', '_')).rstrip().replace(' ', '_')
        filename = f"knowledge_point_drafts_{sanitized_course_name}.json"
        try:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(knowledge_points, f, indent=4, ensure_ascii=False)
            self._log(f"Knowledge point drafts saved to '{filename}'.")
        except Exception as e:
            self._log(f"Error writing knowledge point drafts file: {e}")
