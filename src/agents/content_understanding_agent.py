from .base_agent import BaseAgent
from typing import Dict, Any, List
from src.utils.json_parser import extract_json_from_string # Import the utility

class ContentUnderstandingAgent(BaseAgent):
    def __init__(self, name: str, description: str, api_key: str = None, api_url: str = None):
        super().__init__(name, description, api_key, api_url)

    async def execute(self, initial_context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Receives all raw data, performs deep understanding, summarization, and extraction,
        and outputs structured knowledge point drafts.
        """
        multimodal_content = initial_context.get("multimodal_parsed_content", "")
        internet_content = initial_context.get("internet_scraped_content", "")
        academic_content = initial_context.get("academic_scraped_content", "")
        course_name = initial_context.get("course_name", "a generic course")

        self._log(f"Understanding content for '{course_name}'. Combining data from multiple sources.")

        combined_raw_data = f"Multimodal Content:\n{multimodal_content}\n\nInternet Content:\n{internet_content}\n\nAcademic Content:\n{academic_content}"

        prompt = f"""
        As a Knowledge Engineer, your task is to perform deep understanding, summarization, and extraction of key knowledge points from the following raw data.
        The goal is to create structured knowledge point drafts for the course "{course_name}".

        Raw Data:
        ---
        {combined_raw_data}
        ---

        Please extract key knowledge points. For each knowledge point, provide:
        -   A concise title/concept.
        -   A brief explanation.
        -   Relevant keywords.

        Format the output as a JSON array of objects, where each object represents a knowledge point.
        Example:
        [
            {{
                "title": "Supervised Learning",
                "explanation": "A type of machine learning where a model learns from labeled training data.",
                "keywords": ["machine learning", "labeled data", "classification", "regression"]
            }}
        ]
        """
        
        knowledge_point_drafts_json_str = await self.llm_service.generate_text(prompt)
        self._log("Knowledge point drafts generated.")
        
        knowledge_point_drafts = extract_json_from_string(knowledge_point_drafts_json_str)
        if isinstance(knowledge_point_drafts, list):
            initial_context["knowledge_point_drafts"] = knowledge_point_drafts
        else:
            self._log(f"Error decoding JSON for knowledge point drafts. Raw content: {knowledge_point_drafts_json_str}")
            initial_context["knowledge_point_drafts"] = []
        
        return initial_context