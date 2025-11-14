from .base_agent import BaseAgent
from typing import Dict, Any

class DemandAnalysisAgent(BaseAgent):
    def __init__(self, name: str, description: str, api_key: str = None, api_url: str = None):
        super().__init__(name, description, api_key, api_url)

    async def execute(self, initial_context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyzes user requirements and generates a demand specification document.
        """
        user_query = initial_context.get("user_query", "No specific query provided.")
        self._log(f"Analyzing demand for user query: {user_query}")

        prompt = f"""
        As a Demand Analysis Expert, your task is to clarify user requirements and output a clear, concise, and structured demand specification document.
        The user's initial query is: "{user_query}"

        Please generate a demand specification document that includes:
        1.  **Project Goal:** What is the main objective?
        2.  **Scope:** What functionalities or areas will be covered?
        3.  **Key Deliverables:** What are the expected outputs?
        4.  **Success Metrics:** How will success be measured?
        5.  **Constraints/Assumptions:** Any limitations or assumptions.

        Format the output as a Markdown document.
        """
        
        demand_spec_doc = await self.llm_service.generate_text(prompt)
        self._log("Demand specification document generated.")
        
        initial_context["demand_spec_doc"] = demand_spec_doc
        return initial_context