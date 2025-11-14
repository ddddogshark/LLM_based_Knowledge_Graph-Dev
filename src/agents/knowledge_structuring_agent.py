import json
from .base_agent import BaseAgent

class KnowledgeStructuringAgent(BaseAgent):
    def __init__(self, name: str, description: str, api_key: str = None, api_url: str = None):
        super().__init__(name, description, api_key, api_url)

    async def execute(self, text: str) -> list[dict]:
        """
        Extracts triplets (entity-relation-entity) from a given text using the LLM service.
        """
        self._log(f"Extracting triplets from text (first 100 chars): {text[:100]}...")
        prompt = f"""
    Extract all possible knowledge triplets (subject, predicate, object) from the following text.
    Represent each triplet as a dictionary with keys 'head', 'relation', and 'tail'.
    Return a JSON array of these dictionaries.

    Example:
    Text: "Barack Obama was born in Hawaii."
    Output: [
        {{"head": "Barack Obama", "relation": "born in", "tail": "Hawaii"}}
    ]

    Text:
    {text}
    """
        content = await self.llm_service.generate_text(prompt, temperature=0.3) # Lower temperature for more deterministic output
        
        if "Error" in content:
            self._log(f"Error extracting triplets: {content}")
            return []
        
        try:
            triplets = json.loads(content)
            if isinstance(triplets, list):
                self._log(f"Successfully extracted {len(triplets)} triplets.")
                return triplets
            else:
                self._log(f"Warning: LLM returned non-list content for triplets: {content}")
                return []
        except json.JSONDecodeError:
            self._log(f"Error decoding JSON response for triplets. Raw content: {content}")
            return []
