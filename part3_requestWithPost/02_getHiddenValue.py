import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}

url = 'https://web.pcc.gov.tw/tps/pss/tender.do?method=goSearch&searchMode=common&searchType=advance&searchTarget=ATM'

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')

for i in soup.select('input[type="hidden"]'):
    try:
        print('%s:\t%s'%(i['name'], i['value']))
    except KeyError:
        pass
