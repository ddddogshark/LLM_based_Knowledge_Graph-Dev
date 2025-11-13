# src/agents/demand_analysis_agent.py

from src.agents.base_agent import BaseAgent
from typing import Dict, Any

class DemandAnalysisAgent(BaseAgent):
    def __init__(self, name: str, description: str):
        super().__init__(name, description)

    async def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        self._log("Starting demand analysis...")
        course_name = context.get("course_name", "a specified course")

        # Simulate multi-round conversation with LLM to clarify demand
        prompt = f"""
        You are a Demand Analysis Agent. Your task is to interact with the user (simulated here by a single prompt)
        to clarify the requirements for building a knowledge graph for the course "{course_name}".

        Based on the initial request, generate a detailed "Demand Specification Document" that includes:
        1.  **Project Goal:** What is the primary objective of this knowledge graph?
        2.  **Scope:** What specific topics/areas within "{course_name}" should be covered?
        3.  **Target Audience:** Who will use this KG (students, teachers, researchers)?
        4.  **Key Deliverables:** What are the expected outputs (e.g., structured KG, reports, visualizations)?
        5.  **Success Metrics:** How will the success of the KG be measured?
        6.  **Initial Resources (if any):** Mention any initial resources provided (e.g., course syllabus, textbooks).

        Be thorough and ask clarifying questions if necessary (though for this simulation, provide a complete document).
        """
        
        demand_spec_doc = self.llm_service.generate_text(prompt, temperature=0.7)
        
        context["demand_spec_doc"] = demand_spec_doc
        self._log("Demand analysis completed. Demand Specification Document generated.")
        return context
