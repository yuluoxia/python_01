# 格式化字符 ： %s
a = "my name is %s" % ("李四")  #格式化字符
print(a)


#格式化整数： %d
a = "张三 今年 %d 岁" %(50)
print(a)

# 格式化浮点数 ：%f
a = "一斤苹果%f" % (5)
print(a)

#辅助指令：m ,n
#a = "一斤苹果%1.1f元" % (3.701)

# 显示左对齐
a = "一斤苹果%-12.2f元" % (3.3789)
print(a)
#数字前面显示+
a = "一斤苹果%+20.2f元" %(3.789)
print(a)
# 使用format去格式化： "{}".format("字符串")
a = "张三 {} 岁".format(25)
print(a)

a = "今天星期{}，张三买了{}斤苹果".format("一",3)
print(a)

print("=====")
# format的位置参数："{0}{3}{1}{2}".format(第一个数，第二个数，第三个数，第四个数)
a = "今天星期{0}，张三买了{1}斤苹果".format("三",5)
print(a)

#format 的关键字参数："{x}{y}".format(x="hello",y="world")

a = "今天星期{y},张三买了{x}斤苹果".format(x="5",y="三")
print(a)
# 位置参数和关键字参数结合使用："{0}{x}".format("hello",x="world")
a = "今天星期{0},张三买了{x}斤苹果".format("5",x="三")
print(a)




