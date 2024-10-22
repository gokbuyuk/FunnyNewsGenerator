import requests
from bs4 import BeautifulSoup
from config import NEWS_SOURCE_URL, NUM_NEWS_ITEMS

def fetch_news():
    response = requests.get(NEWS_SOURCE_URL)
    soup = BeautifulSoup(response.content, 'lxml-xml')
    news_items = soup.findAll('item')
    titles = [item.title.text for item in news_items[:NUM_NEWS_ITEMS]]
    articles = [item.description.text for item in news_items[:NUM_NEWS_ITEMS]]
    print('titles: ', titles)
    # print('articles: ', articles)
    return {'titles': titles, 'articles': articles}


def fetch_political_news():
    # Fetch the RSS feed
    response = requests.get(NEWS_SOURCE_URL)
    soup = BeautifulSoup(response.content, 'lxml-xml')
    
    # Find all news items
    news_items = soup.findAll('item')
    
    # Filter only political news based on the keyword "politics"
    political_news = []
    for item in news_items:
        title = item.title.text.lower()  # Convert title to lowercase for case-insensitive search
        description = item.description.text.lower() if item.description else ""
        
        # Check if the title or description contains the word "politics"
        if 'politics' in title or 'politics' in description:
            political_news.append(item.title.text)
        
        # Stop when the desired number of political news items are collected
        if len(political_news) >= NUM_NEWS_ITEMS:
            break
    
    return political_news

# def fetch_google_news():
#     # URL for Google News RSS feed
#     url = "https://news.google.com/rss"
    
#     # Parse the RSS feed
#     feed = feedparser.parse(url)
    
#     articles = []
    
#     for entry in feed.entries:
#         article = {
#             'title': entry.title,
#             'link': entry.link,
#             'published': entry.published
#         }
        
#         # Fetch the full article content (note: this might not work for all news sites)
#         try:
#             response = requests.get(entry.link)
#             soup = BeautifulSoup(response.text, 'html.parser')
            
#             # This is a simple example and might need to be adjusted based on the structure of the news sites
#             article['content'] = soup.find('article').get_text()
#         except:
#             article['content'] = "Could not fetch article content"
        
#         articles.append(article)
    
#     return articles

if __name__ == "__main__":

    # Example usage:
    news = fetch_political_news()
    for idx, title in enumerate(news, 1):
        print(f"{idx}. {title}")
