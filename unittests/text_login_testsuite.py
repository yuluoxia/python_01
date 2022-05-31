#使用 Testloader(),可以批量去添加测试用例（作用），解决单条测试用例的效率问题

#Testloader():
#可以进行批量运行测试用例：discover(test_dir,patten="test*.py")
  #test_dir: 指定要搜素的路径
  #patten:指定匹配的模式，在test_dir目录下搜索所有的patten的文件
from python02.day2 import login
import unittest
import sys

class Testlogin(unittest.TestCase):


    #初始化方法
    @classmethod
    def setupClass(cls) -> None:
        print("开始运行方法：",sys._getframe().f_code.co_name)
    #清空方法
    @classmethod
    def tearDownClass(cls)-> None:
        print("开始运行方法：",sys._getframe().f_code.co_name)

    # 1.输入正确的用户和正确的密码进行登录
    def test_login_success(self):
        print("开始运行方法：", sys._getframe().f_code.co_name)
        except_value = 0
        actual_value = login("admin","123456").get("code")
        self.assertEqual(except_value, actual_value)

    # 2.输入错误的用户名或密码登录
    def test_user_wrong(self):
        print("开始运行方法：", sys._getframe().f_code.co_name)
        except_value = 1
        actual_value = login("bca","123456").get("code")
        self.assertEqual(except_value, actual_value)

    # 3 输入空的用户或密码登录
    def test_password_is_null(self):
        print("开始运行方法：", sys._getframe().f_code.co_name)
        except_value = 1
        actual_value = login("admin","").get("code")
        self.assertEqual(except_value,actual_value)


if __name__ == "__main__":

    #创建一个套件a
    suite_a = unittest.TestLoader().discover(".",pattern="test_testsuite.py")
    suite_a.addTest(Testlogin("test_login_success"))
    suite_a.addTest(Testlogin("test_user_wrong"))
    print(suite_a)

    runner = unittest.TextTestRunner()
    runner.run(suite_a)


