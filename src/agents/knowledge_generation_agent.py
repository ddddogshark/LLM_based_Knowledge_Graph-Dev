from .base_agent import BaseAgent

class KnowledgeGenerationAgent(BaseAgent):
    def __init__(self, name: str, description: str, api_key: str = None, api_url: str = None):
        super().__init__(name, description, api_key, api_url)

    async def execute(self, topic: str) -> str:
        """
        Generates knowledge points for a given topic using the LLM service.
        """
        self._log(f"Generating knowledge for topic: {topic}")
        prompt = f"Generate detailed knowledge points about: {topic}"
        content = await self.llm_service.generate_text(prompt)
        if "Error" in content:
            self._log(f"Error generating knowledge for '{topic}': {content}")
        else:
            self._log(f"Successfully generated knowledge for '{topic}'.")
        return content
