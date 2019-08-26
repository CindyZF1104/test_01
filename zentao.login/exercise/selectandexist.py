from selenium import webdriver
from common.base import Base
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Firefox()
driver.get('http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html')
time.sleep(2)
c = Base(driver)
# loc1 = ('id','account')
# r1 = c.isElementExist1(loc1)#查看元素是否存在，以元组返回
# print(r1)
# loc2 = ('id','account1')
# r2 = c.isElementExist(loc2) #查看元素是否存在
# print(r2)
# loc3 = ('id',"keepLoginon")
# c.click(loc3)  #点击CheckBox
# r3 = c.isSelected(loc3) #判断是否选上
# print(r3)
loc4 = ('id','account')
r= c.isDisplay(loc4)
loc5 = ('id','hiddenwin')
r= c.isDisplay(loc5) #查看隐藏元素
