# 若為Mac電腦，請先貼上此段程式碼
########### For Mac user ###########
import os
import ssl

# used to fix Python SSL CERTIFICATE_VERIFY_FAILED
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context
####################################

from urllib import request, parse
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}

url = 'http://httpbin.org/post'

data = {'key1': 'value1', 'key2': 'value2'}
data = bytes(parse.urlencode(data), encoding = 'utf-8')
req = request.Request(url = url, data = data, headers = headers)
res = request.urlopen(req).read().decode('utf-8')

soup = BeautifulSoup(res, 'html.parser')

print(soup.prettify())