#测试登录的测试用例
#1.输入正确的用户和正确的密码进行登录
#2.输入错误的用户名或密码登录
#3 输入空的用户或密码登录
from python02.day2 import login
import python02
class Testlogin(python02.TestCase):

    # 1.输入正确的用户和正确的密码进行登录
    def test_login_success(self):
        except_value = 0
        actual_value = login("admin", "123456").get("code")
        self.assertEqual(excpet_value, actual_value)

    # 2.输入错误的用户名或密码登录
    def test_user_wrong(self):
        except_value = 1
        actual_value = login("bca", "123456").get("code")
        self.assertEqual(excpet_value, actual_value)

    # 3 输入空的用户或密码登录
    def test_password_is_null(self):
        except_value = 2
        actual_value = login("admin", "").get("code")
        self.assertEqual(excpet_value, actual_value)


if __name__ == "__main__":
    unittest.main()