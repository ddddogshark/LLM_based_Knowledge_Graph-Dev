from .base_agent import BaseAgent
from typing import Dict, Any, List
from src.utils.json_parser import extract_json_from_string
from src.services.llm_service import generate_text_sync
import asyncio
from requests.exceptions import ReadTimeout

BATCH_SIZE = 20

class ContentUnderstandingAgent(BaseAgent):
    def __init__(self, name: str, description: str, api_key: str = None, api_url: str = None):
        super().__init__(name, description, api_key, api_url)

    async def execute(self, initial_context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Processes raw text data from various sources and generates structured knowledge point drafts sequentially.
        """
        course_name = initial_context.get("course_name", "a generic course")
        self._log(f"Understanding content for '{course_name}'. Combining data from multiple sources.")

        all_content = initial_context.get("multimodal_parsed_content", [])

        if not all_content:
            self._log("No content to understand.")
            initial_context["knowledge_point_drafts"] = []
            return initial_context

        all_knowledge_points = []
        for i in range(0, len(all_content), BATCH_SIZE):
            batch = all_content[i:i + BATCH_SIZE]
            combined_text = "\n\n".join(batch)

            prompt = f"""
            Based on the following content for a course on "{course_name}", identify and generate a list of key knowledge points.
            Each knowledge point should be a dictionary with 'title', 'explanation', and 'keywords' (a list of strings).
            Return a JSON array of these dictionaries.

            Content:
            {combined_text}
            """
            
            self._log(f"Processing batch {i//BATCH_SIZE + 1} of {len(all_content)//BATCH_SIZE + 1}")
            try:
                kp_drafts_json_str = generate_text_sync(prompt, temperature=0.5)
                kp_drafts = extract_json_from_string(kp_drafts_json_str)

                if isinstance(kp_drafts, list) and all(isinstance(item, dict) for item in kp_drafts):
                    all_knowledge_points.extend(kp_drafts)
                else:
                    self._log(f"Failed to generate valid knowledge point drafts for batch {i//BATCH_SIZE + 1}. Raw LLM output: {kp_drafts_json_str}")
            except ReadTimeout:
                self._log(f"ReadTimeout error on batch {i//BATCH_SIZE + 1}. Skipping this batch.")
            
            await asyncio.sleep(1)

        self._log(f"Knowledge point drafts generated: {len(all_knowledge_points)} total.")
        initial_context["knowledge_point_drafts"] = all_knowledge_points

        return initial_context