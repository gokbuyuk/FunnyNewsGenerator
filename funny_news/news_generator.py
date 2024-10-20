from config import HUGGINGFACE_API_TOKEN
import requests

HUGGINGFACE_API_TOKEN = HUGGINGFACE_API_TOKEN

API_URL = "https://api-inference.huggingface.co/models/nvidia/Llama-3.1-Nemotron-70B-Instruct-HF"
headers = {"Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"}

def generate_funny_news(headline):
    prompt = f"Create a short, humorous news article based on this headline: '{headline}'\n\nFunny Article:"
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_length": 500,
            "temperature": 0.8,
            "num_return_sequences": 1
        }
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code != 200:
        return "Error: Unable to generate funny news at the moment."
    
    return response.json()[0]['generated_text'].split("Funny Article:")[1].strip()