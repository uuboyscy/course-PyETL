# from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
# options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
# print(options.binary_location)
# driver = webdriver.Chrome('./chromedriver', options=options)
driver = webdriver.Chrome('./chromedriver')

url = 'https://www.ptt.cc/bbs/index.html'

driver.get(url)
driver.find_element_by_class_name('board-name').click()
driver.find_element_by_class_name('btn-big').click()

cookie = driver.get_cookies()

driver.close()

ss = requests.session()

# 設定cookies
for c in cookie:
    ss.cookies.set(c['name'], c['value'])

res = ss.get('https://www.ptt.cc/bbs/Gossiping/index.html')
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.prettify())
