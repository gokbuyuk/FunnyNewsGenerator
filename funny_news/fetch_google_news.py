import feedparser
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timezone

def fetch_todays_google_news():
    # URL for Google News RSS feed
    url = "https://news.google.com/rss"
    
    # Parse the RSS feed
    feed = feedparser.parse(url)
    
    articles = []
    today = datetime.now(timezone.utc).date()
    
    for entry in feed.entries:
        # Convert the published date to a datetime object
        published_date = datetime.strptime(entry.published, "%a, %d %b %Y %H:%M:%S %Z")
        published_date = published_date.replace(tzinfo=timezone.utc)
        
        # Check if the article was published today
        if published_date.date() == today:
            article = {
                'title': entry.title,
                'link': entry.link,
                'published': published_date,
                'summary': entry.summary
            }
            articles.append(article)
    
    return articles

# Fetch and print today's news
todays_news = fetch_todays_google_news()

if todays_news:
    print(f"Found {len(todays_news)} articles from today:\n")
    for article in todays_news:
        print(f"Title: {article['title']}")
        # print(f"Link: {article['link']}")
        # print(f"Published: {article['published'].strftime('%Y-%m-%d %H:%M:%S %Z')}")
        print(f"Summary: {article['summary']}")
        print("\n---\n")
else:
    print("No articles from today found in the feed.")