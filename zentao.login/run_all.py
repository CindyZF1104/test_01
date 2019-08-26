import unittest
from common import HTMLTestRunner_cn
casepath = 'C:\\Users\\test\\PycharmProjects\\zentao.login\\case'
rule = 'test*.py'
discover = unittest.defaultTestLoader.discover(start_dir=casepath,pattern=rule)
print(discover)

reportpath = 'C:\\Users\\test\\PycharmProjects\\zentao.login\\report\\'+'report.html'
fp = open(reportpath,'wb')
runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,title='zentao登录报告',description='查看数据')
runner.run(discover)
fp.close()
