"""
AUthor:regan
email:8713*****@qq.com
company:wuhan****
"""

import unittest

import jsonpath

from common.requests_hadle import SendRequests1
import random
from common.case_data import case_data,data
from common.myconfig import conf
class TestRegister(unittest.TestCase):
    def setUp(self):
        # 准备测试数据
        phone1="15897749"+str(random.randint(100,1000))

        self.url=conf.get("env","base_url")+"/member/register"
        self.headers=eval(conf.get("env","headers"))

        self.data=data.regeister
        self.data.update({"mobile_phone":phone1})
        self.method="post"
        self.requests=SendRequests1()
    def test_register(self):
        response = self.requests.send_requests1(url=self.url, method=self.method,headers=self.headers, json=self.data)
        self.res = response.json()
        print(self.res)
        # 提取id 以及电话
        id=jsonpath.jsonpath(self.res,"$..id")[0]
        phone=jsonpath.jsonpath(self.res,"$..mobile_phone")[0]
        case_data.id=id
        case_data.phone=phone

    def tearDown(self):
        # 断言
        self.assertEqual(0, self.res["code"])
