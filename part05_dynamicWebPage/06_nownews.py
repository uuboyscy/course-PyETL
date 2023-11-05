import requests

# https://www.nownews.com/cat/column/

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
}

url = "https://www.nownews.com/nn-client/api/v1/cat/column/?pid=6294091"

res = requests.get(url, headers=headers, timeout=600)

# print(res.json())

for data in res.json()["data"]["newsList"]:
    article_id = data["id"]
    article_title = data["postTitle"]
    article_url = "https://www.nownews.com" + data["postUrl"]
    article_image_url = data["imageUrl"]

    print(article_id)
    print(article_title)
    print(article_url)
    print(article_image_url)
    print("========")
