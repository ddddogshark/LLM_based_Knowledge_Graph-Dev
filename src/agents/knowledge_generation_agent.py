import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_API_URL = os.getenv("DEEPSEEK_API_URL")

def generate_knowledge(topic: str) -> str:
    """
    Generates knowledge points for a given topic using the DeepSeek API.
    """
    if not DEEPSEEK_API_KEY or not DEEPSEEK_API_URL:
        return "DeepSeek API key or URL not configured."

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
    }

    data = {
        "model": "DeepSeek-R1-671B",
        "messages": [{"role": "user", "content": f"Generate detailed knowledge points about: {topic}"}],
        "temperature": 0.7,
    }

    try:
        response = requests.post(DEEPSEEK_API_URL, headers=headers, data=json.dumps(data))
        response.raise_for_status()  # Raise an exception for HTTP errors
        response_json = response.json()
        return response_json.get("choices", [{}])[0].get("message", {}).get("content", "No content generated.")
    except requests.exceptions.RequestException as e:
        return f"Error calling DeepSeek API: {e}"
    except json.JSONDecodeError:
        return f"Error decoding JSON response from DeepSeek API: {response.text}"
