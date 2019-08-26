from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("https://www.12306.cn/index/")
time.sleep(3)
# js = 'document.getElementById("train_date").value="2019-09-01"' #用JS给readonly的日历控件赋值
js1 = 'document.getElementById("train_date").removeAttribute("readonly")' #先用js去掉日历控件的readonly属性，再调用selenium的sendkey方法
driver.execute_script(js1)
driver.find_element_by_id("train_date").clear()
driver.find_element_by_id("train_date").send_keys("2019-09-01")