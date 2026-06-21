# src/config.py

import os
from dotenv import load_dotenv

load_dotenv()

# ---------------------------------------------------------------------------
# LLM API Configuration (supports OpenAI-compatible APIs: Qwen, DeepSeek, etc.)
# ---------------------------------------------------------------------------
LLM_API_KEY = os.getenv("LLM_API_KEY")
LLM_API_URL = os.getenv("LLM_API_URL")
LLM_MODEL = os.getenv("LLM_MODEL", "Qwen")
LLM_API_KEY_PREFIX = os.getenv("LLM_API_KEY_PREFIX", "")

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_API_URL = os.getenv("DEEPSEEK_API_URL")

# ---------------------------------------------------------------------------
# Neo4j Database Configuration
# ---------------------------------------------------------------------------
NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")
NEO4J_DATABASE = os.getenv("NEO4J_DATABASE", "neo4j")

# ---------------------------------------------------------------------------
# MySQL Database Configuration
# ---------------------------------------------------------------------------
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PORT = int(os.getenv("MYSQL_PORT", "3306"))
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DB = os.getenv("MYSQL_DB", "knowledge_graph_raw_data")

# ---------------------------------------------------------------------------
# Redis Configuration
# ---------------------------------------------------------------------------
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
REDIS_DB = int(os.getenv("REDIS_DB", "0"))

# ---------------------------------------------------------------------------
# Other configurations
# ---------------------------------------------------------------------------
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# ---------------------------------------------------------------------------
# Logging setup (shared across all modules)
# ---------------------------------------------------------------------------
import logging

logging.basicConfig(
    level=getattr(logging, LOG_LEVEL, logging.INFO),
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


def get_logger(name: str = None) -> logging.Logger:
    """Get a logger for the given module name."""
    return logging.getLogger(name or __name__)
