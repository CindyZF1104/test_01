from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from common.base import Base
driver = webdriver.Firefox()
driver.get("https://www.baidu.com/")
time.sleep(2)
# title = EC.title_is("百度一下，你就知道")(driver) #判断标题是不是等于"百度一下，你就知道"
# print(title)
# title1 = EC.title_contains("百度一下")(driver)  #判断标题是不是包含"百度一下，你就知道"
# print(title1)
loc1 = ("id","su")
loc2 = ("link text", "新闻")
# ele1 = EC.presence_of_element_located(loc1)(driver)  #判断是不是能定位到loc1，也就是说loc1是否在DOM里
# print(ele1)
# txt = EC.text_to_be_present_in_element(loc2,"新闻")(driver)#判断DOM里的loc1的text是不是预期结果
# print(txt)
# txt1 = EC.text_to_be_present_in_element_value(loc1,"百度一下")(driver)#判断DOM里的loc1的value是不是一致
# print(txt1)
#用base里封装的方法来测试
baidu = Base(driver)
r1 = baidu.is_Title("百度一下，你就知道")
r2 = baidu.is_Title_Contains("你就知道")
print("r1:%s"%r1)
print("r2:%s"%r2)
r3 = baidu.is_text_in_element(loc2,"新闻")
r4 = baidu.is_value_in_element(loc1,"百度一下")
print("r3:%s"%r3)
print("r4:%s"%r4)