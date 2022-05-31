#使用 TestSuite(),可以降不同的测试用例添加到套件中（作用）

#TestSuite()功能：
#1.addTest(testcase),testcase代表的是测试用例，可以添加不同的测试用例到套件中（单条）
#2.addTest(tests),tests代表的是测试用例，以列表形式显示，可以添加不同的测试用例到套件中（一组）

#使用TestTestrunner()类进行运行测试套件
# run((suite),suite就是测试套件，可以将测试套件进行运行


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
        print("开始运行方法：", sys._getframe().f_code.co_name)

    # 1.输入正确的用户和正确的密码进行登录
    def test_login_success(self):
        print("开始运行方法：", sys._getframe().f_code.co_name)
        except_value = 0
        actual_value = login("admin", "123456").get("code")
        self.assertEqual(except_value, actual_value)

    # 2.输入错误的用户名或密码登录
    def test_user_wrong(self):
        print("开始运行方法：", sys._getframe().f_code.co_name)
        except_value = 1
        actual_value = login("bca", "123456").get("code")
        self.assertEqual(except_value, actual_value)

    # 3 输入空的用户或密码登录
    def test_password_is_null(self):
        print("开始运行方法：", sys._getframe().f_code.co_name)
        except_value = 1
        actual_value = login("admin", "").get("code")
        self.assertEqual(except_value,actual_value)


if __name__ == "__main__":

    #创建一个套件a
    suite_a = unittest.TestSuite()
    suite_a.addTest(Testlogin("test_login_success"))
    suite_a.addTest(Testlogin("test_user_wrong"))
    print(suite_a)

    runner = unittest.TextTestRunner()
    runner.run(suite_a)


