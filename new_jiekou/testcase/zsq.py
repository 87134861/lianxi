"""
AUthor:regan
email:8713*****@qq.com
company:wuhan****
"""


def a(pp):
    x=10
    def b():
        print(x)
        pp()
    return b
@a
def pp():
    print("ok")

pp()