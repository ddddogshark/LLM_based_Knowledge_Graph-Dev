# src/services/llm_service.py

import requests
import json
import time
from src.config import LLM_API_KEY, LLM_API_URL, LLM_MODEL

def generate_text_sync(prompt: str, temperature: float = 0.7, retries: int = 3, delay: int = 2) -> str:
    """
    A simple, synchronous function to generate text using the LLM API.
    """
    headers = {
        "Content-Type": "application/json",
        "Authorization": LLM_API_KEY
    }
    data = {
        "model": LLM_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": temperature
    }

    for attempt in range(retries):
        try:
            response = requests.post(LLM_API_URL, headers=headers, data=json.dumps(data), timeout=120.0)
            response.raise_for_status()
            response_json = response.json()
            return response_json["choices"][0]["message"]["content"]
        except requests.RequestException as e:
            print(f"Error calling LLM API (attempt {attempt + 1}/{retries}): {e.__class__.__name__}: {e}")
            if attempt < retries - 1:
                time.sleep(delay)
            else:
                return f"Error: {e}"
        except KeyError as e:
            print(f"Error parsing LLM API response: {e}")
            if 'response' in locals():
                print(f"Full response: {response.text}")
            return f"Error parsing response: {e}"
    return "Error: All retries failed."

# Example usage (for testing purposes)
if __name__ == "__main__":
    test_prompt = "What is the capital of France?"
    print(f"Querying LLM with prompt: '{test_prompt}'")
    response_text = generate_text_sync(test_prompt)
    print(f"LLM Response: {response_text}")
