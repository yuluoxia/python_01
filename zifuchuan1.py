#字符串方法演示
#字符串分割：join(seq)
astr = "+"
bstr = astr.join("world")
print(bstr)

#2.截取字符串：split(str= “”)
cstr = "a1 = a2 = a3 = a4"
dstr = cstr.split("a3")
print(dstr)

#查找字符串： find()
e = "a = a2 = a3 = a4"
print(e.find("="))
# 替换字符串： replace(old_value,new_value)
g ="hello world"
h = g.replace("world","python")
print(h)

