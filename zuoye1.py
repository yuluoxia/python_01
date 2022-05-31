# 1. 输入a,b,c,d4个整数，计算a+b-c*d的结果

# a = int(input("这是一个整数:"))
# b = int(input("这是一个整数:"))
# c = int(input("这是一个整数:"))
# d = int(input("这是一个整数:"))
# sum = 0
# # sum = a+b-c*d
# print(sum)
# 2. 打印1~100内被3整除的所有数的和 。
# sum = 0
# a = 3
# while a <= 100:
#     sum += a
#     a+=3
# print(sum)
# 3. 使用range()输出1~10内的所有奇数 。
# for x in range(1,10,2):
#     print(x)
# 4. 打印1~100所有偶数的和 减去 所有奇数的和 的值
# a = 0
# for x in range(0,101,2):
#     a += x
# print(a)
# b = 0
# for x in range(1,100,2):
#     b+=x
#
# print(b)
# print(a-b)
# 5. 求1+2+3+...+100的和
# sum = 0
# a = 1
# while a <= 100:
#     sum+=a
#     a+=1
#     print(sum)
# 6. 判断一个数n能同时被3和5整除
# n = int(input("这是一个正整数："))
# if n % 3 == 0 and n % 5 == 0:
#     print("n能同时被3和5整除")
# else:
#     print("n不能同时被3和5整除")

# 7. 定义一个整数变量，判断该变量值是否是1-100内的某个数，如果是打印出来
# n = int(input("这是一个整数："))
# if 0 < n <101:
#     print("这个数是1-100内的某个数")
# else:
#     ("这个数不是1-100内的某个数")

# 8. 输入三个整数x,y,z，请把这三个数由小到大输出。备注：输入方法：input()
# x = int(input("这是一个整数："))
# y = int(input("这是一个整数："))
# z = int(input("这是一个整数："))
# print(x<y<z)

# 9. 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，
# 60分以下的用C表示。备注：需要使用input()方法
# a = int(input("学习成绩："))
# if a >= 90:
#     print("A")
# elif 60 <= a <= 89:
#     print("B")
# else:
#     print("c")
# 10. 将一个列表的数据复制到另一个列表中：
# a = [1,2,3,4,5,6,7,89]
# print(a)
# b = a.copy()
# print(b)
# 11. 输出 9*9 乘法口诀表。
# for x in range(1,10):
#     for y in range(1,x+1):
#         print(x,"*",y,"=",x*y,end="     ")
#     print()
# 12. 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
# a = "hfdhfah hdsh shsjh 122 131 "
# zm = 0
# kg = 0
# sz = 0
# other =0
# for x in a:
#     if x.isalpha():
#         zm += 1
#     elif x.isdigit():
#         sz += 1
#     elif x.isspace():
#         kg += 1
#     else:
#         other += 1
# print("字母:",zm)
# print("数字:",sz)
# print("空格:",kg)
# print("其他字符:",other)
# 13. 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个
# 数相加)，几个数相加由键盘控制。
# a = int(input("a等于一个正整数:"))
# n = int(input("n等于一个正整数："))
# sum = 0
# tmp = a
# for i in range(1,n+1):
#
#     sum+=a
#     a=a*10+tmp
#     print(sum)

# 14. 题目：打印出如下图案（菱形）:
# n = 3+1+3
# n1 =2+3+2
# n2 = 1+5+1
# num = 5
# x = num-1
# for n in range(1,num):
#     space = " "*(x-n)
#     star = "*" *(2*(n-1)+1)
#     print(space+star)
# for n in range(1,4):
#     space = n*" "
#     star = (5-(n-1)*2)*"*"
#     print(space+star)



















