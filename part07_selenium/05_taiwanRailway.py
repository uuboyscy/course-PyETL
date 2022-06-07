import requests
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome


url = "https://www.railway.gov.tw/tra-tip-web/tip"
driver = Chrome('./chromedriver')
driver.get(url)

driver.find_element_by_id('startStation').send_keys("1040")
driver.find_element_by_id('endStation').send_keys("7000")
driver.find_element_by_id('rideDate').clear()
driver.find_element_by_id('rideDate').send_keys("20220603")
driver.find_element_by_id('startTime').send_keys("06:00")
driver.find_element_by_id('endTime').send_keys("18:00")

time.sleep(5)
botton = driver.find_element_by_css_selector("#queryForm > div.zone.v-bottom > input")
# botton = driver.find_element_by_xpath('//*[@id="queryForm"]/div[6]/input')
botton.click()