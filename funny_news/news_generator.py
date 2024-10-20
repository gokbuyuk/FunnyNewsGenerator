from config import *
import requests
import random

# Adjectives to spice up the headlines
funny_adjectives = [
    "hilarious", "preposterous", "mind-boggling", "earth-shattering",
    "ludicrous", "side-splitting", "uproarious", "knee-slapping",
    "gut-busting", "riotous", "farcical", "sideswiping", "bonkers"
]


headers = {"Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"}

def generate_funny_news(news_article):
    funny_adj = random.choice(funny_adjectives)

    prompt = f"Write content to this news headline: {news_article} in a {funny_adj} way. \n\n Funny Article:"
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
        print("Error: Unable to generate funny news at the moment.")
        return "Error: Unable to generate funny news at the moment."
    
    funny_article = response.json()[0]['generated_text'].split("Funny Article:")[1].strip()
    print('funny_article: ', funny_article)
    return funny_article