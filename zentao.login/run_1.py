import unittest
from common import HTMLTestRunner_cn

casepath = 'D:\Pycharm Project\zentao.login\case'
rule = 'test*.py'
discover = unittest.defaultTestLoader.discover(start_dir=casepath,pattern=rule)
print(discover)
reportpath = 'D:\\Pycharm Project\\zentao.login\\report\\'+"report.html"
fp = open(reportpath,'wb')
runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,title='baogao',description='xxxxx')
runner.run(discover)
fp.close()