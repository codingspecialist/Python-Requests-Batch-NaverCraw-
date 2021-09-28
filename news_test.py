import requests, json

url = "http://localhost:8080/news"

response = requests.get(url)
newsDto = response.json();

if newsDto["code"] == 1:
    #print(type(newsDto["data"]))
    print(newsDto["data"][0])



