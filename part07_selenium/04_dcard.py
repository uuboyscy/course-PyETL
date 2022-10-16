from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

driver = Chrome('./chromedriver')
url = 'https://www.dcard.tw/f'

driver.get(url)
time.sleep(5)

# 在表單輸入特定關鍵字
# driver.find_element_by_tag_name('input').send_keys('攝影')
driver.find_element(by=By.TAG_NAME, value='input').send_keys('攝影')
time.sleep(5)

# 按下查詢按鈕
driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div[1]/div/div[1]/div/div/form/button[2]').click()
time.sleep(5)

# 將網頁畫面往下滾動至離頂部 5000 高度的位子
driver.execute_script('var s = document.documentElement.scrollTop=5000')
time.sleep(5)

# 將網頁畫面滾到最上方
driver.execute_script('var s = document.documentElement.scrollTop=0')
time.sleep(5)

driver.execute_script('var s = document.documentElement.scrollTop=10000')
time.sleep(5)

# 取得目前的 html 字串
html = driver.execute_script("return document.getElementsByTagName('html')[0].outerHTML")
print(html)
