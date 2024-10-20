from flask import Flask, render_template
from .news_fetcher import fetch_news, fetch_political_news
from .news_generator import generate_funny_news

app = Flask(__name__, template_folder='../templates')

@app.route('/')
def home():
    real_news_titles = fetch_news()['titles'] 
    print(f"Found {len(real_news_titles)} news articles.")
    real_news_articles = fetch_news()['articles']
    
    # Debug print to ensure the data is being fetched
    # print('real_news: ', real_news)

    # Ensure real_news is not empty
    if not real_news_titles:

        return render_template('index.html', error="No news found.", news_pairs=None)

    funny_news = [generate_funny_news(headline) for headline in real_news_titles]
    print('funny_news: ', funny_news)
    # Debug print to ensure funny news generation is working
    # print('funny_news: ', funny_news)

    # Zip real_news and funny_news so they can be displayed as pairs
    news_pairs = zip(real_news_titles, funny_news)
    # print('news_pairs: ', news_pairs)
    return render_template('index.html', news_pairs=news_pairs)

if __name__ == "__main__":
    app.run(debug=True)
