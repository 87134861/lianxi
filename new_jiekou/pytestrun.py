"""
AUthor:regan
email:8713*****@qq.com
company:wuhan****
"""

import pytest
import time

# 带时间戳的报告
now_time=time.time()


if __name__ == '__main__':
    pytest.main(["--html={}report.html".format(now_time)])
# 此处一定是要传一个列表，及时只有一个值也要要列表