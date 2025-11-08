import time

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()


# 基本設定
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--start-maximized")

# 設定 User Agent
chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36")

# 排除自動化標誌
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)

driver = Chrome(options=chrome_options)

url = "https://www.dcard.tw/f/photography"

driver.get(url)
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
html = driver.execute_script(
    "return document.getElementsByTagName('html')[0].outerHTML"
)
print(html)
