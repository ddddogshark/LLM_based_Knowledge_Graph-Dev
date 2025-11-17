from .base_agent import BaseAgent
from typing import Dict, Any, List
from src.utils.json_parser import extract_json_from_string # Import the utility

BATCH_SIZE = 5 # Define a batch size for processing knowledge points

class KgBuilderAgent(BaseAgent):
    def __init__(self, name: str, description: str, api_key: str = None, api_url: str = None):
        super().__init__(name, description, api_key, api_url)

    async def execute(self, initial_context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Builds a sub-knowledge graph for a course by extracting triplets from knowledge points.
        Processes knowledge points in batches to reduce API calls.
        """
        practically_enhanced_knowledge_points = initial_context.get("practically_enhanced_knowledge_points", [])
        course_name = initial_context.get("course_name", "a generic course")

        self._log(f"Building sub-knowledge graph for '{course_name}' from {len(practically_enhanced_knowledge_points)} knowledge points.")

        if not practically_enhanced_knowledge_points:
            self._log("No practically enhanced knowledge points to build sub-knowledge graph from.")
            initial_context["subgraphs"] = {course_name: []}
            return initial_context

        all_triplets = []
        # Process knowledge points in batches
        for i in range(0, len(practically_enhanced_knowledge_points), BATCH_SIZE):
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
            self._log(f"Sending batch {i//BATCH_SIZE + 1} to LLM for triplet extraction.")
            triplets_json_str = await self.llm_service.generate_text(prompt, temperature=0.3)
            triplets = extract_json_from_string(triplets_json_str)
            if isinstance(triplets, list):
                all_triplets.extend(triplets)
            else:
                self._log(f"Warning: LLM returned non-list content for triplets in batch {i//BATCH_SIZE + 1}: {triplets_json_str}")
        
        self._log(f"Sub-knowledge graph built for '{course_name}' with {len(all_triplets)} triplets.")
        
        # Store subgraphs in context, keyed by course_name
        subgraphs = initial_context.get("subgraphs", {})
        subgraphs[course_name] = all_triplets
        initial_context["subgraphs"] = subgraphs
        return initial_context

    async def integrate_kps(self, initial_context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Integrates all reviewed course sub-graphs to build a complete subject knowledge graph.
        This method would also store the integrated graph in a database (e.g., Neo4j).
        """
        self._log("Integrating sub-knowledge graphs into a unified knowledge graph.")
        all_subgraphs = initial_context.get("subgraphs", {})
        
        unified_triplets = []
        for course, triplets in all_subgraphs.items():
            unified_triplets.extend(triplets)
        
        # In a real scenario, this would involve more sophisticated integration logic
        # (e.g., entity resolution, conflict resolution) and then storing in Neo4j.
        self._log(f"Unified knowledge graph contains {len(unified_triplets)} triplets.")
        
        # Store in Neo4j
        await self.neo4j_driver.store_triplets(unified_triplets)
        self._log("Unified knowledge graph stored in Neo4j.")

        initial_context["final_knowledge_graph"] = unified_triplets
        return initial_context
        return initial_context