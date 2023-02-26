from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
import time

# driver = Chrome('./chromedriver')
service = Service("./chromedriver")
driver = Chrome(service=service)
url = 'https://www.dcard.tw/f'

driver.get(url)
# driver.implicitly_wait(30)
time.sleep(5)

js = "var q=document.documentElement.scrollTop=10000"
js2 = "var q=document.documentElement.scrollTop=0"
driver.execute_script(js)
# driver.implicitly_wait(10)
time.sleep(5)
driver.execute_script(js2)
# driver.implicitly_wait(10)
time.sleep(5)
driver.execute_script(js)
# driver.implicitly_wait(10)
time.sleep(5)
driver.execute_script(js2)
# driver.implicitly_wait(10)
# driver.implicitly_wait(10)
time.sleep(5)
driver.execute_script(js)
time.sleep(5)
driver.execute_script(js2)
# driver.implicitly_wait(10)
time.sleep(5)
driver.execute_script(js)
# driver.implicitly_wait(10)
