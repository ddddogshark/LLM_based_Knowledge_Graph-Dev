# src/config.py

import os

# DeepSeek API Configuration
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "YOUR_DEEPSEEK_API_KEY")
DEEPSEEK_API_URL = "https://aigc-api.hkust-gz.edu.cn/v1/chat/completions"
DEEPSEEK_MODEL = os.getenv("DEEPSEEK_MODEL", "DeepSeek-R1-671B") # or "gpt-3.5-turbo", "gpt-4"

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
