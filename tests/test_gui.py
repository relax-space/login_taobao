import unittest
import os
import gui_
import utils

"""
1.open firefox developer tools (F12)
2.set position: asset/req.png
3.py.test.exe .\tests\test_gui.py -s
"""

class TestReq(unittest.TestCase):

    def testReqUrl(self):
        # err=gui_.Gui().reqUrl("https://taobao.com")
        # self.assertIsNone(err)
        header,param,err =gui_.Gui().copyHTMLPostLoop(name="login.jhtml")
        self.assertIsNone(err)
        print(header,param)
                
