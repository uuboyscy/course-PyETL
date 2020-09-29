from selenium.webdriver import Chrome

driver = Chrome('./chromedriver')
url = 'https://www.dcard.tw/f'

driver.get(url)
driver.implicitly_wait(30)

js="var q=document.documentElement.scrollTop=10000"
js2="var q=document.documentElement.scrollTop=0"
driver.execute_script(js)
driver.implicitly_wait(10)
driver.execute_script(js2)
driver.implicitly_wait(10)
driver.execute_script(js)
driver.implicitly_wait(10)
driver.execute_script(js2)
driver.implicitly_wait(10)
driver.implicitly_wait(10)
driver.execute_script(js)
driver.execute_script(js2)
driver.implicitly_wait(10)
driver.execute_script(js)
driver.implicitly_wait(10)
