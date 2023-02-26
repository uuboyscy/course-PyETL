from selenium.webdriver import Chrome

# from selenium.webdriver import ChromeOptions
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup

###### Deprecated ######
# options = ChromeOptions()
# options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
# print(options.binary_location)
# driver = Chrome('./chromedriver', options=options)
# driver = Chrome('./chromedriver')
########################

service = Service("./chromedriver")
driver = Chrome(service=service)

url = 'https://www.ptt.cc/bbs/index.html'

driver.get(url)
# driver.find_element_by_class_name('board-name').click() # Deprecated
driver.find_element(by=By.CLASS_NAME, value='board-name').click()
# driver.find_element_by_class_name('btn-big').click() # Deprecated
driver.find_element(by=By.CLASS_NAME, value='btn-big').click()

cookie = driver.get_cookies()

driver.close()

ss = requests.session()

# 設定cookies
for c in cookie:
    ss.cookies.set(c['name'], c['value'])

res = ss.get('https://www.ptt.cc/bbs/Gossiping/index.html')
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.prettify())
