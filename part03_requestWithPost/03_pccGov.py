import requests
from bs4 import BeautifulSoup

url_target = 'https://web.pcc.gov.tw/tps/pss/tender.do?searchMode=common&searchType=advance'

# post data
post_data_str = """method: search
searchMethod: true
searchTarget: ATM
orgName: 
orgId: 
hid_1: 1
tenderName: 
tenderId: 
tenderStatus: 5,6,20,28
tenderWay: 
awardAnnounceStartDate: 109/09/25
awardAnnounceEndDate: 109/09/25
proctrgCate: 
tenderRange: 
minBudget: 
maxBudget: 
item: 
hid_2: 1
gottenVendorName: 
gottenVendorId: 
hid_3: 1
submitVendorName: 
submitVendorId: 
location: 
execLocationArea: 
priorityCate: 
isReConstruct: 
btnQuery: 查詢"""

post_data = {}
for row in post_data_str.split('\n'):
    post_data[row.split(': ')[0]] = row.split(': ')[1]

headers_str = """Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7
Cache-Control: max-age=0
Connection: keep-alive
Content-Length: 429
Content-Type: application/x-www-form-urlencoded
Cookie: cookiesession1=07474E02EBTJJ4APJT7QRLGCNU5FEA3C; JSESSIONID=0000qcPv8ChXqACmnIeBEbDOg_V:148b36dur; NSC_xfc_qfstjtufodf=ffffffff09081f7445525d5f4f58455e445a4a423660
Host: web.pcc.gov.tw
Origin: https://web.pcc.gov.tw
Referer: https://web.pcc.gov.tw/tps/pss/tender.do?method=goSearch&searchMode=common&searchType=advance&searchTarget=ATM
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"""

headers = {}
for row in headers_str.split('\n'):
    headers[row.split(': ')[0]] = row.split(': ')[1]

res = requests.post(url_target, headers=headers, data=post_data)
soup = BeautifulSoup(res.text, 'html.parser')
# print(soup)

title = soup.select('div[id="print_area"] td[align="left"]')

for n, i in enumerate(title):
    if (n+1) % 4 == 2:
        print(i.u.text)
    else:
        print(i.text)
    if (n+1) % 4 == 0:
        print('=' * 20)
