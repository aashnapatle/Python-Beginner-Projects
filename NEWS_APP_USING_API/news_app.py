import requests
import os
from dotenv import load_dotenv

load_dotenv()
query = input("What type of news are you interested in today? ")
api = os.getenv("NEWS_API_KEY")

url = f"https://newsapi.org/v2/everything?q={query}&from=2026-10-13&sortBy=publishedAt&apiKey={api}"

print(url)
r =  requests.get(url)

data = r.json()

print(data)
print("Status code:", r.status_code)

if data.get("status") == "ok":

    articles = data["articles"]

    for index, article in enumerate(articles):
        print(index + 1, article["title"], article["url"])
        print("\n********************************\n")

else:
    print("API Error:", data.get("message"))