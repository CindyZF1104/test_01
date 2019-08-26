from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from common.base import Base

driver = webdriver.Firefox()
driver.get("http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html")
time.sleep(2)
zentao = Base(driver)
r1 = zentao.is_alert()
loc1 = ("id","account")
loc2 = ("name","password")
loc3 = ("id", "submit")
zentao.sendKeys(loc1,"admin1")
zentao.sendKeys(loc2,"123456")
zentao.click(loc3)
time.sleep(2)
r2 = zentao.is_alert()
print("r1:%s"%r1)
print("r2:%s"%r2)
print(r2.text)
print(r2.accept())
driver.quit()