# src/services/llm_service.py

import requests
import json
import time
import aiohttp # Import aiohttp for asynchronous requests
import asyncio # Import asyncio for async operations
from src.config import LLM_API_KEY, LLM_API_URL, LLM_MODEL
from requests.exceptions import ReadTimeout, HTTPError

def generate_text_sync(prompt: str, temperature: float = 0.7, retries: int = 3, delay: int = 2, backoff_factor: float = 2.0, api_key: str = None, api_url: str = None) -> str:
    """
    A synchronous function to generate text using the LLM API with exponential backoff.
    """
    api_key_to_use = api_key or LLM_API_KEY
    api_url_to_use = api_url or LLM_API_URL

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key_to_use}" # Use f-string for Authorization header
    }
    data = {
        "model": LLM_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": temperature
    }

    for attempt in range(retries):
        try:
            response = requests.post(api_url_to_use, headers=headers, data=json.dumps(data), timeout=300.0)
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

async def generate_text_async(prompt: str, temperature: float = 0.7, retries: int = 3, delay: int = 2, backoff_factor: float = 2.0, api_key: str = None, api_url: str = None) -> str:
    """
    An asynchronous function to generate text using the LLM API with exponential backoff.
    """
    api_key_to_use = api_key or LLM_API_KEY
    api_url_to_use = api_url or LLM_API_URL

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key_to_use}" # Use f-string for Authorization header
    }
    data = {
        "model": LLM_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": temperature
    }

    for attempt in range(retries):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(api_url_to_use, headers=headers, data=json.dumps(data), timeout=300.0) as response:
                    response.raise_for_status()
                    response_json = await response.json()
                    if "choices" not in response_json:
                        raise KeyError("The 'choices' key was not found in the response.")
                    return response_json["choices"][0]["message"]["content"]
        except aiohttp.ClientResponseError as e:
            if e.status == 403:
                print(f"Fatal error calling LLM API: {e.__class__.__name__}: {e}. Stopping retries.")
                return f"Error: {e}"
            else:
                print(f"HTTP error calling LLM API (attempt {attempt + 1}/{retries}): {e.__class__.__name__}: {e}")
        except asyncio.TimeoutError:
            print(f"Timeout error calling LLM API (attempt {attempt + 1}/{retries}).")
        except (KeyError, json.JSONDecodeError) as e:
            print(f"Error parsing LLM API response (attempt {attempt + 1}/{retries}): {e.__class__.__name__}: {e}")
            # The response object might not be directly available here, so we skip printing full response for async
        except Exception as e: # Catch other potential aiohttp exceptions
            print(f"Unexpected error calling LLM API (attempt {attempt + 1}/{retries}): {e.__class__.__name__}: {e}")
        
        if attempt < retries - 1:
            sleep_time = delay * (backoff_factor ** attempt)
            print(f"Retrying in {sleep_time:.2f} seconds...")
            await asyncio.sleep(sleep_time) # Use asyncio.sleep for async
        else:
            return "Error: All retries failed."

# Example usage (for testing purposes)
if __name__ == "__main__":
    test_prompt = "What is the capital of France?"
    print(f"Querying LLM with prompt: '{test_prompt}' (sync)")
    response_text_sync = generate_text_sync(test_prompt)
    print(f"LLM Sync Response: {response_text_sync}")

    async def main_async_test():
        print(f"Querying LLM with prompt: '{test_prompt}' (async)")
        response_text_async = await generate_text_async(test_prompt)
        print(f"LLM Async Response: {response_text_async}")

    asyncio.run(main_async_test())