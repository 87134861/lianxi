"""
AUthor:regan
email:8713*****@qq.com
company:wuhan****
"""
import os
from common.handle_path import confdir
from configparser import ConfigParser
class HandleConfig(ConfigParser):
    def __init__(self,filename):
        super().__init__()
        self.filename=filename
        self.read(filename,encoding="utf8")
    def write_data(self,section,options,value):
        """写入数据的方法"""
        self.set(section,options,value)
        self.write(fp=open(self.filename,"w"))

# 封装好后读取数据：
conf=HandleConfig(os.path.join(confdir,"config.ini"))
conf1=conf.sections()
print(conf1)
