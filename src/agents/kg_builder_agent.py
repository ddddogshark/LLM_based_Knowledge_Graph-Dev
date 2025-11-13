# src/agents/kg_builder_agent.py

from src.agents.base_agent import BaseAgent
from typing import Dict, Any, List
import json

class KgBuilderAgent(BaseAgent):
    def __init__(self):
        super().__init__("KgBuilderAgent", "Builds knowledge sub-graphs by extracting triplets from enriched knowledge points.")

    async def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        self._log("Starting knowledge sub-graph construction...")
        
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
                # The LLM might return the JSON string within a code block or with extra text.
                # We'll try to find the JSON list within the response.
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

        # Add the triplets to the context
        if "knowledge_subgraph_triplets" not in context:
            context["knowledge_subgraph_triplets"] = []
        context["knowledge_subgraph_triplets"].extend(all_triplets)
        
        self._log(f"Completed sub-graph construction with a total of {len(all_triplets)} triplets.")
        
        # For now, we will also store them in Neo4j directly.
        # In a more complex scenario, this might happen in a later stage.
        if all_triplets:
            self._log("Storing triplets in Neo4j...")
            self.neo4j_driver.store_triplets(all_triplets)
            self._log("Finished storing triplets.")
            
        return context
