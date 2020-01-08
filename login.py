import re
import os
import json

import requests
import req
import utils

"""
获取详细教程、获取代码帮助、提出意见建议
关注微信公众号「裸睡的猪」与猪哥联系

@Author  :   猪哥,
@Version :   2.0"
"""

s = requests.Session()
# cookies序列化文件
COOKIES_FILE_PATH = 'taobao_login_cookies.txt'


class UsernameLogin:

    def __init__(self, username, ua, TPL_password2):
        """
        账号登录对象
        :param username: 用户名
        :param ua: 淘宝的ua参数
        :param TPL_password2: 加密后的密码
        """
        # 检测是否需要验证码的URL
        self.user_check_url = 'https://login.taobao.com/member/request_nick_check.do?_input_charset=utf-8'
        # 验证淘宝用户名密码URL
        self.verify_password_url = "https://login.taobao.com/member/login.jhtml"
        # 访问st码URL
        self.vst_url = 'https://login.taobao.com/member/vst.htm?st={}'
        # 淘宝个人 主页
        self.my_taobao_url = 'http://i.taobao.com/my_taobao.htm'

        # 淘宝用户名
        self.username = username
        # 淘宝关键参数，包含用户浏览器等一些信息，很多地方会使用，从浏览器或抓包工具中复制，可重复使用
        self.ua = ua
        # 加密后的密码，从浏览器或抓包工具中复制，可重复使用
        self.TPL_password2 = TPL_password2

        # 请求超时时间
        self.timeout = 3

    def _user_check(self):
        """
        检测账号是否需要验证码
        :return:
        """
        data = {
            'username': self.username,
            'ua': self.ua
        }
        try:
            response = s.post(self.user_check_url, data=data, timeout=self.timeout)
            response.raise_for_status()
        except Exception as e:
            print('检测是否需要验证码请求失败，原因：')
            return None,str(e)
        needcode = response.json()['needcode']
        print('是否需要滑块验证：{}'.format(needcode))
        return needcode,None

    def _verify_password(self):
        """
        验证用户名密码，并获取st码申请URL
        :return: 验证成功返回st码申请地址
        """
        # verify_password_headers = {
        #     'Connection': 'keep-alive',
        #     'Cache-Control': 'no-cache',
        #     'Origin': 'https://login.taobao.com',
        #     'Upgrade-Insecure-Requests': '1',
        #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0',
        #     'Content-Type': 'application/x-www-form-urlencoded',
        #     'Referer': 'https://login.taobao.com/member/login.jhtml?redirectURL=https%3A%2F%2Fwww.taobao.com%2F',
        # }
        # 
        # verify_password_data = {
        #     'TPL_username': self.username,
        #     'ncoToken': '81ba2ac20acdbe7846318af36a1cdaec6e5b82b8',
        #     'slideCodeShow': 'false',
        #     'useMobile': 'false',
        #     'lang': 'zh_CN',
        #     'loginsite': 0,
        #     'newlogin': 0,
        #     'TPL_redirect_url': 'https://www.taobao.com/',
        #     'from': 'tb',
        #     'fc': 'default',
        #     'style': 'default',
        #     'keyLogin': 'false',
        #     'qrLogin': 'true',
        #     'newMini': 'false',
        #     'newMini2': 'false',
        #     'loginType': '3',
        #     'gvfdcname': '10',
        #     'gvfdcre': '68747470733A2F2F6C6F67696E2E74616F62616F2E636F6D2F6D656D6265722F6C6F676F75742E6A68746D6C3F73706D3D613231626F2E323031372E3735343839343433372E372E356166393131643964555731426A26663D746F70266F75743D7472756526726564697265637455524C3D68747470732533412532462532467777772E74616F62616F2E636F6D253246',
        #     'TPL_password_2': self.TPL_password2,
        #     'loginASR': '1',
        #     'loginASRSuc': '1',
        #     'oslanguage': 'zh-CN',
        #     'sr': '1920*1080',
        #     'naviVer': 'firefox|71',
        #     'osACN': 'Mozilla',
        #     'osAV': '5.0 (Windows)',
        #     'osPF': 'Win32',
        #     'appkey': '00000000',
        #     'mobileLoginLink': 'https://login.taobao.com/member/login.jhtml?redirectURL=https://www.taobao.com/&useMobile=true',
        #     'showAssistantLink': '',
        #     'um_token': 'T0EC0F6614ED31DC032C7F3B6921A1A3A3E94A3DBBBECBB717941D00056',
        #     'ua': self.ua
        # }
        headerPath=os.path.join(utils.DATA_PATH,utils.DATA_PATH_HEADER)
        verify_password_headers,err=req.Req().readHeaderFile(headerPath)
        if err != None:
            return None,err
        del verify_password_headers["Cookie"]
        '''登录toabao.com提交的数据，如果登录失败，可以从浏览器复制你的form data'''
        paramPath=os.path.join(utils.DATA_PATH,utils.DATA_PATH_PARAM)
        verify_password_data=req.Req().readParamPostFile(paramPath)
        verify_password_data["TPL_username"]=self.username
        verify_password_data["TPL_password_2"]=self.TPL_password2
        verify_password_data["ua"]=self.ua
        try:
            response = s.post(self.verify_password_url, headers=verify_password_headers, data=verify_password_data,
                              timeout=self.timeout)
            response.raise_for_status()
            # 从返回的页面中提取申请st码地址
        except Exception as e:
            print('验证用户名和密码请求失败，原因：%s' % (e))
            return None, str(e)
        # 提取申请st码url
        apply_st_url_match = re.search(r'<script src="(.*?)"></script>', response.text)
        # 存在则返回
        if apply_st_url_match:
            print('验证用户名密码成功，st码申请地址：{}'.format(apply_st_url_match.group(1)))
            return apply_st_url_match.group(1),None
        else:
            return None, '用户名密码验证失败！response：{}'.format(response.text)

    def _apply_st(self):
        """
        申请st码
        :return: st码
        """
        apply_st_url,err = self._verify_password()
        if err != None:
            return None,err
        try:
            response = s.get(apply_st_url)
            response.raise_for_status()
        except Exception as e:
            print('申请st码请求失败，原因：')
            return None, str(e)
        st_match = re.search(r'"data":{"st":"(.*?)"}', response.text)
        if st_match:
            print('获取st码成功，st码：{}'.format(st_match.group(1)))
            return st_match.group(1),None
        else:
            return None,'获取st码失败！response：{}'.format(response.text)

    def login(self):
        """
        使用st码登录
        :return:
        """
        # 加载cookies文件
        if self._load_cookies():
            return None
        # 判断是否需要滑块验证
        need,err = self._user_check()
        if err != None:
            return err
        if need == True:
            return "需要滑块，请明天再重试"
        st,err = self._apply_st()
        if err != None:
            return err
        headers = {
            'Host': 'login.taobao.com',
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }
        try:
            response = s.get(self.vst_url.format(st), headers=headers)
            response.raise_for_status()
        except Exception as e:
            print('st码登录请求，原因：')
            return str(e)
        # 登录成功，提取跳转淘宝用户主页url
        my_taobao_match = re.search(r'top.location.href = "(.*?)"', response.text)
        if my_taobao_match:
            print('登录淘宝成功，跳转链接：{}'.format(my_taobao_match.group(1)))
            err = self._serialization_cookies()
            if err != None:
                return err
            return None
        else:
            return '登录失败！response：{}'.format(response.text)

    def _load_cookies(self):
        # 1、判断cookies序列化文件是否存在
        if not os.path.exists(COOKIES_FILE_PATH):
            return False
        # 2、加载cookies
        s.cookies,err = self._deserialization_cookies()
        if err != None:
            return False
        # 3、判断cookies是否过期
        _,err=self.get_taobao_nick_name()
        if err != None:
            os.remove(COOKIES_FILE_PATH)
            print('cookies过期，删除cookies文件！')
            return False
        print('加载淘宝登录cookies成功!!!')
        return True

    def _serialization_cookies(self):
        """
        序列化cookies
        :return:
        """
        try:
            cookies_dict = requests.utils.dict_from_cookiejar(s.cookies)
            with open(COOKIES_FILE_PATH, 'w+', encoding='utf-8') as file:
                json.dump(cookies_dict, file)
                print('保存cookies文件成功！')
                return None
        except Exception as e:
            return str(e)

    def _deserialization_cookies(self):
        """
        反序列化cookies
        :return:
        """
        try:
            with open(COOKIES_FILE_PATH, 'r+', encoding='utf-8') as file:
                cookies_dict = json.load(file)
                cookies = requests.utils.cookiejar_from_dict(cookies_dict)
                return cookies,None
        except Exception as e:
            return None, str(e)

    def get_taobao_nick_name(self):
        """
        获取淘宝昵称
        :return: 淘宝昵称
        """
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }
        try:
            response = s.get(self.my_taobao_url, headers=headers)
            response.raise_for_status()
        except Exception as e:
            print('获取淘宝主页请求失败！原因：')
            return None, str(e)
        # 提取淘宝昵称
        nick_name_match = re.search(r'<input id="mtb-nickname" type="hidden" value="(.*?)"/>', response.text)
        if nick_name_match:
            print('登录淘宝成功，你的用户名是：{}'.format(nick_name_match.group(1)))
            return nick_name_match.group(1),None
        else:
            return None,'获取淘宝昵称失败！response：{}'.format(response.text)
