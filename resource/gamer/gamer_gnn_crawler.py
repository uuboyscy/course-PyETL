"""
### Gamer crawler
1. latest 10 pages
2. Each title with URL
3. Stars and comments in each article

### URL reference
* Get comment amount
    >- https://gnn.gamer.com.tw/ajax/gnn-html.php?sn=235369
    >- res.json()['data']['comment'] to get HTML then extract the comment amount number
* Get star amount
    >- https://wall.gamer.com.tw/api/link_post.php?url=https://gnn.gamer.com.tw/detail.php?sn=235369
    >- {"data":{"like":3,"isLike":0}}
    ```json
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "referer": "https://gnn.gamer.com.tw/detail.php?sn=235369",
    "cookie": "_gid=GA1.3.800346094.1658831722; __gads=ID=f03b6a46efed39d5:T=1658831737:S=ALNI_MZ0uW5i3TTNa5riIFAdxi5W1eSdhQ; buap_modr=p014; ckForumListOrder=post; ckAPP_VCODE=1328; ckBahamutCsrfToken=fa82599a4bbb0ff1; __gpi=UID=000008175adc3c2a:T=1658831737:RT=1658887731:S=ALNI_MbDpsVR6L5mfXM2uzY9StYVx2wcfQ; ckBahaAd=0------------------------; ckBH_lastBoard=[[%225191%22%2C%22%E6%96%B0%E5%A4%A9%E7%BF%BC%E4%B9%8B%E9%8D%8A%EF%BC%88TalesWeaver%EF%BC%89%22]%2C[%227650%22%2C%22%E6%96%B0%E6%A5%93%E4%B9%8B%E8%B0%B7%22]]; buap_puoo=p301%20p103; _ga=GA1.1.1951735684.1658831722; _ga_2Q21791Y9D=GS1.1.1658904159.4.1.1658906035.60"
}
    ```
"""

import pandas as pd
import requests
import random
import json
import time
import re
import os
from bs4 import BeautifulSoup
# from urllib.parse import unquote


class GamerCrawler:

    def __init__(self):
        self.cxSeries = "partner-pub-9012069346306566:kd3hd85io9c"
        self.cseToken = None  # 3e1664f444e6eb06
        self.cselibVersion = None  # AB1-RNUa21L3zW3YjE3vq6xHeRVG:1658974378322
        self.cseTokenUsedCount = 0

    def genCseToken(self, force=False) -> tuple:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
        }

        url = "https://cse.google.com/cse.js?cx=partner-pub-9012069346306566:kd3hd85io9c"

        cseTokenRePattern = r'"cse_token":[\s]* "[0-9a-zA-Z\-\_:]*"'
        cselibVersionRePattern = r'"cselibVersion":[\s]* "[0-9a-zA-Z\-\_:]*"'

        if self.cseToken == None or self.cseTokenUsedCount > 5 or force:
            res = requests.get(url, headers=headers)
            matchCseTokenObj = re.search(cseTokenRePattern, res.text)
            matchCselibVersionObj = re.search(cselibVersionRePattern, res.text)
            self.cseToken = json.loads("{" + matchCseTokenObj.group(0) + "}")["cse_token"]
            self.cselibVersion = json.loads("{" + matchCselibVersionObj.group(0) + "}")["cselibVersion"]
            self.cseTokenUsedCount = 0
        else:
            self.cseTokenUsedCount += 1

        return (self.cseToken, self.cselibVersion)

    def extractCseText(self, q: str, start=0, sort='date') -> str:
        self.genCseToken()
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
        }
        params = {
            'rsz': '10',
            'num': '10',
            'hl': 'zh-TW',
            'source': 'gcsc',
            'gss': '.tw',
            #             'start': '40',
            'cselibv': self.cselibVersion,
            'cx': self.cxSeries,
            'q': q + ' more:找新聞',
            'safe': 'active',
            'cse_tok': self.cseToken,
            'sort': sort,
            'exp': 'csqr,cc',
            'rsToken': 'undefined',
            'afsExperimentId': 'undefined',
            'callback': 'google.search.cse.api{}'.format(random.randint(148, 17963))
        }
        if not start == 0:
            params["start"] = str(start)

        url = "https://cse.google.com/cse/element/v1"
        res = requests.get(url, params=params, headers=headers)

        return res.text

    def cseTextToJson(self, cseText: str) -> dict:
        rePattern = r'/\*O_o\*/[\r\n]+google.search.cse.api[0-9]+\('
        replaceTo = ''
        resultJsonStr = re.sub(rePattern, replaceTo, cseText)[:-2]

        return json.loads(resultJsonStr)

    def getCommentAmount(self, articleSn: int) -> int:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
        }

        url = "https://gnn.gamer.com.tw/ajax/gnn-html.php?sn={}".format(articleSn)
        res = requests.get(url, headers=headers)
        oriCommentAmountStr = BeautifulSoup(res.json()['data']['comment'], 'html.parser').select_one('p').text  # 顯示所有的 6 則評語
        if '顯示所有的' in oriCommentAmountStr:
            commentAmountStr = oriCommentAmountStr.replace('顯示所有的', '').replace('則評語', '')
            return int(commentAmountStr)
        else:
            return BeautifulSoup(res.json()['data']['comment'], 'html.parser').select('p').__len__() - 1

    def getLikeAmount(self, articleSn: int) -> int:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
            "referer": "https://gnn.gamer.com.tw/detail.php?sn={}".format(articleSn),
            "cookie": "_gid=GA1.3.800346094.1658831722; __gads=ID=f03b6a46efed39d5:T=1658831737:S=ALNI_MZ0uW5i3TTNa5riIFAdxi5W1eSdhQ; buap_modr=p014; ckForumListOrder=post; ckAPP_VCODE=1328; ckBahamutCsrfToken=fa82599a4bbb0ff1; __gpi=UID=000008175adc3c2a:T=1658831737:RT=1658887731:S=ALNI_MbDpsVR6L5mfXM2uzY9StYVx2wcfQ; ckBahaAd=0------------------------; ckBH_lastBoard=[[%225191%22%2C%22%E6%96%B0%E5%A4%A9%E7%BF%BC%E4%B9%8B%E9%8D%8A%EF%BC%88TalesWeaver%EF%BC%89%22]%2C[%227650%22%2C%22%E6%96%B0%E6%A5%93%E4%B9%8B%E8%B0%B7%22]]; buap_puoo=p301%20p103; _ga=GA1.1.1951735684.1658831722; _ga_2Q21791Y9D=GS1.1.1658904159.4.1.1658906035.60"
        }
        params = {
            "url": "https://gnn.gamer.com.tw/detail.php?sn={}".format(articleSn)
        }

        url = "https://wall.gamer.com.tw/api/link_post.php"
        res = requests.get(url, params=params, headers=headers)

        return res.json()['data']['like']

    def getPublishedDate(self, articleSn: int) -> str:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
        }

        url = "https://gnn.gamer.com.tw/detail.php?sn={}".format(articleSn)
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')

        for jsonData in json.loads(soup.select_one('script[type="application/ld+json"]').text):
            if 'datePublished' in jsonData:
                return jsonData['datePublished']


