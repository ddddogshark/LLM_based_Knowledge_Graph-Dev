# src/services/llm_service.py

import httpx
import json
import asyncio
from src.config import LLM_API_KEY, LLM_API_URL, LLM_MODEL, LLM_API_KEY_PREFIX # Updated imports

class LLMService:
    def __init__(self, api_key: str = None, api_url: str = None):
        self.api_key = api_key if api_key else LLM_API_KEY
        self.api_url = api_url if api_url else LLM_API_URL
        self.model = LLM_MODEL # Use LLM_MODEL
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"{LLM_API_KEY_PREFIX}{self.api_key}" # Dynamic prefix
        }

    async def generate_text(self, prompt: str, temperature: float = 0.7, retries: int = 3, delay: int = 2) -> str:
        data = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": temperature
        }
        for attempt in range(retries):
            try:
                async with httpx.AsyncClient() as client:
                    response = await client.post(self.api_url, headers=self.headers, data=json.dumps(data), timeout=120.0)
                    response.raise_for_status()
                    response_json = response.json()
                    return response_json["choices"][0]["message"]["content"]
            except httpx.RequestError as e:
                print(f"Error calling LLM API (attempt {attempt + 1}/{retries}): {e.__class__.__name__}: {e}")
                if attempt < retries - 1:
                    await asyncio.sleep(delay)
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
    import asyncio
    llm_service = LLMService()
    test_prompt = "What is the capital of France?"
    print(f"Querying LLM with prompt: '{test_prompt}'")
    response_text = asyncio.run(llm_service.generate_text(test_prompt)) # Await the coroutine
    print(f"LLM Response: {response_text}")
