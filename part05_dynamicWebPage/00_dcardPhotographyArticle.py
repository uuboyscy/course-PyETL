"""Archived. Web site changed."""

import json

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}

# url = 'https://www.dcard.tw/_api/forums/photography/posts?popular=false&limit=30&before=232004767'
url = 'https://www.dcard.tw/service/api/v2/forums/photography/posts?limit=24&before=234542096'

for i in range(0, 5):
    res = requests.get(url, headers=headers)
    json_string = str(res.text)
    js = json.loads(json_string)

    last_id = js[len(js) - 1]['id']

    for each_article in js:
        print(each_article['title'])
        print('https://www.dcard.tw/f/photography/p/' + str(each_article['id']))
        print()

    # url = 'https://www.dcard.tw/_api/forums/photography/posts?popular=false&limit=30&before=%s'%(last_id)
    url = (
        'https://www.dcard.tw/service/api/v2/forums/photography/posts?limit=24&before=%s'
        % (last_id)
    )
