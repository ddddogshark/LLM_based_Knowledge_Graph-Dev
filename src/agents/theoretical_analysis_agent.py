from .base_agent import BaseAgent
from typing import Dict, Any, List
from src.utils.json_parser import extract_json_from_string # Import the utility

class TheoreticalAnalysisAgent(BaseAgent):
    def __init__(self, name: str, description: str, api_key: str = None, api_url: str = None):
        super().__init__(name, description, api_key, api_url)

    async def execute(self, initial_context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Ensures theoretical rigor and coherence of knowledge points.
        """
        knowledge_point_drafts = initial_context.get("knowledge_point_drafts", [])
        course_name = initial_context.get("course_name", "a generic course")

        self._log(f"Performing theoretical analysis for {len(knowledge_point_drafts)} knowledge points for '{course_name}'.")

        if not knowledge_point_drafts:
            self._log("No knowledge point drafts to analyze theoretically.")
            initial_context["theoretically_refined_knowledge_points"] = []
            return initial_context

        refined_knowledge_points = []
        for kp in knowledge_point_drafts:
            prompt = f"""
            As a Theoretical Analyst for the course "{course_name}", review the following knowledge point for theoretical rigor, coherence, and completeness.
            Suggest any improvements, identify potential gaps, or rephrase for better clarity and academic accuracy.
            
            Knowledge Point:
            Title: {kp.get('title', 'N/A')}
            Explanation: {kp.get('explanation', 'N/A')}
            Keywords: {', '.join(kp.get('keywords', []))}

            Provide the refined knowledge point in the same JSON format (title, explanation, keywords).
            """
            refined_kp_json_str = await self.llm_service.generate_text(prompt)
            refined_kp = extract_json_from_string(refined_kp_json_str)
            if refined_kp:
                refined_knowledge_points.append(refined_kp)
            else:
                self._log(f"Error decoding JSON for refined knowledge point. Raw content: {refined_kp_json_str}. Keeping original.")
                refined_knowledge_points.append(kp) # Keep original if parsing fails

        self._log("Theoretical analysis completed.")
        initial_context["theoretically_refined_knowledge_points"] = refined_knowledge_points
        return initial_context