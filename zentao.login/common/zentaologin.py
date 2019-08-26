
import time
def testlogin(driver,user,psd):
    driver.find_element_by_id("account").send_keys(user)
    driver.find_element_by_name("password").send_keys(psd)
    driver.find_element_by_id("submit").click()

if __name__=="__main__":
    from selenium import  webdriver
    driver = webdriver.Firefox()
    url = 'http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html'
    driver.get(url)
    time.sleep(2)
    testlogin(driver,"admin","123456")
