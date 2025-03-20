import requests
from bs4 import BeautifulSoup

def scrape_news(company_name):
    url = f"https://news.google.com/rss/search?q={company_name}"  # Using RSS feed for static content
    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to retrieve data.")
        return []

    soup = BeautifulSoup(response.content, "xml")  # Use "xml" parser for RSS
    articles = []

    for item in soup.find_all("item")[:10]:  # Get first 10 news items
        title = item.title.text
        link = item.link.text
        source = item.source.text if item.source else "Unknown"

        articles.append({
            "title": title,
            "source": source,
            "link": link
        })

    return articles