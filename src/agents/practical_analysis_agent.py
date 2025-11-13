# src/agents/practical_analysis_agent.py

from src.agents.base_agent import BaseAgent
from typing import Dict, Any, List

class PracticalAnalysisAgent(BaseAgent):
    def __init__(self):
        super().__init__("PracticalAnalysisAgent", "Finds practical examples and case studies for knowledge points.")

    async def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        self._log("Starting practical analysis of refined knowledge points...")
        
        refined_knowledge: List[Dict[str, str]] = context.get("refined_knowledge_points", [])
        
        if not refined_knowledge:
            self._log("No refined knowledge points found for practical analysis.")
            return context
            
        self._log(f"Analyzing {len(refined_knowledge)} refined knowledge points.")
        
        enriched_knowledge_points = []
        for item in refined_knowledge:
            refined_content = item.get("refined_content", "")
            
            self._log(f"Finding practical examples for knowledge point...")
            
            prompt = f"""
            You are a Practical Analysis Agent. Your task is to take a theoretically sound knowledge point
            and enrich it with practical applications, such as code examples or real-world case studies.

            Your analysis should:
            1.  **Identify Application Areas:** Where is this concept used in practice?
            2.  **Provide Code Examples:** If applicable, provide a simple code snippet (e.g., in Python) that demonstrates the concept.
            3.  **Describe a Case Study:** Briefly describe a real-world case study or project where this concept was applied.

            Refined Knowledge Point:
            ---
            {refined_content}
            ---
            
            Generate the enriched knowledge point with practical examples.
            """
            
            practical_enrichment = self.llm_service.generate_text(prompt, temperature=0.6)
            
            # Combine the refined content with the practical enrichment
            item["enriched_content"] = f"{refined_content}\n\n--- Practical Application ---\n{practical_enrichment}"
            item["status"] = "practically_analyzed"
            enriched_knowledge_points.append(item)
            
        # Replace the refined knowledge with the enriched knowledge
        context["enriched_knowledge_points"] = enriched_knowledge_points
        context.pop("refined_knowledge_points", None)
        
        self._log(f"Completed practical analysis of {len(enriched_knowledge_points)} knowledge points.")
        
        return context
