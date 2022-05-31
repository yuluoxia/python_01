## 需求-迭代1：登录功能
# 1. 定义两条用户数据 ，要求用户数据的属性包括用户角色，用户账号，密码，部门
# 2. 要求返回的格式是字典形式 ，包含两个字段，code和message ,code为0代表成功，为1代表失败
# ；message给出相应的提示 ，格式如 ：{'code':0,'message':'登录成功'}
# 3. 用户通过控制台输入用户名和密码，判断用户名和密码是否和定义数据中的用户名密码相匹配，
# 若匹配返回成功登录消息体，并把用户列表也追加到返回结果中,{'code':0,'message':'登录成功',user_list:[]}
# 4. 若用户名输入为空或密码输入为空，都给出对应的提示，如用户名不能为空
# 5. 若用户名或密码不匹配，都给出登录失败，请检查您的用户名或密码是否填写正确。提示
# class User():
#     def __int__(self,ro,ac,pw,dt):
#         self.ac = ac
#         self.pw = pw
#     def logon(self,ac,pw):
#         if self.ac == ac and self.pw == pw:
#             print({"code":0,"message":"登录成功"})
#         elif self.ac =="":
#             print("用户名不能为空")
#         elif self.pw == "":
#             print("密码不能为空")
#         else:
#             print("登录失败，请检查您的用户名或密码是否填写正确")
# u = User()
# u.ac = "admin"
# u.pw = "123456"
# u.logon(ac=input("请输入账号"),pw = input("请输入密码"))

## 需求-迭代1：登录功能
# 1. 定义两条用户数据 ，要求用户数据的属性包括用户角色，用户账号，密码，部门
# 2. 要求返回的格式是字典形式 ，包含两个字段，code和message ,code为0代表成功，为1代表失败
# ；message给出相应的提示 ，格式如 ：{'code':0,'message':'登录成功'}
# 3. 用户通过控制台输入用户名和密码，判断用户名和密码是否和定义数据中的用户名密码相匹配，
# 若匹配返回成功登录消息体，并把用户列表也追加到返回结果中,{'code':0,'message':'登录成功',user_list:[]}
# 4. 若用户名输入为空或密码输入为空，都给出对应的提示，如用户名不能为空
# 5. 若用户名或密码不匹配，都给出登录失败，请检查您的用户名或密码是否填写正确。提示
user_list =  [{'role':'admin','account':'admin','password':'123456','dept':'tester'},{'role':'user','account':'dev','password':'123456','dept':'dev'}]
result ={"code":0,"message":""}
def login(username,password):
    if username is None or username == "":
        result.update({"code":1,"message":"用户名不能为空"})
        return result

    if password is None or username == "":
        result.update({"code":1,"message":"密码不能为空"})
        return result
    for user_info in user_list:
        if username == user_list.get

if __name__ == "__main__":
    username = input("请输入用户名")
    password = input("请输入密码")
    print(login("None","123456"))
    print(login(username,password))





