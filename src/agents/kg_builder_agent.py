from .base_agent import BaseAgent
from typing import Dict, Any, List
from src.utils.json_parser import extract_json_from_string
from src.services.llm_service import generate_text_sync
import asyncio
import json
import os

BATCH_SIZE = 2

class KgBuilderAgent(BaseAgent):
    def __init__(self, name: str, description: str, api_key: str = None, api_url: str = None):
        super().__init__(name, description, api_key, api_url)

import os

class KgBuilderAgent(BaseAgent):
    def __init__(self, name: str, description: str, api_key: str = None, api_url: str = None):
        super().__init__(name, description, api_key, api_url)

    async def execute(self, initial_context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Builds a sub-knowledge graph for a course by extracting triplets from knowledge points.
        Processes knowledge points in batches and uses checkpointing to handle long-running tasks.
        """
        practically_enhanced_knowledge_points = initial_context.get("practically_enhanced_knowledge_points", [])
        course_name = initial_context.get("course_name", "a generic course")

        self._log(f"Building sub-knowledge graph for '{course_name}' from {len(practically_enhanced_knowledge_points)} knowledge points.")

        if not practically_enhanced_knowledge_points:
            self._log("No practically enhanced knowledge points to build sub-knowledge graph from.")
            initial_context["subgraphs"] = {course_name: []}
            return initial_context

        # --- Checkpoint Setup ---
        sanitized_course_name = "".join(c for c in course_name if c.isalnum() or c in (' ', '_')).rstrip().replace(' ', '_')
        checkpoint_filename = f"KgBuilder_checkpoint_{sanitized_course_name}.json"
        
        all_triplets = []
        start_batch_index = 0

        if os.path.exists(checkpoint_filename):
            try:
                with open(checkpoint_filename, "r", encoding="utf-8") as f:
                    checkpoint_data = json.load(f)
                all_triplets = checkpoint_data.get("all_triplets", [])
                last_processed_index = checkpoint_data.get("last_processed_batch_index", -1)
                if last_processed_index > -1:
                    start_batch_index = last_processed_index + BATCH_SIZE
                self._log(f"Checkpoint found. Resuming from batch index {start_batch_index}. Already have {len(all_triplets)} triplets.")
            except (json.JSONDecodeError, FileNotFoundError):
                self._log(f"Could not read checkpoint {checkpoint_filename}, starting from scratch.")
                all_triplets = []
                start_batch_index = 0
        
        total_batches = (len(practically_enhanced_knowledge_points) + BATCH_SIZE - 1) // BATCH_SIZE
        # Loop from the starting batch index
        for i in range(start_batch_index, len(practically_enhanced_knowledge_points), BATCH_SIZE):
            batch = practically_enhanced_knowledge_points[i:i + BATCH_SIZE]
            batch_text_to_structure = []
            for kp in batch:
                batch_text_to_structure.append(f"Title: {kp.get('title', '')}\nExplanation: {kp.get('explanation', '')}\nPractical Example: {kp.get('practical_example', '')}")
            
            combined_text = "\n\n---\n\n".join(batch_text_to_structure)

            prompt = f"""
            Extract all possible knowledge triplets (subject, predicate, object) from the following texts.
            Each text block is separated by '---'.
            Represent each triplet as a dictionary with keys 'head', 'relation', and 'tail'.
            Return a JSON array of these dictionaries, containing triplets from all provided texts.

            Example:
            Text: "Barack Obama was born in Hawaii. --- Joe Biden is the current president."
            Output: [
                {{"head": "Barack Obama", "relation": "born in", "tail": "Hawaii"}},
                {{"head": "Joe Biden", "relation": "is", "tail": "current president"}}
            ]

            Texts:
            {combined_text}
            """
            current_batch_num = (i // BATCH_SIZE) + 1
            self._log(f"Sending batch {current_batch_num}/{total_batches} to LLM for triplet extraction.")
            
            triplets_json_str = generate_text_sync(prompt, temperature=0.3)
            triplets = extract_json_from_string(triplets_json_str)

            if isinstance(triplets, list):
                newly_found_triplets = 0
                for triplet in triplets:
                    if isinstance(triplet, dict) and triplet.get("head") and triplet.get("relation") and triplet.get("tail"):
                        all_triplets.append(triplet)
                        newly_found_triplets += 1
                    else:
                        self._log(f"Warning: Discarding invalid triplet in batch {current_batch_num}/{total_batches}: {triplet}")
                
                # --- Save Checkpoint ---
                if newly_found_triplets > 0:
                    try:
                        checkpoint_data = {
                            "last_processed_batch_index": i,
                            "all_triplets": all_triplets
                        }
                        with open(checkpoint_filename, "w", encoding="utf-8") as f:
                            json.dump(checkpoint_data, f, indent=4)
                        self._log(f"Checkpoint saved after batch {current_batch_num}. Total triplets: {len(all_triplets)}")
                    except Exception as e:
                        self._log(f"Error saving checkpoint file: {e}")

            else:
                self._log(f"Warning: LLM returned non-list content for triplets in batch {current_batch_num}/{total_batches}: {triplets_json_str}")
            
            await asyncio.sleep(1)
        
        # --- Finalization ---
        self._log(f"Sub-knowledge graph built for '{course_name}' with {len(all_triplets)} triplets.")
        
        # Save the final triplets to a local JSON file
        self._save_triplets_to_json(all_triplets, course_name)

        # Clean up checkpoint file after successful completion
        if os.path.exists(checkpoint_filename):
            try:
                os.remove(checkpoint_filename)
                self._log(f"Successfully removed checkpoint file '{checkpoint_filename}'.")
            except Exception as e:
                self._log(f"Error removing checkpoint file: {e}")

        subgraphs = initial_context.get("subgraphs", {})
        subgraphs[course_name] = all_triplets
        initial_context["subgraphs"] = subgraphs
        return initial_context

    def _save_triplets_to_json(self, triplets: List[Dict[str, str]], course_name: str):
        """Saves the extracted triplets to a JSON file."""
        if not triplets:
            return
        
        sanitized_course_name = "".join(c for c in course_name if c.isalnum() or c in (' ', '_')).rstrip().replace(' ', '_')
        filename = f"KgBuilder_{sanitized_course_name}.json"
        
        try:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(triplets, f, indent=4, ensure_ascii=False)
            self._log(f"Successfully saved {len(triplets)} triplets to '{filename}'.")
        except Exception as e:
            self._log(f"Error writing triplets to JSON file '{filename}': {e}")

    async def integrate_kps(self, initial_context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Integrates all reviewed course sub-graphs to build a complete subject knowledge graph.
        This method would also store the integrated graph in a database (e.g., Neo4j).
        """
        try:
            self._log("Integrating sub-knowledge graphs into a unified knowledge graph.")
            all_subgraphs = initial_context.get("subgraphs", {})
            
            unified_triplets = []
            for course, triplets in all_subgraphs.items():
                unified_triplets.extend(triplets)
            
            self._log(f"Unified knowledge graph contains {len(unified_triplets)} triplets.")
            
            if self.neo4j_driver:
                self.neo4j_driver.store_triplets(unified_triplets)
                self._log("Unified knowledge graph stored in Neo4j.")
            else:
                self._log("Neo4j driver not available. Skipping storage.")

            initial_context["final_knowledge_graph"] = unified_triplets
        except Exception as e:
            self._log(f"Error during knowledge graph integration: {e}")
        
        return initial_context