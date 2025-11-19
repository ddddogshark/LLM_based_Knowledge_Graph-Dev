# src/services/llm_service.py

import requests
import json
import time
from src.config import LLM_API_KEY, LLM_API_URL, LLM_MODEL
from requests.exceptions import ReadTimeout, HTTPError

def generate_text_sync(prompt: str, temperature: float = 0.7, retries: int = 3, delay: int = 2, backoff_factor: float = 2.0) -> str:
    """
    A simple, synchronous function to generate text using the LLM API with exponential backoff.
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
            if "choices" not in response_json:
                raise KeyError("The 'choices' key was not found in the response.")
            return response_json["choices"][0]["message"]["content"]
        except HTTPError as e:
            if e.response.status_code == 403:
                print(f"Fatal error calling LLM API: {e.__class__.__name__}: {e}. Stopping retries.")
                return f"Error: {e}"
            else:
                print(f"HTTP error calling LLM API (attempt {attempt + 1}/{retries}): {e.__class__.__name__}: {e}")
        except ReadTimeout as e:
            print(f"ReadTimeout error calling LLM API (attempt {attempt + 1}/{retries}): {e.__class__.__name__}: {e}")
        except (KeyError, json.JSONDecodeError) as e:
            print(f"Error parsing LLM API response (attempt {attempt + 1}/{retries}): {e.__class__.__name__}: {e}")
            if 'response' in locals():
                print(f"Full response: {response.text}")
        
        if attempt < retries - 1:
            sleep_time = delay * (backoff_factor ** attempt)
            print(f"Retrying in {sleep_time:.2f} seconds...")
            time.sleep(sleep_time)
        else:
            return "Error: All retries failed."

# Example usage (for testing purposes)
if __name__ == "__main__":
    test_prompt = "What is the capital of France?"
    print(f"Querying LLM with prompt: '{test_prompt}'")
    response_text = generate_text_sync(test_prompt)
    print(f"LLM Response: {response_text}")
