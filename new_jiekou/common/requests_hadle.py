"""
AUthor:regan
email:8713*****@qq.com
company:wuhan****
"""
import requests
class SendRequests1(object):
    """不需要鉴权"""
    def __init__(self):
        self.requests= requests


    def send_requests1(self,url,headers,method,params=None,data=None,json=None,files=None):

        if method=="get":
            response=self.requests.get(url=url,headers=headers,params=params)
        elif method=="post":
            response=self.requests.post(url=url,headers=headers,data=data,json=json,files=files)
        elif method=="patch":
            response=self.requests.patch(url=url,headers=headers,data=data,json=json,files=files)
        return response


# class SendRequests2(object):
#     """cookie+session鉴权封装"""
#     def __init__(self):
#         self.session = requests.session()
#
#     def send_requests2(self,url,headers,method,params=None,data=None,json=None,files=None):
#         method=method.lower()
#         if method=="get":
#             response=self.session.get(url=url,headers=headers,params=params)
#         elif method=="post":
#             response=self.session.post(url=url,headers=headers,data=data,json=json,files=files)
#         elif method=="patch":
#             response=self.session.patch(url=url,headers=headers,data=data,json=json,files=files)
#         return response


