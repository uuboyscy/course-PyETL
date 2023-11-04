import requests

# https://www.nownews.com/cat/column/

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
}

url = "https://www.nownews.com/nn-client/api/v1/cat/column/?pid=6294091"

res = requests.get(url, headers=headers, timeout=600)

print(res.json())
