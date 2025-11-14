from .base_agent import BaseAgent
from typing import Dict, Any

class SubjectOverviewAgent(BaseAgent):
    def __init__(self, name: str, description: str, api_key: str = None, api_url: str = None):
        super().__init__(name, description, api_key, api_url)

    async def execute(self, initial_context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Formulates an overall plan for subject knowledge system construction.
        """
        demand_spec_doc = initial_context.get("demand_spec_doc", "No demand specification document provided.")
        course_name = initial_context.get("course_name", "a generic subject")
        self._log(f"Formulating subject overview plan for '{course_name}' based on demand specification.")

        prompt = f"""
        As a Chief Architect for a knowledge system, your task is to formulate an overall plan for subject knowledge system construction.
        The demand specification document is as follows:
        ---
        {demand_spec_doc}
        ---

        Based on this, please generate a comprehensive plan that includes:
        1.  **Core Course List:** A list of essential courses or major topics.
        2.  **Logical Relationships:** How these courses/topics relate to each other (e.g., prerequisites, dependencies).
        3.  **Unified Data Specifications:** High-level guidelines for data consistency and format across the knowledge graph.
        4.  **Task Breakdown:** How the overall task of building the knowledge graph for "{course_name}" will be broken down into manageable parts.

        Format the output as a Markdown document.
        """
        
        subject_overview_plan = await self.llm_service.generate_text(prompt)
        self._log("Subject overview plan generated.")
        
        initial_context["subject_overview_plan"] = subject_overview_plan
        return initial_context