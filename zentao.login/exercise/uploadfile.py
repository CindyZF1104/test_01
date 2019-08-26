from pymouse import PyMouse
import time
from pykeyboard import PyKeyboard
from selenium import webdriver
from pages.login_page import LoginPage


driver = webdriver.Firefox()
login = LoginPage(driver)
login.login()
driver.get("http://127.0.0.1/zentao/bug-create-1-0-moduleID=0.html")
time.sleep(2)
js = 'window.scrollTo(0,200)'
driver.execute_script(js)
time.sleep(1)
driver.find_element_by_css_selector(".ke-toolbar-icon.ke-toolbar-icon-url.ke-icon-image").click()
time.sleep(1)
file = "C:\c.png"
driver.find_element_by_css_selector(".ke-inline-block.ke-upload-button").click()
time.sleep(1)
p = PyKeyboard()
for i in file:
    p.tap_key(i)
time.sleep(2)
# p.tap_key(p.enter_key)
p.tap_key(p.enter_key)
time.sleep(1)
driver.find_element_by_xpath("html/body/div[3]/div[1]/div[3]/span[1]/input").click()