import requests
from send_email import send_email

topic = "tesla"

api_key = "30784b4e663544838b3df5fb2aa75ea3"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2023-01-26&sortBy=publishedAt&apiKey=" \
      "30784b4e663544838b3df5fb2aa75ea3&" \
      "language=en"
# make request
request = requests.get(url)

# get dic with data
content = request.json()

news_articles = ""

# access the article titles & descriptions
for article in content["articles"][:20]:
    if article["title"] is not None:
      news_articles = "Subject: Today's news" + "\n" \
      + news_articles + article["title"] + "\n" \
      + article["description"] + "\n" + article["url"] + 2*"\n"

news_articles = news_articles.encode("utf-8")
send_email(news_articles)
