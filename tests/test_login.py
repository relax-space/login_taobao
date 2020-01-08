import unittest
import os
import login

# py.test.exe .\tests\test_login.py -s

class TestLogin(unittest.TestCase):
        
    def testLogin(self):
         # 淘宝用户名
        username = os.getenv("T_NAME")
        # 淘宝重要参数，从浏览器或抓包工具中复制，可重复使用
        ua = os.getenv("T_UA")
        # 加密后的密码，从浏览器或抓包工具中复制，可重复使用
        TPL_password2 = os.getenv("T_PWD2")
        ul = login.UsernameLogin(username, ua, TPL_password2)
        err=ul.login()
        self.assertIsNone(err)
                
