from selenium import webdriver
import time
from common.base import Base

login_url = "http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html"
class LoginPage(Base):  #括号里的参数继承，则不需要实例化，因为Base里已经实例化了
    #登录定位
    loc_user = ("id", "account")
    loc_psw = ("name", "password")
    loc_submit = ("id", "submit")
    loc_user_menu = ("xpath",".//*[@id='userMenu']/a")
    loc_keeplogin = ("id","keepLoginon")
    loc_forget_psw = ("link text","忘记密码")
    loc_forget_psw_refresh = ("xpath","html/body/div[1]/div/div[2]/p/a")

    def input_user(self,user="admin"):
        '''输入用户名'''
        self.sendKeys(self.loc_user, user)  # 输入用户名

    def input_psw(self,psw="123456"):
        '''输入密码'''
        self.sendKeys(self.loc_psw, psw)  # 输入密码

    def keep_login(self,keep_login_button=False):
        '''keep login'''
        if keep_login_button:#如果是False，则点击选中keep login
            self.click(self.loc_keeplogin)

    def click_login(self):
        '''点击登录'''
        self.click(self.loc_submit)  # 点击登录

    def forget_psw(self):
        '''忘记密码'''
        self.click(self.loc_forget_psw)

    def login(self,user="admin",psw="123456",keep_login_button=False):
        '''登录流程'''
        self.driver.get(login_url)#打开网页
        self.input_user(user)#输入用户名
        self.input_psw(psw)#输入密码
        self.click_login()#点击登录
        # self.sendKeys(self.loc_user,user)#输入用户名
        # self.sendKeys(self.loc_psw,psw)#输入密码
        # if keep_login_button: #如果是False，则点击选中keep login
        #     self.click(self.loc_keeplogin)
        # self.click(self.loc_submit)#点击登录

    def get_user(self):
       # r = self.is_text_in_element(self.loc_user,_text)
        user = self.get_text(self.loc_user_menu)
        return user

    def login_result(self,user):
        result = self.is_text_in_element(self.loc_user_menu,user)
        return result

    def alert_accept(self):
        try:
            alert = self.is_alert()
            text = alert.text
            alert.accept()
            return text
        except:
            return ""

    def forget_psw_refresh_check(self):
        '''判断忘记密码页面是否打开'''
        try:
            self.isElementExist(self.loc_forget_psw_refresh)
            return True
        except:
            return False



if __name__ == "__main__":
    driver = webdriver.Firefox()
    # driver.get(login_url)
    # time.sleep(2)
    login = LoginPage(driver)
    login.login()
    # login.input_user("admin")
    # login.input_psw("123456")
    # login.keep_login()
    # login.click_login()

