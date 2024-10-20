# import requests
# from config import *
# import json

# headers = {"Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"}

# def query(payload):
#     response = requests.post(API_URL, headers=headers, json=payload)
#     return response.json()

# output = query({
#     "inputs": "Tell me a funny story about a cat"
# })

# print(json.dumps(output, indent=2))

import requests
import json
from config import *

headers = {"Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"}

payload = {
    "inputs": "Hello, world!"
}

print("Sending payload:", json.dumps(payload, indent=2))

response = requests.post(API_URL, headers=headers, json=payload)

print(f"Status Code: {response.status_code}")
print("Response:")
print(json.dumps(response.json(), indent=2))