# 若為Mac電腦，請先貼上此段程式碼
########### For Mac user ###########
import os
import ssl
# used to fix Python SSL CERTIFICATE_VERIFY_FAILED
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context
####################################

# 引入urllib
from urllib import request
# 引入BeautifulSoup
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/joke/index.html'

# 使用headers
useragent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
headers = {'User-Agent' : useragent}
req = request.Request(url = url, headers = headers)
res = request.urlopen(req)

soup = BeautifulSoup(res, 'html.parser')
action_bar = soup.findAll('div', {'id' : 'action-bar-container'})
action_bar = soup.findAll('div', id='action-bar-container')

print(action_bar)

# Try to get other <div> tag and <a> and in action_bar
tmp_div = action_bar[0].find('div')  # Notice that action_bar is a list
print('Other <div> :')
print(tmp_div)
print()
tmp_a = action_bar[0].find('a')
print('Other <a> :')
print(tmp_a)  # <a class="btn selected" href="/bbs/joke/index.html">看板</a>
print()

# Get text in tag
tmp_text_in_a = tmp_a.text
print('Text in <a> tag :')
print(tmp_text_in_a)
print()

# Other way to get text
tmp_text_in_a = tmp_a.string
print('Text in <a> tag :')
print(tmp_text_in_a)
print()

# Get URL in <a> tag
tmp_url = tmp_a['href']
print('URL :')
print(tmp_url)
print()
print('https://www.ptt.cc'+tmp_url)
