# src/agents/kg_builder_agent.py

from src.agents.base_agent import BaseAgent
from typing import Dict, Any, List
import json

class KgBuilderAgent(BaseAgent):
    def __init__(self):
        super().__init__("KgBuilderAgent", "Builds and integrates knowledge graphs.")

    async def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        This method is used in Stage 3 to create a course-level sub-graph.
        It extracts triplets from enriched knowledge points.
        """
        self._log("Starting knowledge sub-graph construction (triplet extraction)...")
        
        enriched_knowledge: List[Dict[str, str]] = context.get("enriched_knowledge_points", [])
        
        if not enriched_knowledge:
            self._log("No enriched knowledge points found to build the graph from.")
            return context
            
        self._log(f"Processing {len(enriched_knowledge)} enriched knowledge points.")
        
        all_triplets = []
        for item in enriched_knowledge:
            enriched_content = item.get("enriched_content", "")
            
            self._log(f"Extracting triplets from an enriched knowledge point...")
            
            prompt = f"""
            You are a Knowledge Graph Builder Agent. Your task is to extract knowledge triplets (Head, Relation, Tail)
            from the provided enriched knowledge point text.

            Rules for extraction:
            1.  **Entities (Head/Tail):** Should be specific concepts, terms, or entities.
            2.  **Relations:** Should describe the relationship between the head and tail (e.g., "is_a", "part_of", "has_property", "used_for", "prerequisite_for").
            3.  **Output Format:** Provide the output as a JSON list of lists, where each inner list is a triplet. Example: [["Machine Learning", "is_a", "Field of AI"], ["Transformer", "based_on", "Attention Mechanism"]]

            Enriched Knowledge Point:
            ---
            {enriched_content}
            ---
            
            Extract all relevant triplets and provide them in the specified JSON format.
            """
            
            triplets_json_str = self.llm_service.generate_text(prompt, temperature=0.3)
            
            try:
                start_index = triplets_json_str.find('[')
                end_index = triplets_json_str.rfind(']') + 1
                if start_index != -1 and end_index != -1:
                    triplets_json_str = triplets_json_str[start_index:end_index]
                    triplets = json.loads(triplets_json_str)
                    if isinstance(triplets, list):
                        all_triplets.extend(triplets)
                        self._log(f"Extracted {len(triplets)} triplets.")
                else:
                    self._log("Warning: Could not find a JSON list in the LLM response.")

            except json.JSONDecodeError as e:
                self._log(f"Error decoding JSON from LLM response: {e}")
                self._log(f"LLM Response was: {triplets_json_str}")

        # Add the triplets to the context for the current course
        course_name = context.get("course_name", "unknown_course")
        if "subgraphs" not in context:
            context["subgraphs"] = {}
        context["subgraphs"][course_name] = all_triplets
        
        self._log(f"Completed sub-graph construction for {course_name} with {len(all_triplets)} triplets.")
        
        return context

    async def integrate_and_store(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        This method is used in Stage 4 to integrate all sub-graphs and store them.
        """
        self._log("Starting knowledge graph integration and storage...")
        subgraphs = context.get("subgraphs", {})
        
        if not subgraphs:
            self._log("No sub-graphs found to integrate.")
            return context

        # In a real multi-course scenario, this is where you would perform
        # entity alignment, conflict resolution, etc., across the different sub-graphs.
        # For now, we will just merge all triplets from all sub-graphs.
        
        integrated_triplets = []
        for course_name, triplets in subgraphs.items():
            self._log(f"Integrating {len(triplets)} triplets from course: {course_name}")
            integrated_triplets.extend(triplets)
            
        self._log(f"Total of {len(integrated_triplets)} triplets integrated.")
        
        # Store the final, integrated triplets in Neo4j
        if integrated_triplets:
            self._log("Storing integrated triplets in Neo4j...")
            self.neo4j_driver.store_triplets(integrated_triplets)
            self._log("Finished storing triplets.")
            
        context["integrated_triplets"] = integrated_triplets
        
        return context
