# #封装
class Students():
    name = "张三"
    score ="76"
    def __set_score(self,score):
        self.score = score

print(Students.core)
s = Students()
s.score()
print(s.core())


# 类的继承

class People():

    age = 0

    def eat(self,people_type):
        print(people_type,"在吃饭")

class Students(People):
    def eat(self,grade):
        print(grade,"年级学生正在吃饭")

class Teacher(People):
    def eat(self,subject,time):
        print("{}的老师在{}时间吃饭".format(subject,time))

s = Students()
s.eat("2年级")

t = Teacher()
t.eat("语文科目","12")



#多肽













