import unittest
import req
import os
import utils
import dto

"""
py.test.exe .\tests\test_req.py -s
"""

class TestReq(unittest.TestCase):
    
    def testReadHeader(self):
        str = """
POST /member/login.jhtml?redirectURL=https%3A%2F%2Fwww.taobao.com%2F HTTP/1.1
Host: login.taobao.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 2786
Origin: https://login.taobao.com
Connection: keep-alive
Referer: https://login.taobao.com/member/login.jhtml?redirectURL=https%3A%2F%2Fwww.taobao.com%2F
Cookie: _uab_collina=157836170112456279868722; mt=ci=0_0; t=43449f292592335cd8e157ac6379125d; cookie2=19ea2558ef5a273e6556b3b4d5d9e322; _tb_token_=ee14100576bb7; isg=BNrac6FnUMbjkNxqy3QhAoxLKIA8o3bOKnGm6uRTG204V36RzZ6r9AnlI-PunNZ9; l=dBIyU6RmQTWo1LGQBOfZqsKV3KQT0IRVGkPzcZeXlICPO6fH5-QAWZDDkn8MCn1VnsZWJ35u5_48BP8utyznd9KwNBQ7XPQondLh.; XSRF-TOKEN=a0150c90-ea8b-4bbd-b2bd-301ee4f44f1e; v=0; cna=ZNGaFuaioG4CASRwajKEc6KI
Upgrade-Insecure-Requests: 1
Pragma: no-cache
Cache-Control: no-cache"""
        actDict =req.Req().readHeader(str)
        del actDict["Cookie"]
        expDict={
            "Host": "login.taobao.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Accept-Encoding": "gzip, deflate, br",

            "Content-Type": "application/x-www-form-urlencoded",
            "Content-Length": "2786",
            "Origin": "https://login.taobao.com",
            "Connection": "keep-alive",
            "Referer": "https://login.taobao.com/member/login.jhtml?redirectURL=https%3A%2F%2Fwww.taobao.com%2F",
            
            "Upgrade-Insecure-Requests": "1",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache"
        }
        self.assertEqual(actDict,expDict)

    def testReadHeaderFile(self):
        filePath = utils.absPath("tests/data/header.txt")
        actDict,err =req.Req().readHeaderFile(filePath)
        del actDict["Cookie"]
        self.assertIsNone(err)
        expDict={
            "Host": "login.taobao.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Accept-Encoding": "gzip, deflate, br",

            "Content-Type": "application/x-www-form-urlencoded",
            "Content-Length": "2786",
            "Origin": "https://login.taobao.com",
            "Connection": "keep-alive",
            "Referer": "https://login.taobao.com/member/login.jhtml?redirectURL=https%3A%2F%2Fwww.taobao.com%2F",
            
            "Upgrade-Insecure-Requests": "1",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache"
        }
        self.assertEqual(actDict,expDict)
    
    def testReadUrlParam(self):
        str = """
POST /member/login.jhtml?redirectURL=https%3A%2F%2Fwww.taobao.com%2F HTTP/1.1
Host: login.taobao.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 2786
Origin: https://login.taobao.com
Connection: keep-alive
Referer: https://login.taobao.com/member/login.jhtml?redirectURL=https%3A%2F%2Fwww.taobao.com%2F
Cookie: _uab_collina=157836170112456279868722; mt=ci=0_0; t=43449f292592335cd8e157ac6379125d; cookie2=19ea2558ef5a273e6556b3b4d5d9e322; _tb_token_=ee14100576bb7; isg=BNrac6FnUMbjkNxqy3QhAoxLKIA8o3bOKnGm6uRTG204V36RzZ6r9AnlI-PunNZ9; l=dBIyU6RmQTWo1LGQBOfZqsKV3KQT0IRVGkPzcZeXlICPO6fH5-QAWZDDkn8MCn1VnsZWJ35u5_48BP8utyznd9KwNBQ7XPQondLh.; XSRF-TOKEN=a0150c90-ea8b-4bbd-b2bd-301ee4f44f1e; v=0; cna=ZNGaFuaioG4CASRwajKEc6KI
Upgrade-Insecure-Requests: 1
Pragma: no-cache
Cache-Control: no-cache"""
        actUrl,actParamDto,err =req.Req().readUrlParam(str)
        self.assertIsNone(err)
        expParamDto={
            "redirectURL": "https%3A%2F%2Fwww.taobao.com%2F"
        }
        expUrl="/member/login.jhtml"
        self.assertEqual(actUrl,expUrl)
        self.assertEqual(actParamDto,expParamDto)

    def testReadUrlParamFile(self):
        filePath = utils.absPath("tests/data/header.txt")
        actUrl,actParamDto,err =req.Req().readUrlParamFile(filePath)
        self.assertIsNone(err)
        expParamDto={
            "redirectURL": "https%3A%2F%2Fwww.taobao.com%2F"
        }
        expUrl="/member/login.jhtml"
        self.assertEqual(actUrl,expUrl)
        self.assertEqual(actParamDto,expParamDto)
    def testReadParamPost(self):
        str = """
TPL_username
TPL_password
ncoSig
ncoSessionid
ncoToken=81ba8ac206cdbe98463d8af3ba1cd3ec6ecb82b3
slideCodeShow=false
useMobile=false
lang=zh_CN
loginsite=0
newlogin=0
TPL_redirect_url=https://www.taobao.com/
from=tb
fc=default
style=default
css_style
keyLogin=false
qrLogin=true
newMini=false
newMini2=false
tid
loginType=3
minititle
minipara
pstrong
sign
need_sign
isIgnore
full_redirect
sub_jump
popid
callback
guf
not_duplite_str
need_user_id
poy
gvfdcname=10
gvfdcre=68747470733A2F2F6C6F67696E2E74616F62616F2E636F6D2F6D656D6265722F6C6F676F75742E6A68746D6C3F73706D3D613231626F2E323031372E3735343839343433372E372E356166393131643939314943676426663D746F70266F75743D7472756526726564697265637455524C3D68747470732533412532462532467777772E74616F62616F2E636F6D253246
from_encoding
sub
TPL_password_2
loginASR=1
loginASRSuc=1
allp
oslanguage=zh-CN
sr=1920*1080
osVer
naviVer=firefox|71
osACN=Mozilla
osAV=5.0 (Windows)
osPF=Win32
miserHardInfo
appkey=00000000
nickLoginLink
mobileLoginLink=https://login.taobao.com/member/login.jhtml?redirectURL=https://www.taobao.com/&useMobile=true
showAssistantLink
um_token=T90A4D3B40710C978FF908CBCBA0F4420FCB7483FE19BC35EC493E234B5
ua"""
        actDict =req.Req().readParamPost(str)
        expDict={
            "TPL_username": "", 
            "TPL_password": "", 
            "ncoSig": "", 
            "ncoSessionid": "", 
            "ncoToken": "81ba8ac206cdbe98463d8af3ba1cd3ec6ecb82b3", 
            "slideCodeShow": "false", 
            "useMobile": "false", 
            "lang": "zh_CN", 
            "loginsite": "0", 
            "newlogin": "0", 
            "TPL_redirect_url": "https://www.taobao.com/", 
            "from": "tb", 
            "fc": "default", 
            "style": "default", 
            "css_style": "", 
            "keyLogin": "false", 
            "qrLogin": "true", 
            "newMini": "false", 
            "newMini2": "false", 
            "tid": "", 
            "loginType": "3", 
            "minititle": "", 
            "minipara": "", 
            "pstrong": "", 
            "sign": "", 
            "need_sign": "", 
            "isIgnore": "", 
            "full_redirect": "", 
            "sub_jump": "", 
            "popid": "", 
            "callback": "", 
            "guf": "", 
            "not_duplite_str": "", 
            "need_user_id": "", 
            "poy": "", 
            "gvfdcname": "10", 
            "gvfdcre": "68747470733A2F2F6C6F67696E2E74616F62616F2E636F6D2F6D656D6265722F6C6F676F75742E6A68746D6C3F73706D3D613231626F2E323031372E3735343839343433372E372E356166393131643939314943676426663D746F70266F75743D7472756526726564697265637455524C3D68747470732533412532462532467777772E74616F62616F2E636F6D253246", 
            "from_encoding": "", 
            "sub": "", 
            "TPL_password_2": "", 
            "loginASR": "1", 
            "loginASRSuc": "1", 
            "allp": "", 
            "oslanguage": "zh-CN", 
            "sr": "1920*1080", 
            "osVer": "", 
            "naviVer": "firefox|71", 
            "osACN": "Mozilla", 
            "osAV": "5.0 (Windows)", 
            "osPF": "Win32", 
            "miserHardInfo": "", 
            "appkey": "00000000", 
            "nickLoginLink": "", 
            "mobileLoginLink": "https://login.taobao.com/member/login.jhtml?redirectURL=https://www.taobao.com/&useMobile=true", 
            "showAssistantLink": "", 
            "um_token": "T90A4D3B40710C978FF908CBCBA0F4420FCB7483FE19BC35EC493E234B5", 
            "ua": ""
        }
        self.assertEqual(actDict,expDict)
    def testReadParamPostFile(self):
        filePath = utils.absPath("tests/data/param.txt")
        actDict =req.Req().readParamPostFile(filePath)
        expDict={
            "TPL_username": "", 
            "TPL_password": "", 
            "ncoSig": "", 
            "ncoSessionid": "", 
            "ncoToken": "81ba8ac206cdbe98463d8af3ba1cd3ec6ecb82b3", 
            "slideCodeShow": "false", 
            "useMobile": "false", 
            "lang": "zh_CN", 
            "loginsite": "0", 
            "newlogin": "0", 
            "TPL_redirect_url": "https://www.taobao.com/", 
            "from": "tb", 
            "fc": "default", 
            "style": "default", 
            "css_style": "", 
            "keyLogin": "false", 
            "qrLogin": "true", 
            "newMini": "false", 
            "newMini2": "false", 
            "tid": "", 
            "loginType": "3", 
            "minititle": "", 
            "minipara": "", 
            "pstrong": "", 
            "sign": "", 
            "need_sign": "", 
            "isIgnore": "", 
            "full_redirect": "", 
            "sub_jump": "", 
            "popid": "", 
            "callback": "", 
            "guf": "", 
            "not_duplite_str": "", 
            "need_user_id": "", 
            "poy": "", 
            "gvfdcname": "10", 
            "gvfdcre": "68747470733A2F2F6C6F67696E2E74616F62616F2E636F6D2F6D656D6265722F6C6F676F75742E6A68746D6C3F73706D3D613231626F2E323031372E3735343839343433372E372E356166393131643939314943676426663D746F70266F75743D7472756526726564697265637455524C3D68747470732533412532462532467777772E74616F62616F2E636F6D253246", 
            "from_encoding": "", 
            "sub": "", 
            "TPL_password_2": "", 
            "loginASR": "1", 
            "loginASRSuc": "1", 
            "allp": "", 
            "oslanguage": "zh-CN", 
            "sr": "1920*1080", 
            "osVer": "", 
            "naviVer": "firefox|71", 
            "osACN": "Mozilla", 
            "osAV": "5.0 (Windows)", 
            "osPF": "Win32", 
            "miserHardInfo": "", 
            "appkey": "00000000", 
            "nickLoginLink": "", 
            "mobileLoginLink": "https://login.taobao.com/member/login.jhtml?redirectURL=https://www.taobao.com/&useMobile=true", 
            "showAssistantLink": "", 
            "um_token": "T90A4D3B40710C978FF908CBCBA0F4420FCB7483FE19BC35EC493E234B5", 
            "ua": ""
        }
        self.assertEqual(actDict,expDict)
    # # 需要先网页打开，并且按F12 定位到XHR
    # def testWrite(self):
    #     subPath = "test_data/davebella"
    #     url ="https://davebella.world.tmall.com/category.htm"
    #     err =req.Req(subPath).write(url,name="asynSearch.htm")
    #     self.assertIsNone(err)
