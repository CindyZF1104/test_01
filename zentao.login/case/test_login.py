from selenium import webdriver
import  time
import unittest
from common.zentaologin import testlogin

class Login1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()

    def setUp(self):
        url = 'http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html'
        self.driver.get(url)
        time.sleep(2)

    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def is_login_success(self):
        ''''''
        '''判断是否登录成功'''
        try:
            result = self.driver.find_element_by_xpath('//*[@id="userMenu"]/a').text
            print(result)
            return result
        except:
            return ''

    def is_alert_exist(self):
        ''''''
        '''判断是否有弹框存在'''
        try:
            a = self.driver.switch_to.alert
            alert_text = a.text
            a.accept()
            print(alert_text)
            return  alert_text
        except:
            pass

    def test_01(self):
        '''用例说明:输入正确的用户名密码并登录'''
        testlogin(self.driver,"admin","123456")
        time.sleep(2)
        self.is_alert_exist()
        r = self.is_login_success()
        print("登录的用户名：%s" %r)
        self.assertTrue(r == 'admin')

    def test_02(self):
        '''输入错误的用户名密码登录'''
        testlogin(self.driver,"admin1", "1234")
        time.sleep(2)
        self.is_alert_exist()
        r = self.is_login_success()
        print("登录的用户名：%s"%r)
        self.assertTrue(r == '')

    def test_03(self):
        '''输入错误的用户名密码登录'''
        testlogin(self.driver,"admin", "123456")
        time.sleep(2)
        self.is_alert_exist()
        r = self.is_login_success()
        print("登录的用户名：%s"%r)
        self.assertTrue(r == 'admin')