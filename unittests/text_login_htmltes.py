
#使用HMTLTestRunner模块生成测试报告，原理，将运行的测试用例结果输出到了HTML，就能用浏览器
#前置条件:



from python02.day2 import login
import unittest
import sys
from unittests.HTMLTestRunner import HTMLTestRunner

class Testlogin(unittest.TestCase):

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
    suite_a.addTest(Testlogin("test_password_is_null"))
    print(suite_a)
    #创建一个测试报告文件，这个文件是HTML格式的
    test_report = "./test_report.html"

    with open(test_report,"wb") as f:


        runner =HTMLTestRunner(f,title="测试报告",description ="测试报告描述")
        runner.run(suite_a)


