from selenium.webdriver import Chrome
from selenium import webdriver
import time

driver = Chrome('./chromedriver')

url = 'https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Dzh-TW%26next%3D%252F&hl=zh-TW&ec=65620&flowName=GlifWebSignIn&flowEntry=ServiceLogin'

driver.get(url)
driver.implicitly_wait(20)

driver.find_element_by_id('identifierId').send_keys('aegis12321@gmail.com')
time.sleep(3)
driver.find_element_by_id('identifierNext').click()
time.sleep(3)
driver.refresh()
driver.find_element_by_id('identifierId').send_keys('aegis12321@gmail.com')
time.sleep(3)
driver.find_element_by_id('identifierNext').click()
with open('./passwd', 'r', encoding='utf-8') as f:
    passwd = f.read()
driver.find_element_by_class_name('whsOnd').send_keys(passwd)
driver.find_element_by_id('passwordNext').click()
time.sleep(15)

cookie_list = driver.get_cookies()
# driver.close()
#
# import requests
# from bs4 import BeautifulSoup
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context
#
# headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
#
# url = 'https://www.youtube.com/'
# url = 'https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Dzh-TW%26next%3D%252F%253Fgl%253DTW%2526hl%253Dzh-TW&hl=zh-TW&ec=65620&flowName=GlifWebSignIn&flowEntry=ServiceLogin'
# url_playlist = 'https://www.youtube.com/view_all_playlists'
# ss = requests.session()
# for c in cookie_list:
#     ss.cookies.set(c['name'], c['value'])
#
# res = ss.get(url_playlist, headers=headers)
# soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.prettify())