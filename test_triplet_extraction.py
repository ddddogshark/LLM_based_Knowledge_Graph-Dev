import requests
import json

text_to_extract = 'Machine Learning is a subset of Artificial Intelligence. It enables systems to learn from data. Supervised Learning is a type of Machine Learning.'
url = "http://127.0.0.1:8000/extract_triplets"
headers = {"Content-Type": "application/json"}
data = {"text": text_to_extract}

try:
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response.raise_for_status()  # Raise an exception for HTTP errors
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"Error making request: {e}")
except json.JSONDecodeError:
    print(f"Error decoding JSON response: {response.text}")
