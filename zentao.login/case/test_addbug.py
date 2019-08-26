import unittest
from selenium import webdriver
import time
from pages.addbug_page import addBugPage
from pages.login_page import LoginPage
class addBug(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        # cls.driver.get("http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html")
        # time.sleep(2)
        cls.bug = addBugPage(cls.driver)
        cls.login = LoginPage(cls.driver)
        cls.login.login()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test01(self):
        timestr = time.strftime("%Y%m%d%H%M%S")
        title = "test title" + timestr
        self.bug.add_bug(title)
        r = self.bug.add_bug_is_success(title)
        print(r)
        self.assertTrue(r)

    # def test02(self):
    #     timestr = time.strftime("%Y%m%d%H%M%S")
    #     title = "test title" + timestr
    #     self.bug.add_bug(title)
    #     r = self.bug.add_bug_is_success(title)
    #     print(r)
    #     self.assertTrue(r)