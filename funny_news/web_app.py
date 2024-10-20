from flask import Flask, render_template
from .news_fetcher import fetch_news, fetch_political_news
from .news_generator import generate_funny_news

app = Flask(__name__, template_folder='../templates')

@app.route('/')
def home():
    real_news = fetch_political_news()
    funny_news = [generate_funny_news(headline) for headline in real_news]
    return render_template('index.html', news_pairs=zip(real_news, funny_news))
