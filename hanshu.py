# 函数
#定义列表形式
def add(x,y,*args):
    print(args)
    return None
print(add(3,4))
print(add(3,4,*[5,6,4,5]))

def c(**kwargs):
    print(kwargs)

d={'x':1,"y":2,"z":3}
print(c(**d))

