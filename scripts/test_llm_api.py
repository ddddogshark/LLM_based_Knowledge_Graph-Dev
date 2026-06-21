"""Test script to verify LLM API connectivity.

Usage:
    python scripts/test_llm_api.py

Requires .env file with LLM_API_KEY and LLM_API_URL set.
"""

import os
import sys
import json
import requests
from dotenv import load_dotenv

load_dotenv()

LLM_API_KEY = os.getenv("LLM_API_KEY")
LLM_API_URL = os.getenv("LLM_API_URL")
LLM_MODEL = os.getenv("LLM_MODEL", "Qwen")

if not LLM_API_KEY or not LLM_API_URL:
    print("ERROR: LLM_API_KEY and LLM_API_URL must be set in .env file.")
    sys.exit(1)

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {LLM_API_KEY}",
}

data = {
    "model": LLM_MODEL,
    "messages": [{"role": "user", "content": "who are you"}],
    "temperature": 0,
}

try:
    response = requests.post(LLM_API_URL, headers=headers, json=data, timeout=30)
    response.raise_for_status()
    print("Connection successful!")
    print(json.dumps(response.json(), indent=2))
except requests.exceptions.RequestException as e:
    print(f"Connection failed: {e}")
    sys.exit(1)
