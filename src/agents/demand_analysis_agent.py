from .base_agent import BaseAgent
from typing import Dict, Any
from src.services.llm_service import generate_text_sync

class DemandAnalysisAgent(BaseAgent):
    def __init__(self, name: str, description: str, api_key: str = None, api_url: str = None):
        super().__init__(name, description, api_key, api_url)

    async def execute(self, initial_context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyzes the user's query to produce a structured demand specification document.
        """
        user_query = initial_context.get("user_query", "No specific query provided.")
        main_query_input = initial_context.get("course_name", "")
        if user_query != "No specific query provided.":
            main_query_input = f"{main_query_input} with additional user request: {user_query}"

        prompt = f"""
        As a Senior Analyst, analyze the following query and generate a structured demand specification document in markdown format.
        The document should clarify the needs, define the scope, and outline key requirements.
        If the query is generic, create a comprehensive template for a demand specification document.

        Query: "{main_query_input}"
        """
        
        demand_spec_doc = generate_text_sync(prompt, api_key=self.api_key, api_url=self.api_url)
        self._log("Demand specification document generated.")
        
        initial_context["demand_spec_doc"] = demand_spec_doc
        return initial_context