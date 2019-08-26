'''
1. 输入admin，输入123456，点登陆
2. 输入admin，输入 ，点登陆
3. 输入admin，输入123456，点记住登录按钮，点登陆
4. 点忘记密码
'''
import unittest
from selenium import webdriver
from pages.login_page import LoginPage
import time
login_url = "http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html"
class LoginPageCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get(login_url)
        cls.login = LoginPage(cls.driver)

    def setUp(self):
        self.login.alert_accept()
        self.driver.delete_all_cookies()
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test01(self):
        '''1. 输入admin，输入123456，点登陆'''
        self.login.input_user("admin")
        self.login.input_psw("123456")
        self.login.click_login()
        result = self.login.get_user()
        self.assertEqual(result,"admin")

    def test02(self):
        '''2. 输入admin，输入 ，点登陆'''
        self.login.input_user("admin")
        self.login.click_login()
        result = self.login.get_user()
        self.assertEqual(result,"")

    def test03(self):
        '''3. 输入admin，输入123456，点记住登录按钮，点登陆'''
        self.login.input_user("admin")
        self.login.input_psw("123456")
        self.login.keep_login()
        self.login.click_login()
        result = self.login.get_user()
        self.assertEqual(result,"admin")

    def test04(self):
        '''4. 点忘记密码'''
        self.login.forget_psw()
        result = self.login.forget_psw_refresh_check()
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()