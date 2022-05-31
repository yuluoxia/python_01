#Testloader():
form python02
import unittests
class Testloader(unittests.TestCase):
    #测试登录的测试用例
    #casel1: 输入正确的用户和正确的密码进行登录
    def test_login_success(self):
