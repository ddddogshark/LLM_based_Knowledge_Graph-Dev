# src/agents/subject_overview_agent.py

from src.agents.base_agent import BaseAgent
from typing import Dict, Any

class SubjectOverviewAgent(BaseAgent):
    def __init__(self):
        super().__init__("SubjectOverviewAgent", "Creates an overall subject knowledge system planning based on demand.")

    async def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        self._log("Starting subject overview planning...")
        demand_spec_doc = context.get("demand_spec_doc", "No demand specification document found.")
        course_name = context.get("course_name", "a specified course")

        prompt = f"""
        You are a Subject Overview Agent. Your task is to act as a "Chief Architect" and create a comprehensive
        "Subject Knowledge System Overall Plan" based on the provided Demand Specification Document for the course "{course_name}".

        The plan should include:
        1.  **Core Course List:** Identify the main courses/modules within "{course_name}" (even if it's just one, detail its sub-modules).
        2.  **Logical Relationships between Courses/Modules:** Describe how these courses/modules connect.
        3.  **Unified Data Specification:** Propose a high-level data model or schema for the knowledge graph, including entity types, relationship types, and key attributes.
        4.  **Task Breakdown for Course-Specific Agents:** Outline initial tasks for hypothetical course-specific agents for each core course/module identified.

        Here is the Demand Specification Document:
        ---
        {demand_spec_doc}
        ---
        """
        
        subject_plan = self.llm_service.generate_text(prompt, temperature=0.7)
        
        context["subject_overview_plan"] = subject_plan
        self._log("Subject overview planning completed. Subject Knowledge System Overall Plan generated.")
        return context