if __name__ == '__main__':
    queryKeyWordList = [
        "RO",
        "RO 仙境傳說",
        "RO 仙境傳說：愛如初見",
        "RO仙境傳説：愛如初見",
        "仙境傳説：愛如初見",
        "天翼之鍊",
        "TALES WEAVER",
        "TALESWEAVER"
    ]

    if not os.path.exists("./gnn_output"):
        os.mkdir("./gnn_output")

    for queryKeyWord in queryKeyWordList:

        gc = GamerCrawler()

        columns = ["title", "like_amount", "comment_amount", "published_date", "article_url"]
        data = list()

        for offSet in range(0, 10):
            extractedCseText = gc.extractCseText(q=queryKeyWord, start=offSet * 10)
            resultData = gc.cseTextToJson(extractedCseText)

            if 'results' not in resultData:
                print("-----------------------")
                print("Regenerate cse_token...")
                print(gc.genCseToken(force=True))
                print("-----------------------")

            for articleObj in resultData['results']:
                title = articleObj['title']
                articleUrl = articleObj['unescapedUrl']
                sn = ''
                commentAmount = -1
                likeAmount = -1
                publishedDate = None

                # Get SN number
                if 'sn=' in articleUrl:
                    sn = articleUrl.split('sn=')[1]
                else:
                    continue

                try:
                    time.sleep(random.randint(2, 5))
                    commentAmount = gc.getCommentAmount(sn)
                except Exception as e:
                    print(e.args)
                    commentAmount = -1

                try:
                    time.sleep(random.randint(2, 5))
                    likeAmount = gc.getLikeAmount(sn)
                except Exception as e:
                    print(e.args)
                    likeAmount = -1

                try:
                    time.sleep(random.randint(2, 5))
                    publishedDate = gc.getPublishedDate(sn)
                except Exception as e:
                    print(e.args)
                    publishedDate = None

                print(title)
                print(articleUrl)
                print("SN:", sn)
                print("commentAmount:", commentAmount)
                print("likeAmount:", likeAmount)
                print("publishedDate:", publishedDate)
                print("========")

                data.append(
                    [title, likeAmount, commentAmount, publishedDate, articleUrl]
                )

                time.sleep(random.randint(2, 20))

            time.sleep(random.randint(30, 60))

        df = pd.DataFrame(data=data, columns=columns)
        df.to_csv(
            "./gnn_output/{}.csv".format(queryKeyWord),
            index=False,
            encoding="utf-8-sig"
        )