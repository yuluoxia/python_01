# #面相对象
# #车的启动
# def car_start():
#     print("车在行驶")

#创建学生类：要求有属性，姓名和年级： 方法有：学习的方法，打印学生的上课情况

class Students():
    name =""
    grade = ""
    def study(self):
        print("{}年级的学生{}正在学习".format(self.grade,self.name))
s1 =Students()
s1.name = "张三"
s1.grade = "5"
print(s1.study())

#的构造方法：
class students1():
    def __init__(self,name,grade):

        self.name = name
        self.grade = grade

    def study(self):

        print("{}年级的学生{}正在学习".format(self.grade,self.name))
s3 = students1("李四","三")
s3.study()






