import requests
from bs4 import BeautifulSoup

# https://www.newmobilelife.com/最新文章/

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}

url = "https://www.newmobilelife.com/wp-json/csco/v1/more-posts"

data = {"action": "csco_ajax_load_more", "page": 4, "posts_per_page": 30}

res = requests.post(url, data=data, timeout=600)
jsondata = res.json()

html = jsondata["data"]["content"]

soup = BeautifulSoup(html, "html.parser")
for div in soup.select("div.cs-entry__excerpt"):
    print(div.text)
