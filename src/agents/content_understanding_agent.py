# src/agents/content_understanding_agent.py

from src.agents.base_agent import BaseAgent
from typing import Dict, Any, List

class ContentUnderstandingAgent(BaseAgent):
    def __init__(self, name: str, description: str):
        super().__init__(name, description)

    async def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        self._log("Starting content understanding and transformation...")
        
        raw_data: List[Dict[str, str]] = context.get("raw_data", [])
        
        if not raw_data:
            self._log("No raw data found to process.")
            return context
            
        self._log(f"Processing {len(raw_data)} raw data items.")
        
        knowledge_point_drafts = []
        for item in raw_data:
            source = item.get("source", "Unknown source")
            content = item.get("content", "")
            
            self._log(f"Processing content from: {source}")
            
            prompt = f"""
            You are a Content Understanding Agent. Your task is to process the following raw text and
            transform it into a structured "Knowledge Point Draft".
            
            The draft should be a concise summary of the key information in the text.
            It should identify the main concept, its definition, and any key relationships or properties.
            
            Raw Text from {source}:
            ---
            {content}
            ---
            
            Generate the Knowledge Point Draft.
            """
            
            draft = self.llm_service.generate_text(prompt, temperature=0.5)
            knowledge_point_drafts.append({
                "source": source,
                "draft": draft
            })
            
        # Add the drafts to the context
        if "knowledge_point_drafts" not in context:
            context["knowledge_point_drafts"] = []
        context["knowledge_point_drafts"].extend(knowledge_point_drafts)
        
        self._log(f"Generated {len(knowledge_point_drafts)} knowledge point drafts.")
        
        # Clear raw_data to avoid reprocessing in later stages
        context["raw_data"] = []
        
        return context
