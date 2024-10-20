import requests
from config import HUGGINGFACE_API_TOKEN
import json

API_URL = "https://api-inference.huggingface.co/models/gpt2"
headers = {"Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

output = query({
    "inputs": "Hello, I'm a language model",
})

print(json.dumps(output, indent=2))