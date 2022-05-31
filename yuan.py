# 元组
#定义 变量 = （）

tp1 = ()
tp2 = (1,3,1,"hello",None)
print(tp1)
print(tp2)
#2.循环
for x in tp2:
    print(x)
# 打印 1-10的数

for x in (1,2,3,4,5,6,4,5,6,7,8):
    print(x)

#字典（dict）

dct1 = {}
dct2 = {"a":1,"b":2}
print(dct1)
print(dct2)
#2字典的获取

print("获取字典dct2中键名为b的值",dct2["b"])

# 字典的获取，dict.get(键名)
print("获取字典dct2中键名为b的值",dct2.get('b'))

#3.更新字典的某个值，dict["键名“]= 新值

dct2["c"] = 31
print(dct2)

#4,更新字典里的值到另外一个字典，dict.update(dict1)
dct3 = {'e':22,'f':"hello"}
dct2.update(dct3)
print("更新后的字典显示",dct2)

#5 判断字典中是否存在某个键名: "键名" in dict
print("e" in dct2)

# 获取字典中所有的键名：dict.keys()
print("获取字典中所有的键名:",dct2.keys())
for x in dct2.keys():
    print(x)
# 7,获取字典中所有的值，dict.values()
print("获取字典中所有的值:",dct2.values())
for x in dct2.values():
    print(x)

# 获取字典中所有的键值对： dict，items()
print("获取字典中所有的键值对:",dct2.items())
for x,y in dct2.items():
    print(x,"======",y)

#返回一个新字典，以序列seq中元素做字典的键，值为字段所有键对应的初始值
e ={}
e = e.fromkeys(["a","b"],"hello")
print(e)




















