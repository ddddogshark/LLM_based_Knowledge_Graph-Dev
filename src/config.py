# src/config.py

import os
from dotenv import load_dotenv

load_dotenv()

# LLM API Configuration (Generic for Qwen, DeepSeek, etc.)
LLM_API_KEY = os.getenv("LLM_API_KEY", "YOUR_LLM_API_KEY")
LLM_API_URL = os.getenv("LLM_API_URL", "https://aigc-api.hkust-gz.edu.cn/v1/chat/completions")
LLM_MODEL = os.getenv("LLM_MODEL", "Qwen") # Default to Qwen as per user's example
LLM_API_KEY_PREFIX = os.getenv("LLM_API_KEY_PREFIX", "") # Default to empty string for Qwen, "Bearer " for others if needed

# Neo4j Database Configuration
NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USERNAME = os.getenv("NEO4J_USERNAME", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password")

# MySQL Database Configuration
MYSQL_HOST = os.getenv("MYSQL_HOST", "10.108.6.2")
MYSQL_PORT = int(os.getenv("MYSQL_PORT", "3306"))
MYSQL_USER = os.getenv("MYSQL_USER", "root")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "Hkust@12345")
MYSQL_DB = os.getenv("MYSQL_DB", "knowledge_graph_raw_data")

# Redis Configuration
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
REDIS_DB = int(os.getenv("REDIS_DB", "0"))

# Other configurations
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
