import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_API_URL = os.getenv("DEEPSEEK_API_URL")

def extract_triplets(text: str) -> list[dict]:
    """
    Extracts triplets (entity-relation-entity) from a given text using the DeepSeek API.
    """
    if not DEEPSEEK_API_KEY or not DEEPSEEK_API_URL:
        print("DeepSeek API key or URL not configured.")
        return []

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
    }

    prompt = f"""
    Extract all possible knowledge triplets (subject, predicate, object) from the following text. 
    Represent each triplet as a dictionary with keys 'head', 'relation', and 'tail'.
    Return a JSON array of these dictionaries.

    Example:
    Text: "Barack Obama was born in Hawaii."
    Output: [
        {{"head": "Barack Obama", "relation": "born in", "tail": "Hawaii"}}
    ]

    Text:
    {text}
    """

    data = {
        "model": "DeepSeek-R1-671B",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.3, # Lower temperature for more deterministic output
    }

    try:
        response = requests.post(DEEPSEEK_API_URL, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        response_json = response.json()
        content = response_json.get("choices", [{}])[0].get("message", {}).get("content", "[]")
        try:
            triplets = json.loads(content)
            if isinstance(triplets, list):
                return triplets
            else:
                print(f"Warning: DeepSeek API returned non-list content for triplets: {content}")
                return []
        except json.JSONDecodeError:
            print(f"Error decoding JSON response for triplets. Raw content: {content}")
            return []
    except requests.exceptions.RequestException as e:
        print(f"Error calling DeepSeek API for triplet extraction: {e}")
        return []
    except json.JSONDecodeError:
        print(f"Error decoding JSON response for triplets: {content}")
        return []
