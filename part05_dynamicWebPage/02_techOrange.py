"""Archived. Web site changed."""

import json

import requests
from bs4 import BeautifulSoup

url = 'https://buzzorange.com/techorange/'
url_post = 'https://buzzorange.com/techorange/wp-admin/admin-ajax.php'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}

for page in range(0, 10):
    post_data = {'action': 'fm_ajax_load_more', 'nonce': 'a084a70399', 'page': page + 1}

    res = requests.post(url_post, headers=headers, data=post_data)

    data_dict = json.loads(res.text)
    html = data_dict['data']
    soup = BeautifulSoup(html, 'html.parser')

    for t in soup.select('h4 a'):
        print(t.text)
        print(t['href'])
        print()
