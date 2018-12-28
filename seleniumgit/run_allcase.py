from common.HTMLReport import HTMLTestRunner
import unittest
import os


#获取当前文件的父目录
cur_dir = os.path.dirname(os.path.realpath(__file__))
#获取存放测试案例的目录
testcase_dir = os.path.join(cur_dir,'cases')
#生成测试报告的存放目录和测试报告的文件
report_dir = os.path.join(cur_dir,'report','testcases_report.html')


discover = unittest.defaultTestLoader.discover(start_dir=testcase_dir,
                                               pattern='test*.py')
with open(report_dir,'wb') as fp:
    runner = HTMLTestRunner(fp,
                            verbosity=2,
                            title='测试案例报告',
                            description='执行测试案例生成的报告')
    runner.run(discover)



