# src/core/agent_manager.py

from typing import Dict, Type
from src.agents.base_agent import BaseAgent
from src.config import get_logger

logger = get_logger(__name__)


class AgentManager:
    """Manages the lifecycle and registration of pipeline agents.

    Agents are registered by class type and instantiated with shared
    LLM API configuration. Provides lookup and listing capabilities.
    """

    def __init__(self):
        self._agents: Dict[str, BaseAgent] = {}

    def register_agent(
        self,
        agent_class: Type[BaseAgent],
        name: str,
        description: str,
        api_key: str = None,
        api_url: str = None,
    ):
        """Register and instantiate an agent by class type.

        Args:
            agent_class: The agent class to instantiate.
            name: Unique name for this agent instance.
            description: Human-readable description of the agent's role.
            api_key: Optional LLM API key override.
            api_url: Optional LLM API URL override.
        """
        if name in self._agents:
            raise ValueError(f"Agent with name '{name}' already registered.")
        self._agents[name] = agent_class(
            name=name, description=description, api_key=api_key, api_url=api_url
        )
        logger.info("Agent '%s' registered.", name)

    def get_agent(self, name: str) -> BaseAgent:
        """Retrieve an agent instance by name."""
        agent = self._agents.get(name)
        if not agent:
            raise ValueError(f"Agent with name '{name}' not found.")
        return agent

    def list_agents(self) -> Dict[str, str]:
        """Return a mapping of agent names to their descriptions."""
        return {name: agent.description for name, agent in self._agents.items()}
