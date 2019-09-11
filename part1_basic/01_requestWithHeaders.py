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

url = 'https://www.ptt.cc/bbs/joke/index.html'

# res = request.urlopen(url)

# 使用headers
useragent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
headers = {'User-Agent' : useragent}
req = request.Request(url = url, headers = headers)
res = request.urlopen(req)

print(res.read().decode('utf-8'))



