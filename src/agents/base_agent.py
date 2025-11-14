# src/agents/base_agent.py

from abc import ABC, abstractmethod
from src.services.llm_service import LLMService
from src.database.neo4j_driver import Neo4jDriver
from src.database.mysql_driver import MySQLDriver
from src.database.redis_driver import RedisDriver

class BaseAgent(ABC):
    def __init__(self, name: str, description: str, api_key: str = None, api_url: str = None):
        self.name = name
        self.description = description
        self.llm_service = LLMService(api_key=api_key, api_url=api_url)
        self.neo4j_driver = Neo4jDriver()
        self.mysql_driver = MySQLDriver()
        self.redis_driver = RedisDriver()

    @abstractmethod
    async def execute(self, *args, **kwargs):
        """
        Abstract method for agent execution logic.
        Each agent must implement its specific task here.
        """
        pass

    def _log(self, message: str):
        print(f"[{self.name}] {message}")

    # Common utility methods can be added here
    # For example, methods to interact with LLM, databases, etc.
    # These can be overridden by specific agents if needed.
