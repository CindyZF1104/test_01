'''
1. 输入admin，输入123456，点登陆
2. 输入admin，输入 ，点登陆
3. 输入admin111，输入123456，点登陆
4. 点忘记密码
'''
import unittest
from selenium import webdriver
from pages.login_page import LoginPage
import ddt
from common.read_excel import ExcelRead
import os
url = "http://127.0.0.1/zentao/user-login.html"
#直接在代码中传入测试数据
testdata = [
    {"user": "admin", "psw": "123456", "exp": "admin"},
    {"user": "admin", "psw": "", "exp": ""},
    {"user": "admin111", "psw": "123456", "exp": ""}
]

# filepath = "C:\\Users\\test\\PycharmProjects\\zentao.login\\common\\data.xlsx" #绝对路径  用excel 获取数据
#相对路径
# currentpath = os.path.realpath(__file__)  #获取当前路径
# packagepath = os.path.dirname(currentpath) #获取当前路径的包名
# projectpath = os.path.dirname(packagepath) #获取当前路径的project名
# filepath = os.path.join(projectpath,"common","data.xlsx") #切换到project下其他包里的文件路径
#
# data = ExcelRead(filepath)#读取文件
# exceldata = data.dictData() #读取数据
# print(exceldata)
@ddt.ddt
class Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.login = LoginPage(cls.driver)

    def setUp(self):
        self.driver.get(url)

    def tearDown(self):
        self.login.alert_accept()
        self.driver.delete_all_cookies()
        self.driver.refresh()
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def login_case(self,user,psw,exp):
        self.login.input_user(user)
        self.login.input_psw(psw)
        self.login.click_login()
        result = self.login.login_result(user)
        print(result)
        self.assertEqual(result,exp)
    @ddt.data({"user": "admin", "psw": "123456", "exp": True},
    {"user": "admin", "psw": "", "exp": False},
    {"user": "admin111", "psw": "123456", "exp": False})
    # @ddt.data(*exceldata)
    def test01(self,data):
        # data1 = testdata[0]
        print("输入的测试数据为%s"%data)
        self.login_case(data["user"],data["psw"],data["exp"])

    # def test02(self):
    #     data2 = testdata[1]
    #     print("输入的测试数据为%s" % data2)
    #     self.login_case(data2["user"], data2["psw"], data2["exp"])
    #
    # def test03(self):
    #     data3 = testdata[2]
    #     print("输入的测试数据为%s" % data3)
    #     self.login_case(data3["user"], data3["psw"], data3["exp"])