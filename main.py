from bs4 import BeautifulSoup
import requests

NEWS_URL = "https://www.wired.co.uk/topic/technology"


response = requests.get(NEWS_URL)
data = response.text

soup = BeautifulSoup(data,"html.parser")
all_news = soup.find_all(name="a",class_="SummaryItemHedLink-cgaOJy")

topics = []
links = []

for news in all_news:
    topics.append(news.text)
    links.append(f"https://www.wired.co.uk{news.get('href')}")

print(topics)
print(links)

with open("today's_news.txt","w") as text_file:
    for n in range(len(topics)):
        text_file.write(f"{topics[n]}:{links[n]}\n")
