import unittest
import os
import gui_
import utils

# py.test.exe .\tests\test_utils.py -s

class TestUtil(unittest.TestCase):

    def testAbsPath(self):
        print(utils.absPath("tests/data"))
        
    def testStrToDict(self):
        exp1 = {'aaa': ''}
        act1 = utils.strToDict("aaa","\n","=")
        self.assertEqual(act1,exp1)
        exp2 = {'aaa': '11'}
        act2=utils.strToDict("aaa=11","\n","=")
        self.assertEqual(act2,exp2)
    
    def testRegex(self):
        str ='''
nickLoginLink
mobileLoginLink=https://login.taobao.com/member/login.jhtml?redirectURL=https://www.taobao.com/&useMobile=true
showAssistantLink
um_token=T90A4D3B40710C978FF908CBCBA0F4420FCB7483FE19BC35EC493E234B5
ua=121212
        '''
        act1 = utils.regex(str,"ua=","\n")
        self.assertEqual(act1,"121212")

    def testRegex(self):
        str ='''
nickLoginLink
mobileLoginLink=https://login.taobao.com/member/login.jhtml?redirectURL=https://www.taobao.com/&useMobile=true
showAssistantLink
um_token=T90A4D3B40710C978FF908CBCBA0F4420FCB7483FE19BC35EC493E234B5
ua=121212'''
        expStr ='''nickLoginLink
mobileLoginLink=1314
showAssistantLink
um_token=T90A4D3B40710C978FF908CBCBA0F4420FCB7483FE19BC35EC493E234B5
ua=121212'''
        actStr = utils.regexSub(str,"mobileLoginLink=1314\n","mobileLoginLink=")
        self.assertEqual(actStr,expStr)
    def testRegex2(self):
        str ='''
nickLoginLink
mobileLoginLink=https://login.taobao.com/member/login.jhtml?redirectURL=https://www.taobao.com/&useMobile=true
showAssistantLink
um_token=T90A4D3B40710C978FF908CBCBA0F4420FCB7483FE19BC35EC493E234B5
ua=121212'''
        expStr ='''nickLoginLink
mobileLoginLink=https://login.taobao.com/member/login.jhtml?redirectURL=https://www.taobao.com/&useMobile=true
showAssistantLink
um_token=T90A4D3B40710C978FF908CBCBA0F4420FCB7483FE19BC35EC493E234B5
ua='''
        actStr = utils.regexSub(str,"ua=\n","ua=")
        self.assertEqual(actStr,expStr)
                
