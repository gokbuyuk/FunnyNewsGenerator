import requests
from bs4 import BeautifulSoup
from config import NEWS_SOURCE_URL, NUM_NEWS_ITEMS

def fetch_news():
    response = requests.get(NEWS_SOURCE_URL)
    soup = BeautifulSoup(response.content, features="xml")
    news_items = soup.findAll('item')
    return [item.title.text for item in news_items[:NUM_NEWS_ITEMS]]
