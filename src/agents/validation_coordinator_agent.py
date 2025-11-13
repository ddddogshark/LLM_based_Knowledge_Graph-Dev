# src/agents/validation_coordinator_agent.py

from src.agents.base_agent import BaseAgent
from typing import Dict, Any

class ValidationCoordinatorAgent(BaseAgent):
    def __init__(self):
        super().__init__("ValidationCoordinatorAgent", "Coordinates validation, quality gates, and review meetings.")

    async def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        self._log("Validation coordinator is active. No direct execution for this agent in a stage, primarily used by gate functions.")
        # This agent's primary role is to facilitate gate functions, not necessarily to
        # perform a direct task that modifies the context in a stage's execution flow.
        return context

    async def review_document(self, document_name: str, document_content: str, criteria: str) -> bool:
        """
        Simulates a review process for a document based on given criteria.
        Uses LLM to evaluate the document.
        """
        self._log(f"Initiating review for '{document_name}' with criteria: {criteria}")
        prompt = f"""
        You are a Validation Coordinator Agent. Your task is to review a document based on specific criteria.
        
        Document Name: {document_name}
        Document Content:
        ---
        {document_content}
        ---
        
        Review Criteria: {criteria}
        
        Based on the criteria, evaluate the document. Respond with "APPROVED" if it meets the criteria,
        or "REJECTED" if it does not. Provide a brief reason for your decision.
        """
        
        review_result = self.llm_service.generate_text(prompt, temperature=0.3)
        self._log(f"Review result for '{document_name}': {review_result}")
        
        if "APPROVED" in review_result.upper():
            return True
        else:
            return False
