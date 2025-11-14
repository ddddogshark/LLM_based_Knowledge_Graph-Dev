from .base_agent import BaseAgent
from typing import Dict, Any, List
from src.utils.json_parser import extract_json_from_string # Import the utility

class PracticalAnalysisAgent(BaseAgent):
    def __init__(self, name: str, description: str, api_key: str = None, api_url: str = None):
        super().__init__(name, description, api_key, api_url)

    async def execute(self, initial_context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Matches knowledge points with code examples or project practices.
        """
        theoretically_refined_knowledge_points = initial_context.get("theoretically_refined_knowledge_points", [])
        course_name = initial_context.get("course_name", "a generic course")

        self._log(f"Performing practical analysis for {len(theoretically_refined_knowledge_points)} knowledge points for '{course_name}'.")

        if not theoretically_refined_knowledge_points:
            self._log("No theoretically refined knowledge points to analyze practically.")
            initial_context["practically_enhanced_knowledge_points"] = []
            return initial_context

        enhanced_knowledge_points = []
        for kp in theoretically_refined_knowledge_points:
            prompt = f"""
            As a Practical Application Expert for the course "{course_name}", provide a relevant code example or a small project idea for the following knowledge point.
            Focus on demonstrating the practical application of the concept.

            Knowledge Point:
            Title: {kp.get('title', 'N/A')}
            Explanation: {kp.get('explanation', 'N/A')}
            Keywords: {', '.join(kp.get('keywords', []))}

            Provide the enhanced knowledge point in the same JSON format (title, explanation, keywords) and add a new key "practical_example" with the code or project idea.
            If no practical example is suitable, set "practical_example" to "N/A".
            """
            enhanced_kp_json_str = await self.llm_service.generate_text(prompt)
            enhanced_kp = extract_json_from_string(enhanced_kp_json_str)
            if enhanced_kp:
                enhanced_knowledge_points.append(enhanced_kp)
            else:
                self._log(f"Error decoding JSON for enhanced knowledge point. Raw content: {enhanced_kp_json_str}. Keeping original.")
                enhanced_knowledge_points.append(kp) # Keep original if parsing fails

        self._log("Practical analysis completed.")
        initial_context["practically_enhanced_knowledge_points"] = enhanced_knowledge_points
        return initial_context