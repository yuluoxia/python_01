
# # # 字符串方法演示
# # # 字符串分割： join(seq)
# #
# # a ="asd"
# # b = a.join("1000")
# # print(b)
#
# # 截取字符串 ：split(str="")
# # c = "hello world"
# # d =c.split("o")
# # print(d)
#
# # 查找字符串：find(subestr),如果找到了返回的是最小索引，没有找到返回 -1
# e = "hellowrold"
# print(e.find("l"))
# print(e.find("x"))
# print(e.index("l"))

# 查找以xxx结尾的字符串： endswith("xxx")
f ="测试报告.doc"
if f.endswith(".doc"):
    print("它是一个word文档")

# 替换字符串： replace(old_valu,new_value)
g = "hello world"
h = g.replace("world","python")
print(h)






#序列的通用操作
#1. 索引 - 列表，序列，字符串
#a = ["red","hello",2,3,4]
#print(a[1])
#print(a[-1])
#a = "fsdafasfsa"
#print(a[3])
#print(a[-2])

#2，序列的切片
#a = [0,1,2,3,4,5,6]
#print(a[2:7:2])
# a = (1,2,3,"a",5,6)
# print(a[1:6:2])
#
# #
# a = (1,2,3,"a",5,6)
# print(a[2::])
# print(a[::2])
# print(a[:2:])
# print(a[1::])
# print(a[1:])
# a = (1,2,3,4,5,6,7,8,9,10)
# print(a[::2])
# print("====")
#
# a = [1,2,3,4,5]
# b = ['red',"abc","dada"]
# c = a+b
# print(c)
# print((a+b)*2)
# print(a*5)
# print(a+a)





