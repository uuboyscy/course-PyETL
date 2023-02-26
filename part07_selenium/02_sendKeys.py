from selenium.webdriver import Chrome
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
driver.close()
