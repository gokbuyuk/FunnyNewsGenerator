import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_funny_news(headline):
    prompt = f"Create a short, humorous news article based on this headline: '{headline}'"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.8,
    )
    return response.choices[0].text.strip()
