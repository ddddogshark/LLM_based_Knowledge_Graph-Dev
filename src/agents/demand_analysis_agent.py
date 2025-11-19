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
        self._log(f"Analyzing demand for user query: {user_query}")

        prompt = f"""
        As a Senior Analyst, analyze the following user query and generate a structured demand specification document in markdown format.
        The document should clarify the user's needs, define the scope, and outline key requirements.
        If the query is generic, create a comprehensive template for a demand specification document.

        User Query: "{user_query}"
        """
        
        demand_spec_doc = generate_text_sync(prompt)
        self._log("Demand specification document generated.")
        
        initial_context["demand_spec_doc"] = demand_spec_doc
        return initial_context