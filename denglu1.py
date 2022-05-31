# """
# ## 需求-迭代1：登录功能
# 1. 定义两条用户数据 ，要求用户数据的属性包括用户角色，用户账号，密码，部门
# 2. 要求返回的格式是字典形式 ，包含两个字段，code和message ,code为0代表成功，为1代表失败 ；message给出相应的提示 ，
# 格式如 ：{'code':0,'message':'登录成功'}
# 3. 用户通过控制台输入用户名和密码，判断用户名和密码是否和定义数据中的用户名密码相匹配，
# # 若匹配返回成功登录消息体，并把用户列表也追加到返回结果中,{'code':0,'message':'登录成功',user_list:[]}
# # 4. 若用户名输入为空或密码输入为空，都给出对应的提示，如用户名不能为空
# # 5. 若用户名或密码不匹配，都给出登录失败，请检查您的用户名或密码是否填写正确。提示
# # """
# # 1.定义用户默认数据：[a1,a2]
# user_list = [{'role':'admin','account':'admin','password':'123456','dept':'tester'},{'role':'user','account':'dev','password':'123456','dept':'dev'}]
# #2. 定义默认返回结果
# result ={"code":0,"message":""}
# #3.定义登录功能
# def login(username,password):
#
#     #用户名或密码为空的情况
#     if username is None or username == "":
#         result.update({"code":1,"message":"用户名不能为空"})
#         return result
#     if password is None or username =="":
#         result.update({"code":1,"message":"密码不能为空"})
#         return result
#     #登录成功的情况
#     for user_info in user_list:
#         if username ==user_info.get("account") and password == user_info.get("password"):
#             result.update({"message":"登录成功！","user_list":user_list})
#     #用户名或密码不匹配或错误的情况
#     result.update({"code":1,"message":"请检查您的用户名或密码是否填写正确"})
#     return result
# if __name__ == "__main__":
#     username = input("请输入用户名:")
#     password = input("请输入密码:")
#     print(login(username, password))

# ## 需求-迭代2：用户查询功能:
# 1. 用户查询功能必须是在登录以后才能调用 ，否则给出权限不足提示
# 2. 若输入的用户名正确，返回登录用户的信息，password字段不显示  。
# 3. 若输入的用户名不正确 ，给出无查询结果的提示
# 4. 查询支持模糊查询。

# # 用户查询功能
def get_user(username):
    #判断用户名是否登录，若登录成功可以进行查询：若登录失败，返回权限不足
    if not result.get("code"):
        result.update({"code":11,"message":"用户未登录，无法查询出结果"})
        return result
    #输入正确用户名进行查询，返回结果（支持模糊查询）
    result.update({"user_list":[]})
    lst = [] #存放的是查询到的结果的数据
    for x in user_list:
        account = x.get("accout")
        if username in account:         #支持模糊查询
            x.pop("password")
            lst.append(x)
    #判断新列表里的数据，如果列表不为空，查询成功，返回对应的结果
    if lit:
        result.update({"message":"查询用户成功！","user_list":lst})
        return result
    #若输入的用户名不正确，返回无查询结果提示
    result.update({"code":12,"message":"未查到用户，请重新输入"})
    return result
if __name__ == "__main--":
    #1进行循环，以便用户做各种操作
    flag = true
    while flag:
        #提供用户的各种选择，比如输入1代表登录操作，输入2代表查询操作，输入q:退出操作
        vls = input("操作请输入对应编号:"
                    "\n 1:) 进行登录："
                    "\n 2:) 进行查询用户，请输入用户名:"
                    "\n q:) 退出操作:"
                    "\n 其它字符:) 未知操作，请重新输入:")
        #当输入未知符号后，进行重新输入
        if not vls in("1","2","q","quit"):
            print("=" * 30)
            continue
        #进行登录操作
        if vls =="1":
            username = input("请输入用户名：")
            password = input("请输入密码:")
            loqin_result = login(username,password)
            print(login_result)
            print("=" * 30)
            continue
        # 进行查询用户的情况
        if vls == "2":
            name=input("请输入查询用户名:")
            get_result = get_user(name)
            print(get_result)
            print("=" * 30)
            continue
        #是否退出
        if vls in ("q","quit"):
            flag = False
            print("退出成功！")


