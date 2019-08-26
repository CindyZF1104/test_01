from selenium import webdriver
import time
from common.base import Base


class addBugPage(Base):  #括号里的参数继承，则不需要实例化，因为Base里已经实例化了
    #登录定位
    # loc1 = ("id", "account")
    # loc2 = ("name", "password")
    # loc3 = ("id", "submit")
    #添加bug定位
    loc_test = ("link text","测试")
    loc_bug = ("link text","Bug")
    loc_addbug = ("xpath",".//*[@id='createActionMenu']/a")#添加bug按钮
    loc_trunk = ("xpath",".//*[@id='openedBuild_chosen']/ul")
    loc_trunkbuild = ("css selector",".active-result.highlighted")
    loc_title = ("id", "title")
    #此处需要先切换iframe
    loc_body = ("class name","article-content")
    loc_savebutton = ("id","submit")
    #定位新加的bug是否添加成功
    loc_newbug = ("xpath",".//*[@id='bugList']/tbody/tr/td[4]/a")
    # def __init__(self,driver):
    #由于继承了Base类，并且base类已经实例化过方法，此处不需要实例化
    #     self.driver = driver
    #     self.zentao = Base(self.driver)
    # def login(self,user="admin",psw="123456"):
    #     '''登录'''
    #
    #     self.sendKeys(self.loc1,user)#输入用户名
    #     self.sendKeys(self.loc2,psw)#输入密码
    #     self.click(self.loc3)#点击登录
    def add_bug(self,title):
        '''添加bug'''
        self.click(self.loc_test)#点击测试
        self.click(self.loc_bug)#点击BUG
        self.click(self.loc_addbug)#点击添加bug
        self.click(self.loc_trunk)#点击build
        self.click(self.loc_trunkbuild)#选中build
        self.sendKeys(self.loc_title,title)#输入标题
        frame = self.findElement(("class name","ke-edit-iframe"))
        self.driver.switch_to.frame(frame)#切换到iframe
        # self.clear(self.loc_body)  #富文本不能clear
        body = '''
        test test
        test test
        test test
        '''
        self.sendKeys(self.loc_body, body)#输入文本
        self.driver.switch_to.default_content()
        self.click(self.loc_savebutton)#点击保存

    def add_bug_is_success(self,_text):
        result = self.is_text_in_element(self.loc_newbug,_text)
        return result

if __name__ == "__main__":
    driver = webdriver.Firefox()
    # driver.get("http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html")
    # time.sleep(2)
    bug = addBugPage(driver)
    from pages.login_page import LoginPage
    a = LoginPage(driver)
    a.login()
    timestr = time.strftime("%Y%m%d%H%M%S")
    title = "test title"+timestr
    bug.add_bug(title)
    r = bug.add_bug_is_success(title)
    print(r)
