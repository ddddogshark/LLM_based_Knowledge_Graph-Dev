from .base_agent import BaseAgent
from typing import Dict, Any, List
from src.utils.json_parser import extract_json_from_string # Import the utility

class CourseAgent(BaseAgent):
    def __init__(self, name: str, description: str, api_key: str = None, api_url: str = None):
        super().__init__(name, description, api_key, api_url)

    async def execute(self, initial_context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Provides core resource lists (specified textbooks, keywords, etc.) for its course.
        """
        course_name = initial_context.get("course_name", "a generic course")
        self._log(f"Providing core resources for course: {course_name}")

        prompt = f"""
        As an expert in curriculum design, provide a list of core resources for the course "{course_name}".
        This should include:
        -   Key textbooks (title, author, year if possible)
        -   Important keywords for web scraping
        -   Relevant academic fields or sub-topics for academic paper scraping

        Format the output as a JSON object with keys "textbooks", "keywords", and "academic_fields", where values are lists of strings.
        Example:
        {{
            "textbooks": ["Deep Learning by Goodfellow et al."],
            "keywords": ["neural networks", "deep learning", "machine learning"],
            "academic_fields": ["Computer Science", "Artificial Intelligence"]
        }}
        """
        
        resources_json_str = await self.llm_service.generate_text(prompt)
        self._log("Core resources generated.")
        
        resources = extract_json_from_string(resources_json_str)
        if resources:
            initial_context["course_resources"] = resources
        else:
            self._log(f"Error decoding JSON for course resources. Raw content: {resources_json_str}")
            initial_context["course_resources"] = {"textbooks": [], "keywords": [course_name], "academic_fields": []}
        
        return initial_context

    async def review_knowledge_points(self, knowledge_points: List[Dict[str, Any]]) -> bool:
        """
        Reviews the quality and relevance of knowledge points for the course.
        """
        self._log(f"Reviewing {len(knowledge_points)} knowledge points.")
        # In a real scenario, this would involve LLM-based review or specific checks.
        # For now, simulate a positive review if there are knowledge points.
        return len(knowledge_points) > 0