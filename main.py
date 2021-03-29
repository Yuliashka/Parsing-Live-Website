# https://news.ycombinator.com/
from bs4 import BeautifulSoup

# to download the data from website we use module:
import requests

# OPENING A WEBPAGE:
# requests allows us to get the data from the particular url:
response = requests.get("https://news.ycombinator.com/newest")
yc_web_page = response.text

# PARCING OUR WEB PAGE TO BEAUTIFUL SOUP:
soup = BeautifulSoup(yc_web_page, "html.parser")

# GETTING 30 ARTICLES FROM OUR WEB SITE:
articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [score.getText() for score in soup.find_all(name="span", class_="score")]
print(article_texts)
print(article_links)
print(article_upvotes)

# TO GET NUMBERS OF VOTES:
article_upvotes_int = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# TO GET MAX VOTE:
max_vote = max(article_upvotes_int)
print(max_vote)

# TO GET ARTICLE AND ITS LINK WITH MAX VOTE:
index_of_max_vote = article_upvotes_int.index(max_vote)
print(article_texts[index_of_max_vote])
print(article_links[index_of_max_vote])


