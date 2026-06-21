import requests
import json

triplets_to_store = [
    {"head": "Machine Learning", "relation": "is a subset of", "tail": "Artificial Intelligence"},
    {"head": "Machine Learning", "relation": "enables", "tail": "systems to learn from data"},
    {"head": "Supervised Learning", "relation": "is a type of", "tail": "Machine Learning"}
]

url = "http://127.0.0.1:8000/store_triplets"
headers = {"Content-Type": "application/json"}
data = {"triplets": triplets_to_store}

try:
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response.raise_for_status()  # Raise an exception for HTTP errors
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"Error making request: {e}")
except json.JSONDecodeError:
    print(f"Error decoding JSON response: {response.text}")
