#1. 输入a,b,c,d4个整数，计算a+b-c*d的结果
a = 0+1
b = a+1
c = b+a
d = a+b+c
e = a+b-c*d
print(e)     # -15
print("=======")

#2. 打印1~100内被3整除的所有数的和 。
a = 0
for x in range(3,100,3):
    a += x
print(a)    # 1683
print("=======")

#3. 使用range()输出1~10内的所有奇数 。

for x in range(1,10,2):
    print(x)
print("=============")

#4. 打印1~100所有偶数的和 减去 所有奇数的和 的值
a = 0
for x in range(2,101,2):
    a += x
print(a)
b = 0
for x in range(1,100,2):
    b += x
print(a)
print(a-b)
print("=======")
#5. 求1+2+3+...+100的和
a = 0
for x in range(1,101):
    a+= x
print(a)
print("=======")
#6. 判断一个数n能同时被3和5整除
n = int(input("请输入一个正整数："))
if n % 3 == 0 and n % 5 == 0:
   print("这个正整数能同时被3和5整除")
else:
   print("这个正整数不能同时被3和5整除")
print('=========')
#7. 定义一个整数变量，判断该变量值是否是1-100内的某个数，如果是打印出来

n = int(input("请输入一个正整数："))
if n > 0 and n < 101:
    print("这个正整数在1到100内")
else:
   print("这个正整数不在1到100内")

print('=========')
#8. 输入三个整数x,y,z，请把这三个数由小到大输出。备注：输入方法：input()
x =int(input("一个数:"))
y =int(input("一个数:"))
z =int(input("一个数:"))
a = [x,y,z]
a.sort()
for b in a:
    print(a)
print('=========')
#9. 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，
#60分以下的用C表示。备注：需要使用input()方法

a = int(input('输入一个成绩'))
if a >= 90:
    print('A同学')
elif 59 < a < 90:
    print("B同学")
else:
    print("c同学")
print('=========')

#10. 将一个列表的数据复制到另一个列表中。
a = [1,2,"ai"]
b = [4,5.1,6]
a.extend(b)
print(a)
 #11. 输出 9*9 乘法口诀表。


#12. 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
a = hfh fs ,k,k,h, ,4,5 , ,4 54  35
yw =
sz = a.isdigit


#13. 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个

#数相加)，几个数相加由键盘控制。















