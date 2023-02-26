import requests


# https://www.nownews.com/cat/column/

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}

url = "https://www.nownews.com/nn-client/api/v1/cat/column/?pid=6065571"

res = requests.get(url, headers=headers)

print(res.json())
