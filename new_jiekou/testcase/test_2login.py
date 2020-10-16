"""
AUthor:regan
email:8713*****@qq.com
company:wuhan****
"""
import unittest
import requests
import jsonpath
from common.excel_handle import Excel_Read
from common.requests_hadle import SendRequests1
import random
from common.case_data import case_data,data
from common.myconfig import conf
import re
class TestLogin(unittest.TestCase):


    def setUp(self):


        self.url = conf.get("env", "base_url") + "/member/login"

        self.headers = eval(conf.get("env", "headers"))
        self.data = data.login
        self.data.update({"mobile_phone":case_data.phone})
        self.method = "post"
        self.requests = SendRequests1()



    def test_login(self):
        response = self.requests.send_requests1(url=self.url, method=self.method,headers=self.headers, json=self.data)
        res = response.json()
        print(res)
    # 使用正则表达式提取登录的电话号码
        phone1 = re.findall("'mobile_phone': '(.+?)', 'reg_name'",str(res))
        print(phone1[0])

    def tearDown(self):
        pass
