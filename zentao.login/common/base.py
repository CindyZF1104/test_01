from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


class Base():
    def __init__(self,driver:webdriver.Firefox):
        self.driver = driver
        self.timeout = 10
        self.t = 1

    def findElementNew(self,locator):
        '''通过expected_conditions的presence_of_element_located查找定位元素'''
        if not isinstance(locator,tuple):
            print('locator参数类型错误，必须传元组类型： loc = ("xpath","xxx")')
        else:
            print('正在定位元素信息：定位方式->%s,value值->%s'%(locator[0],locator[1]))
            ele = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(locator))
            return ele

    def findElement(self,locator):
        '''查找定位一个元素'''
        if not isinstance(locator,tuple):
            print('locator参数类型错误，必须传元组类型： loc = ("xpath","xxx")')
        else:
            print('正在定位元素信息：定位方式->%s,value值->%s'%(locator[0],locator[1]))
            ele = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*locator))
            return ele

    def findElements(self,locator):
        '''查找定位一组元素'''
        if not isinstance(locator,tuple):
            print('locator参数类型错误，必须传元组类型： loc = ("xpath","xxx")')
        else:
            print('正在定位元素信息：定位方式->%s,value值->%s'%(locator[0],locator[1]))
            ele = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_elements(*locator))
            return ele

    def sendKeys(self,locator,text):
        '''赋值'''
        ele = self.findElement(locator)
        ele.send_keys(text)

    def move_to_element(self,locator):
        '''鼠标悬停操作'''
        ele = self.findElement(locator)
        ActionChains(driver).move_to_element(ele).perform()

    def click(self,locator):
        '''单击'''
        ele = self.findElement(locator)
        ele.click()

    def clear(self,locator):
        '''清空输入框'''
        ele = self.findElement(locator)
        ele.clear()

    def isSelected(self,locator):
        '''判断元素是否被选中'''
        ele = self.findElement(locator)
        r = ele.is_selected()
        return r

    def isElementExist(self,locator):
        '''判断元素是否存在'''
        try:
            ele = self.findElement(locator)
            return True
        except:
            return False

    def isElementExists(self,locator):
        '''通过定位一组元素判断元素是否存在'''
        eles = self.findElements(locator)
        n = len(eles)
        if n == 0:
            return False
        elif n ==1:
            print("定位到一个元素")
            return True
        else:
            print("定位到多个元素")
            return True

    def isDisplay(self,locator):
        '''判断是否显示，返回bool值'''
        ele = self.findElement(locator)
        r = ele.is_displayed()
        print(r)
        return r

    def is_Title(self,_title):
        '''标题是不是等于预期值 _title是预期标题值，返回bool值'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_is(_title))
            return result
        except:
            return False

    def is_Title_Contains(self,_title):
        '''标题是不是等于预期值 _title是预期标题值，返回bool值'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_contains(_title))
            return result
        except:
            return False

    def is_text_in_element(self,locator,_text):
        '''判断元素文本是不是等于预期值 _title是预期文本值，返回bool值'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element(locator,_text))
            return result
        except:
            return False

    def is_value_in_element(self,locator,_value):
        '''判断元素文本是不是等于预期值 _value是预期文本值，返回bool值,注意：value为空时返回False'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element_value(locator,_value))
            return result
        except:
            return False

    def is_alert(self):
        '''判断alert是否存在，存在则返回alert，不存在就返回false'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.alert_is_present())
            return result
        except:
            return False

    def get_text(self,locator):
        '''获取文本，存在则返回值，不存在就返回空'''
        try:
            result = self.findElement(locator).text
            return result
        except:
            return ""

    def get_Attribute(self,locator,name):
        '''获取属性，存在则返回值，不存在就返回空'''
        try:
            result = self.findElement(locator)
            return result.get_attribute(name)
        except:
            return ""

    def js_scroll_to_end(self):
        '''滚动到底部'''
        js = "window.scrollTo(0,document.body.scrollHeight)" #将滚动条拉倒最底端
        driver.execute_script(js)

    def js_scroll_to_top(self):
        '''滚动到顶部'''
        js = "window.scrollTo(0,0)" #将滚动条拉倒最顶端最左边
        driver.execute_script(js)

    def js_focus_element(self,locator):
        ele = driver.find_element_by_link_text(locator)
        driver.execute_script("arguments[0].scrollIntoView();", ele)

    def select_by_index(self,locator,index=0):
        '''通过index序列选择下拉框选项'''
        selectoption = self.findElement(locator)  #查找选择框
        Select(selectoption).select_by_index(index) #选择对应序列的选项
        selectoption.click() #点击下拉框关闭下拉框

    def select_by_value(self,locator,value):
        '''通过value值选择下拉框选项'''
        selectoption = self.findElement(locator)  #查找选择框
        Select(selectoption).select_by_value(value) #选择对应value的选项
        selectoption.click() #点击下拉框关闭下拉框

    def select_by_text(self,locator,text):
        '''通过text值选择下拉框选项'''
        selectoption = self.findElement(locator)  #查找选择框
        Select(selectoption).select_by_visible_text(text) #选择对应text的选项
        selectoption.click() #点击下拉框关闭下拉框

if __name__ =="__main__":
    driver = webdriver.Firefox()
    driver.get("http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html")
    zentao = Base(driver)
    # loc1 = (By.ID, "account") #先导入包再使用该方法
    # loc2 = (By.NAME, "password")
    # loc3 = (By.ID, "submit")
    loc1 = ("id", "account") #不用导入包
    loc2 = ("name", "password")
    loc3 = ("id", "submit")
    zentao.sendKeys(loc1,"admin")
    zentao.sendKeys(loc2, "123456")
    zentao.click(loc3)