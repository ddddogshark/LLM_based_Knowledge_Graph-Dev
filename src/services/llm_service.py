# src/services/llm_service.py

import json
import time
import asyncio
import aiohttp
import requests
from typing import Optional

from src.config import LLM_API_KEY, LLM_API_URL, LLM_MODEL, get_logger

logger = get_logger(__name__)


def generate_text_sync(
    prompt: str,
    temperature: float = 0.7,
    retries: int = 3,
    delay: int = 2,
    backoff_factor: float = 2.0,
    api_key: Optional[str] = None,
    api_url: Optional[str] = None,
) -> str:
    """Generate text synchronously via LLM API with exponential backoff."""
    key = api_key or LLM_API_KEY
    url = api_url or LLM_API_URL

    if not key or not url:
        logger.error("LLM API key or URL not configured")
        return "Error: LLM not configured."

    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {key}"}
    payload = {"model": LLM_MODEL, "messages": [{"role": "user", "content": prompt}], "temperature": temperature}

    for attempt in range(retries):
        try:
            resp = requests.post(url, headers=headers, json=payload, timeout=300.0)
            resp.raise_for_status()
            data = resp.json()
            if "choices" not in data:
                raise KeyError("Missing 'choices' key in response")
            return data["choices"][0]["message"]["content"]
        except requests.HTTPError as e:
            if e.response is not None and e.response.status_code == 403:
                logger.fatal("LLM API returned 403 — check API key. Stopping.")
                return f"Error: {e}"
            logger.warning("HTTP error (attempt %d/%d): %s", attempt + 1, retries, e)
        except requests.Timeout as e:
            logger.warning("Timeout (attempt %d/%d): %s", attempt + 1, retries, e)
        except (KeyError, json.JSONDecodeError) as e:
            logger.warning("Parse error (attempt %d/%d): %s", attempt + 1, retries, e)

        if attempt < retries - 1:
            sleep_time = delay * (backoff_factor**attempt)
            logger.debug("Retrying in %.2fs...", sleep_time)
            time.sleep(sleep_time)

    logger.error("All %d LLM retries exhausted", retries)
    return "Error: All retries failed."


async def generate_text_async(
    prompt: str,
    temperature: float = 0.7,
    retries: int = 3,
    delay: int = 2,
    backoff_factor: float = 2.0,
    api_key: Optional[str] = None,
    api_url: Optional[str] = None,
) -> str:
    """Generate text asynchronously via LLM API with exponential backoff."""
    key = api_key or LLM_API_KEY
    url = api_url or LLM_API_URL

    if not key or not url:
        logger.error("LLM API key or URL not configured")
        return "Error: LLM not configured."

    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {key}"}
    payload = {"model": LLM_MODEL, "messages": [{"role": "user", "content": prompt}], "temperature": temperature}

    for attempt in range(retries):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url, headers=headers, json=payload, timeout=aiohttp.ClientTimeout(total=300)) as resp:
                    resp.raise_for_status()
                    data = await resp.json()
                    if "choices" not in data:
                        raise KeyError("Missing 'choices' key in response")
                    return data["choices"][0]["message"]["content"]
        except aiohttp.ClientResponseError as e:
            if e.status == 403:
                logger.fatal("LLM API returned 403 — check API key. Stopping.")
                return f"Error: {e}"
            logger.warning("HTTP error (attempt %d/%d): %s", attempt + 1, retries, e)
        except asyncio.TimeoutError:
            logger.warning("Timeout (attempt %d/%d)", attempt + 1, retries)
        except (KeyError, json.JSONDecodeError) as e:
            logger.warning("Parse error (attempt %d/%d): %s", attempt + 1, retries, e)
        except Exception as e:
            logger.warning("Unexpected error (attempt %d/%d): %s", attempt + 1, retries, e)

        if attempt < retries - 1:
            sleep_time = delay * (backoff_factor**attempt)
            logger.debug("Retrying in %.2fs...", sleep_time)
            await asyncio.sleep(sleep_time)

    logger.error("All %d async LLM retries exhausted", retries)
    return "Error: All retries failed."
