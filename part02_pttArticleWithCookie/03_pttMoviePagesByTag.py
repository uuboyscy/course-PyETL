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

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}

url = 'https://www.ptt.cc/bbs/movie/index.html'
for i in range(0, 3):
    res = requests.get(url, headers=headers)

    soup = BeautifulSoup(res.text, 'html.parser')

    article_title_html = soup.select('div[class="title"]')

    for each_article in article_title_html:
        print(each_article.a.text)
        print('https://www.ptt.cc' + each_article.a['href'])
        print()

    # 印出文章標題後要進入上一頁，必須找到標籤位子
    last_page_url = soup.select('div[class="btn-group btn-group-paging"]')[0].select(
        'a'
    )[1]['href']
    last_page_url = 'https://www.ptt.cc' + last_page_url
    # 讓新的URL取代原本的URL
    url = last_page_url
