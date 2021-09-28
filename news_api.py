import requests

def getNewsApi():
    url = "http://localhost:8080/news"

    response = requests.get(url)
    newsDto = response.json();

    if newsDto["code"] == 1:
        return newsDto["data"]
    else:
        print(newsDto["msg"])



