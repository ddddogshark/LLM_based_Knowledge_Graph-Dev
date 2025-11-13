# src/services/llm_service.py

import requests
import json
from src.config import DEEPSEEK_API_KEY, DEEPSEEK_API_URL, DEEPSEEK_MODEL

class LLMService:
    def __init__(self):
        self.api_key = DEEPSEEK_API_KEY
        self.api_url = DEEPSEEK_API_URL
        self.model = DEEPSEEK_MODEL
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"{self.api_key}"
        }

    def generate_text(self, prompt: str, temperature: float = 0.7) -> str:
        data = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": temperature
        }
        try:
            response = requests.post(self.api_url, headers=self.headers, data=json.dumps(data))
            response.raise_for_status()  # Raise an exception for HTTP errors
            response_json = response.json()
            return response_json["choices"][0]["message"]["content"]
        except requests.exceptions.RequestException as e:
            print(f"Error calling DeepSeek API: {e}")
            return f"Error: {e}"
        except KeyError as e:
            print(f"Error parsing DeepSeek API response: {e}")
            print(f"Full response: {response.text}")
            return f"Error parsing response: {e}"

# Example usage (for testing purposes)
if __name__ == "__main__":
    llm_service = LLMService()
    test_prompt = "What is the capital of France?"
    print(f"Querying LLM with prompt: '{test_prompt}'")
    response_text = llm_service.generate_text(test_prompt)
    print(f"LLM Response: {response_text}")
