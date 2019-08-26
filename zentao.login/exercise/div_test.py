from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("C:\\Users\\test\\Desktop\\div.html")
time.sleep(3)
'''scrollTop纵向滚动，scrollLeft横向滚动'''
js = '''document.getElementById("yoyoketang").scrollTop="0"
document.getElementById("yoyoketang").scrollLeft="0"'''
driver.execute_script(js)
