"""
AUthor:regan
email:8713*****@qq.com
company:wuhan****
"""
import os
import unittest
from library.HTMLTestRunnerNew import HTMLTestRunner
from common.handle_path import reportdir,casedir

suite = unittest.TestSuite()

loader = unittest.TestLoader()
suite.addTest(loader.discover(casedir))

runner = HTMLTestRunner(stream=open(os.path.join(reportdir,"report.html"),"wb"),
                                                                                                                                                                                                                                                                                                                                                                                                                                                                     title="python项目结构搭建",
                        description="api测试报告",
                        tester="regan")
runner.run(suite)
