"""
AUthor:regan
email:8713*****@qq.com
company:wuhan****
"""
import re


s='123hello456'
s1=re.findall("123(.+?)llo",s)
print(s1)