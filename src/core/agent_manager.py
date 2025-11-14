# src/core/agent_manager.py

from typing import Dict, Type
from src.agents.base_agent import BaseAgent

class AgentManager:
    def __init__(self):
        self._agents: Dict[str, BaseAgent] = {}

    def register_agent(self, agent_class: Type[BaseAgent], name: str, description: str, api_key: str = None, api_url: str = None):
        """
        Registers an agent class and creates an instance of it, passing API configuration.
        """
        if name in self._agents:
            raise ValueError(f"Agent with name '{name}' already registered.")
        self._agents[name] = agent_class(name=name, description=description, api_key=api_key, api_url=api_url)
        print(f"Agent '{name}' registered.")

    def get_agent(self, name: str) -> BaseAgent:
        """
        Retrieves an agent instance by its name.
        """
        agent = self._agents.get(name)
        if not agent:
            raise ValueError(f"Agent with name '{name}' not found.")
        return agent

    def list_agents(self) -> Dict[str, str]:
        """
        Lists all registered agents and their descriptions.
        """
        return {name: agent.description for name, agent in self._agents.items()}

# Example usage (for testing purposes)
if __name__ == "__main__":
    class TestAgent(BaseAgent):
        def __init__(self, name: str, description: str):
            super().__init__(name, description)
            self._log(f"TestAgent '{self.name}' initialized.")

        async def execute(self, task: str):
            self._log(f"Executing task: {task}")
            response = self.llm_service.generate_text(f"Explain: {task}")
            self._log(f"LLM response for '{task}': {response[:100]}...")
            return f"Task '{task}' completed by {self.name}."

    agent_manager = AgentManager()
    agent_manager.register_agent(TestAgent, "TestAgent1", "A simple test agent.")
    agent_manager.register_agent(TestAgent, "TestAgent2", "Another test agent.")

    agent1 = agent_manager.get_agent("TestAgent1")
    import asyncio
    asyncio.run(agent1.execute("What is AI?"))

    print("\nRegistered Agents:")
    for name, desc in agent_manager.list_agents().items():
        print(f"- {name}: {desc}")
