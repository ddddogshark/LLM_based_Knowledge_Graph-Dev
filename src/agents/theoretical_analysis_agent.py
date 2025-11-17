from .base_agent import BaseAgent
from typing import Dict, Any, List
from src.utils.json_parser import extract_json_from_string # Import the utility

BATCH_SIZE = 5 # Define a batch size for processing knowledge points

class TheoreticalAnalysisAgent(BaseAgent):
    def __init__(self, name: str, description: str, api_key: str = None, api_url: str = None):
        super().__init__(name, description, api_key, api_url)

    async def execute(self, initial_context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Ensures theoretical rigor and coherence of knowledge points by processing them in batches.
        """
        knowledge_point_drafts = initial_context.get("knowledge_point_drafts", [])
        course_name = initial_context.get("course_name", "a generic course")

        self._log(f"Performing theoretical analysis for {len(knowledge_point_drafts)} knowledge points for '{course_name}'.")

        if not knowledge_point_drafts:
            self._log("No knowledge point drafts to analyze theoretically.")
            initial_context["theoretically_refined_knowledge_points"] = []
            return initial_context

        refined_knowledge_points = []
        for i in range(0, len(knowledge_point_drafts), BATCH_SIZE):
            batch = knowledge_point_drafts[i:i + BATCH_SIZE]
            
            batch_prompts = []
            for kp in batch:
                batch_prompts.append(f"""
                {{
                    "title": "{kp.get('title', 'N/A')}",
                    "explanation": "{kp.get('explanation', 'N/A')}",
                    "keywords": {kp.get('keywords', [])}
                }}
                """)

            combined_prompts = ",\n".join(batch_prompts)

            prompt = f"""
            As a Theoretical Analyst for the course "{course_name}", review the following knowledge points for theoretical rigor, coherence, and completeness.
            For each knowledge point, suggest any improvements, identify potential gaps, or rephrase for better clarity and academic accuracy.
            
            Return a JSON array containing the refined knowledge points in the same JSON format (title, explanation, keywords).
            The number of returned JSON objects must match the number of input knowledge points.

            Knowledge Points:
            [
            {combined_prompts}
            ]
            """
            self._log(f"Sending batch {i//BATCH_SIZE + 1} to LLM for theoretical analysis.")
            refined_kps_json_str = await self.llm_service.generate_text(prompt)
            refined_kps = extract_json_from_string(refined_kps_json_str)
            
            if isinstance(refined_kps, list) and len(refined_kps) == len(batch):
                refined_knowledge_points.extend(refined_kps)
            else:
                self._log(f"Error decoding JSON or mismatched count for refined knowledge points in batch {i//BATCH_SIZE + 1}. Raw content: {refined_kps_json_str}. Keeping original batch.")
                refined_knowledge_points.extend(batch) # Keep original batch if parsing fails

        self._log("Theoretical analysis completed.")
        initial_context["theoretically_refined_knowledge_points"] = refined_knowledge_points
        return initial_context