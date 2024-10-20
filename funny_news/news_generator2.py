from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import random
from huggingface_hub import login  # For authentication
from config import *

login(HUGGINGFACE_API_TOKEN)

# Adjectives to spice up the headlines
funny_adjectives = [
    "hilarious", "preposterous", "mind-boggling", "earth-shattering",
    "ludicrous", "side-splitting", "uproarious", "knee-slapping",
    "gut-busting", "riotous", "farcical", "sideswiping", "bonkers"
]

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForCausalLM.from_pretrained(MODEL)

def generate_funny_news(headline):
    # Pick a random funny adjective
    funny_adj = random.choice(funny_adjectives)

    # Create the prompt
    prompt = f"Create a short, {funny_adj} news article based on this headline: '{headline}'\n\nFunny Article:"

    # Tokenize the input prompt
    inputs = tokenizer(prompt, return_tensors="pt")  # Convert to tensor format

    # Generate text
    with torch.no_grad():  # Disable gradient calculations (we don't need it for inference)
        output = model.generate(
            inputs.input_ids,
            max_length=500,          # Limit the length of the generated text
            temperature=0.8,         # Adjust the creativity of the output
            num_return_sequences=1,  # Return only one sequence
            pad_token_id=tokenizer.eos_token_id  # Ensure correct padding token
        )

    # Decode the generated output back to text
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

    # Extract the part of the response that comes after "Funny Article:"
    if "Funny Article:" in generated_text:
        funny_article = generated_text.split("Funny Article:")[1].strip()
        # print('funny_article: ', funny_article)
        return funny_article
    else:
        return "Error: Unable to generate funny news article."

# Example usage:
# funny_news = generate_funny_news("Politician Declares Ban on Boring Speeches")
# print(funny_news)
