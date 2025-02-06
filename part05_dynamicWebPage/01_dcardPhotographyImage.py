"""Archived. Web site changed."""

# 若為Mac電腦，請先貼上此段程式碼
########### For Mac user ###########
import os
import ssl

# used to fix Python SSL CERTIFICATE_VERIFY_FAILED
if not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(
    ssl, '_create_unverified_context', None
):
    ssl._create_default_https_context = ssl._create_unverified_context
####################################

import json
# to save image by request.urlretrieve
from urllib import request

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}

res_path = r'./dcard_photography'
if not os.path.exists(res_path):
    os.mkdir(res_path)

# url = 'https://www.dcard.tw/_api/forums/photography/posts?popular=false&limit=30&before=232004767'
url = 'https://www.dcard.tw/service/api/v2/forums/photography/posts?limit=24&before=234542096'

for i in range(0, 3):

    res = requests.get(url, headers=headers)
    json_string = str(res.text)
    js = json.loads(json_string)

    last_id = js[len(js) - 1]['id']

    for each_article in js:
        print(each_article['title'])
        print('https://www.dcard.tw/f/photography/p/' + str(each_article['id']))
        for n, img_url in enumerate(each_article['mediaMeta']):
            tmp_img_url = img_url['url']
            location = os.path.join(
                res_path + '/%s_%s.jpg' % (each_article['title'].replace('/', ''), n)
            )
            print(('\t' + tmp_img_url), end='')
            request.urlretrieve(tmp_img_url, location)
            print('\tDone.')
        print()

    url = (
        'https://www.dcard.tw/service/api/v2/forums/photography/posts?limit=24&before=%s'
        % (last_id)
    )
