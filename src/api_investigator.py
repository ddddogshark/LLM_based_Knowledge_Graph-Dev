# src/api_investigator.py

import requests
import json
import time
import asyncio
import httpx
from src.config import LLM_API_KEY, LLM_API_URL, LLM_MODEL

def test_prompt_size(max_size=100000, step=1000):
    """
    Tests the maximum prompt size that the LLM API can handle.
    """
    print("--- Testing Prompt Size ---")
    for size in range(step, max_size, step):
        prompt = "a" * size
        headers = {
            "Content-Type": "application/json",
            "Authorization": LLM_API_KEY
        }
        data = {
            "model": LLM_MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0
        }
        try:
            response = requests.post(LLM_API_URL, headers=headers, data=json.dumps(data), timeout=10.0)
            response.raise_for_status()
            print(f"Prompt size {size} successful.")
        except Exception as e:
            print(f"Prompt size {size} failed with error: {e}")
            print(f"Maximum prompt size is likely around {size - step} characters.")
            return

async def test_rate_limits(max_concurrency=100, requests_per_worker=5):
    """
    Tests the rate limits of the LLM API.
    """
    print("\n--- Testing Rate Limits ---")
    
    async def worker(session, worker_id):
        for i in range(requests_per_worker):
            prompt = f"Worker {worker_id}, request {i}"
            headers = {
                "Content-Type": "application/json",
                "Authorization": LLM_API_KEY
            }
            data = {
                "model": LLM_MODEL,
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0
            }
            try:
                response = await session.post(LLM_API_URL, headers=headers, data=json.dumps(data), timeout=10.0)
                response.raise_for_status()
                print(f"Worker {worker_id}, request {i} successful.")
            except Exception as e:
                print(f"Worker {worker_id}, request {i} failed with error: {e}")
                return

    for concurrency in range(1, max_concurrency):
        print(f"\n--- Testing with {concurrency} concurrent workers ---")
        async with httpx.AsyncClient() as session:
            tasks = [worker(session, i) for i in range(concurrency)]
            await asyncio.gather(*tasks)
            await asyncio.sleep(1)

def test_error_responses():
    """
    Tests the error responses of the LLM API.
    """
    print("\n--- Testing Error Responses ---")
    
    # Invalid API key
    headers = {
        "Content-Type": "application/json",
        "Authorization": "invalid_key"
    }
    data = {
        "model": LLM_MODEL,
        "messages": [{"role": "user", "content": "test"}],
        "temperature": 0
    }
    try:
        response = requests.post(LLM_API_URL, headers=headers, data=json.dumps(data), timeout=10.0)
        print(f"Invalid API key response: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Invalid API key failed with error: {e}")

    # Malformed prompt
    headers = {
        "Content-Type": "application/json",
        "Authorization": LLM_API_KEY
    }
    data = {
        "model": LLM_MODEL,
        "messages": [{"role": "user", "content": None}],
        "temperature": 0
    }
    try:
        response = requests.post(LLM_API_URL, headers=headers, data=json.dumps(data), timeout=10.0)
        print(f"Malformed prompt response: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Malformed prompt failed with error: {e}")

if __name__ == "__main__":
    # test_prompt_size()
    # The following test is commented out as it requires httpx and is more complex.
    # It is recommended to run this test in a separate environment if needed.
    asyncio.run(test_rate_limits())
    # test_error_responses()
