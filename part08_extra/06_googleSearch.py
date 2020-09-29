import requests
import pandas as pd
# import jieba
import time
import random
import re
import warnings
from urllib import parse
from urllib3.exceptions import InsecureRequestWarning
from bs4 import BeautifulSoup
warnings.simplefilter('ignore', InsecureRequestWarning)

'''Setup'''
######################################

query_str = '無薪假 資遣'
query_par = ''
simple_data = []  # [[TITLE_1, CONTENT_1, URL_1], [TITLE_2, CONTENT_2, URL_2], ......]
full_data = []

# For tbs parameter
li = ''  # All word match
qdr = ''  # Duration
lr = 'lang_1zh-TW'  # Language
tbs = ''

# Which page, +10 per loop
page = 0

# For file name
save_csv_file_name = 'no_pay_list'
save_folder_name = './'
save_path = ''
snap_time = str(int(time.time()))

# For jieba
user_def_dict_path = ''

# DataFrame column
simple_columns = ['TITLE', 'CONTENTS', 'URL']
full_columns = ['TITLE', 'CONTENTS', 'URL', 'FULL_CONTENT']

######################################

# Compute parameter
with open('./config.txt', 'r', encoding='utf-8') as f:
    plist = f.read().split('\n')
plist = [i for i in plist if len(i.strip()) > 0]
plist = [i for i in plist if i.strip()[0] != '#']
pdist = {i.strip().split('=')[0].strip(): i.strip().split('=')[-1].strip() for i in plist}

# Compose tbs
query_str = pdist['keyword']
query_lst = [i for i in query_str.split(' ') if i != '']
if pdist['duration'] in ['h', 'd', 'w', 'm', 'y']:
    qdr = pdist['duration']
else:
    qdr = 'm'
#

# Compose query_par used in url
for n, q in enumerate(query_lst):
    query_par += parse.quote(q) + ('+' if n < len(query_lst) - 1 else '')

# Set headers and url
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
url = f'https://www.google.com/search?lr=lang_zh-TW&safe=active&rlz=1C1GCEV_enTW864TW864&biw=1920&bih=888&tbs=lr%3Alang_1zh-TW%2Cqdr%3A{qdr}&ei=9f9BXqueFLvWmAWAlL64CQ&q={query_par}&oq={query_par}&start={page}'
print('[Info] Search:', url)

# Inintiate
res = requests.get(url, headers=headers, verify=False)
soup = BeautifulSoup(res.text, 'html.parser')
content_html = soup.select('h3.LC20lb')

while len(content_html) > 0:
    # Initiate data
    tmp_title = ''
    tmp_content = ''
    tmp_url = ''
    tmp_full_content = ''

    time.sleep(random.randint(3, 7))

    # reset url
    url = f'https://www.google.com/search?lr=lang_zh-TW&safe=active&rlz=1C1GCEV_enTW864TW864&biw=1920&bih=888&tbs=lr%3Alang_1zh-TW%2Cqdr%3Am&ei=9f9BXqueFLvWmAWAlL64CQ&q={query_par}&oq={query_par}&start={page}'
    res = requests.get(url, headers=headers, verify=False)
    soup = BeautifulSoup(res.text, 'html.parser')
    content_html = soup.select('h3.LC20lb')
    if len(content_html) == 0:
        break

    for n, html in enumerate(soup.select('div.rc')):
        # Initiate data
        tmp_title = ''
        tmp_content = ''
        tmp_url = ''
        tmp_full_content = ''

        # For tmp_title
        tmp_title = html.select('h3.LC20lb')[0].text

        # For tmp_content
        tmp_content = html.select('div.s span.st')[0].text
        for w in query_lst:
            tmp_content = tmp_content.replace(w, '[[%s]]' % (w))

        # For tmp_url
        tmp_url = html.a['href']

        # For tmp_full_content
        try:
            tmp_res = requests.get(tmp_url, headers=headers, verify=False)
            try:
                tmp_res_text = BeautifulSoup(tmp_res.text, 'html.parser').select('body')[0].text
                re_words = re.compile(u"[\u4e00-\u9fa5]+")
                tmp_re_res = re.findall(re_words, tmp_res_text)
                for rw in tmp_re_res:
                    tmp_full_content += rw + '\n'
            except IndexError:
                tmp_full_content = '網頁請求發生錯誤！'
            except:
                tmp_full_content = '網頁請求發生錯誤！'

        except:
            tmp_full_content = '網頁請求發生錯誤！'
            pass

            # Append data
        tmp_title = tmp_title.replace(',', '，')
        tmp_content = tmp_content.replace(',', '，')
        tmp_url = tmp_url.replace(',', '，')
        tmp_full_content = tmp_full_content.replace(',', '，')
        full_data.append([tmp_title, tmp_content, tmp_url, tmp_full_content])
        simple_data.append([tmp_title, tmp_content, tmp_url])
        print('[Complete]', tmp_title)

    page += 10

df_simple = pd.DataFrame(data=simple_data, columns=simple_columns)
df_full = pd.DataFrame(data=full_data, columns=full_columns)

save_path = save_folder_name + save_csv_file_name + '_simple_' + snap_time + '.csv'
df_simple.to_csv(save_path, index=False)
save_path = save_folder_name + save_csv_file_name + '_full_' + snap_time + '.csv'
df_full.to_csv(save_path, index=False)

print('Finished!')