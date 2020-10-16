"""
AUthor:regan
email:8713*****@qq.com
company:wuhan****
"""

import yaml
import os
from common.handle_path import yamldir

yamlPath = os.path.join(yamldir,'data.yaml')
print(yamlPath)
# 加上 ,encoding='utf-8'，处理配置文件中含中文出现乱码的情况。
f = open(yamlPath,'r',encoding='utf-8')

x = yaml.load(f)
# 读数据
print(type(x))
print(x["log"]["age"])
print(x["dl"]["age"])
print(x["xh"])

# 写数据