# src/agents/base_agent.py

from abc import ABC, abstractmethod
from src.config import get_logger

# Database imports are optional; they are initialized lazily.
# Each agent that needs DB access should import the specific driver.

logger = get_logger(__name__)


class BaseAgent(ABC):
    """Abstract base class for all pipeline agents.

    Each agent is responsible for one stage in the KG construction pipeline.
    Subclasses must implement the ``execute()`` async method.
    """

    def __init__(self, name: str, description: str, api_key: str = None, api_url: str = None):
        self.name = name
        self.description = description
        self.api_key = api_key
        self.api_url = api_url
        # Database drivers are initialized on-demand by subclasses
        self.neo4j_driver = None
        self.mysql_driver = None
        self.redis_driver = None

    @abstractmethod
    async def execute(self, *args, **kwargs):
        """Execute the agent's main task. Must be implemented by subclasses."""
        pass

    def _log(self, message: str, level: str = "info"):
        """Log a message with the agent's name as prefix."""
        log_func = getattr(logger, level, logger.info)
        log_func("[%s] %s", self.name, message)
