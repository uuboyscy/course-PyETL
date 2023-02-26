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

page_number = 8296
while page_number >= 8293:
    print(page_number)
    url = 'https://www.ptt.cc/bbs/movie/index.html'
    # 首頁index.html其實跟index8296.html是同一個頁面
    url = 'https://www.ptt.cc/bbs/movie/index8296.html'
    url = 'https://www.ptt.cc/bbs/movie/index%s.html' % (page_number)

    res = requests.get(url, headers=headers)

    soup = BeautifulSoup(res.text, 'html.parser')

    # print(soup.prettify())

    article_title_html = soup.select('div[class="title"]')
    # print(article_title_html)

    for each_article in article_title_html:
        try:
            print(each_article.a.text)
            print('https://www.ptt.cc' + each_article.a['href'])
            print()
        except AttributeError as e:
            print('==========')
            print(each_article)
            print(e.args)
            print('==========')

    page_number -= 1
