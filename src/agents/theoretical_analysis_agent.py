# src/agents/theoretical_analysis_agent.py

from src.agents.base_agent import BaseAgent
from typing import Dict, Any, List

class TheoreticalAnalysisAgent(BaseAgent):
    def __init__(self):
        super().__init__("TheoreticalAnalysisAgent", "Ensures the theoretical rigor and coherence of knowledge points.")

    async def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        self._log("Starting theoretical analysis of knowledge point drafts...")
        
        drafts: List[Dict[str, str]] = context.get("knowledge_point_drafts", [])
        
        if not drafts:
            self._log("No knowledge point drafts found for theoretical analysis.")
            return context
            
        self._log(f"Analyzing {len(drafts)} knowledge point drafts.")
        
        refined_knowledge_points = []
        for item in drafts:
            source = item.get("source", "Unknown source")
            draft_content = item.get("draft", "")
            
            self._log(f"Analyzing draft from: {source}")
            
            prompt = f"""
            You are a Theoretical Analysis Agent. Your task is to analyze the following Knowledge Point Draft
            and refine it to ensure theoretical rigor and coherence.

            Your analysis should:
            1.  **Verify Correctness:** Check the factual accuracy of the statements.
            2.  **Ensure Coherence:** Make sure the concepts are presented in a logical and coherent manner.
            3.  **Add Theoretical Context:** Place the knowledge point within a broader theoretical framework. For example, mention the school of thought it belongs to, or the fundamental principles it's based on.
            4.  **Identify Relationships:** Explicitly state its relationship to other potential concepts (e.g., "this is a specific application of [broader concept]", "this is a prerequisite for [advanced concept]").

            Knowledge Point Draft:
            ---
            {draft_content}
            ---
            
            Generate the refined, theoretically sound knowledge point.
            """
            
            refined_content = self.llm_service.generate_text(prompt, temperature=0.5)
            refined_knowledge_points.append({
                "source": source,
                "refined_content": refined_content,
                "status": "theoretically_analyzed"
            })
            
        # Replace the old drafts with the refined knowledge points
        context["refined_knowledge_points"] = refined_knowledge_points
        context.pop("knowledge_point_drafts", None) # Remove the old drafts
        
        self._log(f"Completed theoretical analysis of {len(refined_knowledge_points)} knowledge points.")
        
        return context
