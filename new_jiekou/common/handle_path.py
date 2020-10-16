"""
AUthor:regan
email:8713*****@qq.com
company:wuhan****
"""
import os

# res=os.path.abspath(__file__)   #获取当前文件的绝对路径
# res2=os.path.dirname(res)   #获取指定路径的父级目录
# res3=os.path.dirname(res2)  #获取项目路径

#项目路径
basedir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#用例模块的路径
casedir = os.path.join(basedir,"testcase")
#用例数据的路径
datadir = os.path.join(basedir,"data")
#测试报告的路径
reportdir = os.path.join(basedir,"reports")
#配置文件的路径
confdir=os.path.join(basedir,"conf")
#日志文件的路径
logdir= os.path.join(basedir,"logs")
#yaml文件的路径
yamldir= os.path.join(basedir,"conf")