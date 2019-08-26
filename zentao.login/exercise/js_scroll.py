from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.cnblogs.com/yoyoketang/")

# js = "window.scrollTo(0,document.body.scrollHeight)" #将滚动条拉倒最底端
# driver.execute_script(js)
# js = "window.scrollTo(0,0)" #将滚动条拉倒最顶端最左边
# driver.execute_script(js)
ele = driver.find_element_by_link_text("python笔记39-unittest框架如何将上个接口的返回结果给下个接口适用(面试必问)")
driver.execute_script("arguments[0].scrollIntoView();",ele)