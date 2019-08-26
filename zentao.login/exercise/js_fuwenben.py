'''以下js写法只是专门处理富文本（有iframe）相关的问题，其它地方遇到iframe不一定通用'''
from selenium import webdriver
import time
from pages.login_page import LoginPage
from common.base import Base
driver = webdriver.Firefox()
driver.get('http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html')
time.sleep(2)
# login = LoginPage(driver) #实例化login方法并登陆
# login.login("admin","123456")
js1 = '''document.getElementById("account").value="admin"
document.getElementsByName("password")[0].value="123456"
document.getElementById("submit").click()'''
driver.execute_script(js1)
'''添加bug页面的地址'''
loc_test = ("link text", "测试")
loc_bug = ("link text", "Bug")
loc_addbug = ("xpath", ".//*[@id='createActionMenu']/a")  # 添加bug按钮
bug = Base(driver) #实例化并调用base里的方法，切换到添加BUG页面
bug.click(loc_test)
bug.click(loc_bug)
bug.click(loc_addbug)
text = 'hello'
'''js操作很快，这里需要先sleep'''
time.sleep(3)
js = 'document.getElementsByClassName("ke-edit-iframe")[0].contentWindow.document.body.innerHTML="%s"'%text
driver.execute_script(js)

