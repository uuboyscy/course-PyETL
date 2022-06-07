from selenium.webdriver import Chrome
from selenium import webdriver
import time

# 關閉通知
options = webdriver.ChromeOptions()
prefs = {
    'profile.default_content_setting_values':
        {
            'notifications': 2
        }
}
options.add_experimental_option('prefs', prefs)
options.add_argument("disable-infobars")

driver = Chrome('./chromedriver', options=options)

url = 'https://www.facebook.com/?stype=lo&jlou=AfeJLBQc7K4gUKuK2Sa9YSoZGaSW1uPZf0A3yUQOs9OekwXZF4RH0TNW2s5sjXwjgokT5msSzoJKP59gh4kl3UVwebt8J3R_8O8CL9TVRyXV0w&smuh=24235&lh=Ac9Xpw9na_MazgWf'

driver.get(url)
driver.implicitly_wait(20)


driver.find_element_by_id('email').send_keys('hating_318@yahoo.com.tw')
driver.find_element_by_id('pass').send_keys('kyou11')
time.sleep(3)
driver.find_element_by_id('u_0_b').click()

driver.implicitly_wait(20)
time.sleep(10)

cookie_list = driver.get_cookies()

driver.execute_script('var q=document.documentElement.scrollTop=500')

getcontext = driver.find_element_by_css_selector('#jsc_c_1w')
getcontext.click()
print(getcontext.text)

# driver.close()

import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
url = 'https://www.facebook.com'

ss = requests.session()

for c in cookie_list:
    ss.cookies.set(c['name'], c['value'])

# print(ss.cookies)

res = ss.get(url, headers=headers)
print(res.text)
# soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.prettify())