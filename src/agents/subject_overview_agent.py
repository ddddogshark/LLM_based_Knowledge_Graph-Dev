from .base_agent import BaseAgent
from typing import Dict, Any
from src.services.llm_service import generate_text_sync

class SubjectOverviewAgent(BaseAgent):
    def __init__(self, name: str, description: str, api_key: str = None, api_url: str = None):
        super().__init__(name, description, api_key, api_url)

    async def execute(self, initial_context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Creates an overall subject plan based on the demand specification.
        """
        demand_spec_doc = initial_context.get("demand_spec_doc", "")
        course_name = initial_context.get("course_name", "a generic course")
        self._log(f"Formulating subject overview plan for '{course_name}' based on demand specification.")

        prompt = f"""
        As a Chief Architect, create a comprehensive and structured plan for building a subject knowledge system for "{course_name}".
        The plan should be based on the following demand specification document.
        The plan should be in markdown format and include a list of core courses/topics.

        Demand Specification:
        {demand_spec_doc}
        """
        
        subject_overview_plan = generate_text_sync(prompt)
        self._log("Subject overview plan generated.")
        
        initial_context["subject_overview_plan"] = subject_overview_plan
        return initial_context