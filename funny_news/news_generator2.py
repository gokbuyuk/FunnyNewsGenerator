from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
import torch
from config import *
import requests
import random
from huggingface_hub import login

# Login to Hugging Face
login(token=HUGGINGFACE_API_TOKEN)

# Adjectives to spice up the headlines
funny_adjectives = [
    "hilarious", "preposterous", "mind-boggling", "earth-shattering",
    "ludicrous", "side-splitting", "uproarious", "knee-slapping",
    "gut-busting", "riotous", "farcical", "sideswiping", "bonkers"
]

# model = 'google/flan-t5-base'
model = "google/flan-t5-large"
# Load the tokenizer and model for text2text generation, passing the API token for authentication
tokenizer = AutoTokenizer.from_pretrained(model, token=HUGGINGFACE_API_TOKEN)
model = AutoModelForSeq2SeqLM.from_pretrained(model, token=HUGGINGFACE_API_TOKEN)


text2text_generator = pipeline("text2text-generation", 
                               model = model, 
                               device_map="auto",
                               tokenizer=tokenizer,
                               max_length=200,
                               do_sample=True)


funny_adj = random.choice(funny_adjectives)

headline = "Trump makes vulgar comments about Arnold Palmer at Pennsylvania rally - CBS News"
prompt = f"Write a funny news story for this news headline: '{headline}'."

response = text2text_generator(prompt)
print(response)


# prompt = f"Write a {funny_adj} news article for this news headline: '{headline}'. \n\n Funny Article:"
# payload = {
#     "inputs": prompt,
#     "parameters": {
#         "max_length": 500,
#         "temperature": 0.7,
#         "num_return_sequences": 1
#     }
# }
# response = requests.post(API_URL, headers=headers, json=payload)



# headers = {"Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"}

def generate_funny_news(headline):
    funny_adj = random.choice(funny_adjectives)

    prompt = f"Write a {funny_adj} news story for this news headline: '{headline}'. \n\n Funny Article:"
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_length": 500,
            "temperature": 0.7,
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


