from urllib import request
from bs4 import BeautifulSoup
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}

# 政治新聞 - Yahoo奇摩新聞
url_yahoo_politics = 'https://tw.news.yahoo.com/rss/politics'
# 批踢踢實業坊 Gossiping 板
url_ptt_gossiping = 'https://www.ptt.cc/atom/Gossiping.xml'
# 聯合新聞網
url_udn = 'https://udn.com/rssfeed/news/2/6638?ch=news'
# 圖書館 News！ :: 隨意窩 Xuite
url_xuite = 'https://blog.xuite.net/ctustlib/blog/rss.xml'
# TechBridge 技術共筆部落格
url_tec_bridge = 'https://blog.techbridge.cc/atom.xml'

# 以 Yahoo奇摩新聞 為例
url = url_yahoo_politics
req = request.Request(url=url, headers=headers)
res = request.urlopen(req)
res = res.read().decode('utf-8')
soup = BeautifulSoup(res)
# soup = BeautifulSoup(res, 'lxml')
title_list = soup.select('title')
for title in title_list:
    print(title.text)
