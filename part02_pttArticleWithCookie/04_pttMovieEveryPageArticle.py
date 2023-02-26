import os

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}

# 創建資料夾存放文字檔
resource_path = r'./res_movie'
if not os.path.exists(resource_path):
    os.mkdir(resource_path)

page_number = 8296
while page_number >= 8293:
    url = 'https://www.ptt.cc/bbs/movie/index%s.html' % (page_number)

    res = requests.get(url, headers=headers)

    soup = BeautifulSoup(res.text, 'html.parser')

    article_title_html = soup.select('div[class="title"]')

    for each_article in article_title_html:
        try:
            print(each_article.a.text)
            print('https://www.ptt.cc' + each_article.a['href'])

            # 文章網址
            article_url = 'https://www.ptt.cc' + each_article.a['href']
            article_text = each_article.a.text
            # 對文章網址提出請求
            article_res = requests.get(article_url, headers=headers)
            article_soup = BeautifulSoup(article_res.text, 'html.parser')
            # 宣告一個違章內容字串的變數
            article_content = article_soup.select('div#main-content')[0].text.split(
                '--'
            )[0]
            with open(
                r'%s/%s.txt' % (resource_path, article_text), 'w', encoding='utf-8'
            ) as w:
                w.write(article_content)
            print()
        except AttributeError as e:
            print('==========')
            print(each_article)
            print(e.args)
            print('==========')
        except FileNotFoundError as e:
            pass
        except OSError as e:
            pass

    page_number -= 1
