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
        GET /i/asynSearch.htm?_ksTS=1575667351284_693&callback=jsonp694&mid=w-14896417856-0&wid=14896417856&path=/category.htm HTTP/1.1

Host: davebella.world.tmall.com

User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0

Accept: text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01

Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2

Accept-Encoding: gzip, deflate, br

Referer: https://davebella.world.tmall.com/category.htm

X-Requested-With: XMLHttpRequest

Connection: keep-alive

Cookie: cna=HkxQFdkfLWgCAS04mzUPF9vr; isg=BNzcapCY7QV0fJla2e3ZODixrvpO_ahU-AfgILbd_EeqAXyL3WWmD2JwZalckrjX; l=dBrlw9eIq8sAj4aGBOCwcuIRMGQ97IOYYuPRw2ZBi_5aX6L68CbOkhoKBFp6csWfT8Ye4_41Zzp9-etowXGR1d_fGzmxyxDc.; hng=CN%7Czh-CN%7CCNY; lid=xiaoxm_001; pnm_cku822=; t=0c7f408b84b590fbc69989916f491575; uc3=lg2=VFC%2FuZ9ayeYq2g%3D%3D&vt3=F8dByus%2B2Gg4F6q%2FuOM%3D&nk2=G4mgLCtQ61Ct4Q%3D%3D&id2=VAYhfVsUHpas; tracknick=xiaoxm_001; uc4=nk4=0%40GToWF7xjYYbAUv7x%2Fo2bwumbKiqP&id4=0%40Vh%2BzeYCIjUuF6BHgRPA5dDOIqLo%3D; lgc=xiaoxm_001; _tb_token_=e1dfeb3a306e; cookie2=11fe8bce6afc6cc4de9118c4ebecad78; _l_g_=Ug%3D%3D; _nk_=xiaoxm_001; dnk=xiaoxm_001; dnk=xiaoxm_001; uc1=cookie16=UtASsssmPlP%2Ff1IHDsDaPRu%2BPw%3D%3D&cookie21=VFC%2FuZ9ainBZ&cookie15=VFC%2FuZ9ayeYq2g%3D%3D&existShop=false&pas=0&cookie14=UoTbmE0pYW6duw%3D%3D&tag=8&lng=zh_CN; _l_g_=Ug%3D%3D; unb=779592136; cookie1=BxoBh8tJNYJ8aIsSu%2Bo62b6SDl1SOXU%2Fivzz8KLg3r0%3D; login=true; cookie17=VAYhfVsUHpas; _nk_=xiaoxm_001; sg=169; csg=097330ee"""
        actDto =req.Req().readHeader(str)
        expDto={
            "Host": "davebella.world.tmall.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0",
            "Accept": "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": "https://davebella.world.tmall.com/category.htm",
            "X-Requested-With": "XMLHttpRequest",
            "Connection": "keep-alive",
            "Cookie": "cna=HkxQFdkfLWgCAS04mzUPF9vr; isg=BNzcapCY7QV0fJla2e3ZODixrvpO_ahU-AfgILbd_EeqAXyL3WWmD2JwZalckrjX; l=dBrlw9eIq8sAj4aGBOCwcuIRMGQ97IOYYuPRw2ZBi_5aX6L68CbOkhoKBFp6csWfT8Ye4_41Zzp9-etowXGR1d_fGzmxyxDc.; hng=CN%7Czh-CN%7CCNY; lid=xiaoxm_001; pnm_cku822=; t=0c7f408b84b590fbc69989916f491575; uc3=lg2=VFC%2FuZ9ayeYq2g%3D%3D&vt3=F8dByus%2B2Gg4F6q%2FuOM%3D&nk2=G4mgLCtQ61Ct4Q%3D%3D&id2=VAYhfVsUHpas; tracknick=xiaoxm_001; uc4=nk4=0%40GToWF7xjYYbAUv7x%2Fo2bwumbKiqP&id4=0%40Vh%2BzeYCIjUuF6BHgRPA5dDOIqLo%3D; lgc=xiaoxm_001; _tb_token_=e1dfeb3a306e; cookie2=11fe8bce6afc6cc4de9118c4ebecad78; _l_g_=Ug%3D%3D; _nk_=xiaoxm_001; dnk=xiaoxm_001; dnk=xiaoxm_001; uc1=cookie16=UtASsssmPlP%2Ff1IHDsDaPRu%2BPw%3D%3D&cookie21=VFC%2FuZ9ainBZ&cookie15=VFC%2FuZ9ayeYq2g%3D%3D&existShop=false&pas=0&cookie14=UoTbmE0pYW6duw%3D%3D&tag=8&lng=zh_CN; _l_g_=Ug%3D%3D; unb=779592136; cookie1=BxoBh8tJNYJ8aIsSu%2Bo62b6SDl1SOXU%2Fivzz8KLg3r0%3D; login=true; cookie17=VAYhfVsUHpas; _nk_=xiaoxm_001; sg=169; csg=097330ee"
        }
        self.assertEqual(actDto,expDto)

    def testReadHeaderFile(self):
        filePath = utils.absPath("tests/data/header.txt")
        actDto,err =req.Req().readHeaderFile(filePath)
        self.assertIsNone(err)
        expDto={
            "Host": "davebella.world.tmall.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0",
            "Accept": "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": "https://davebella.world.tmall.com/category.htm",
            "X-Requested-With": "XMLHttpRequest",
            "Connection": "keep-alive",
            "Cookie": "cna=HkxQFdkfLWgCAS04mzUPF9vr; isg=BNzcapCY7QV0fJla2e3ZODixrvpO_ahU-AfgILbd_EeqAXyL3WWmD2JwZalckrjX; l=dBrlw9eIq8sAj4aGBOCwcuIRMGQ97IOYYuPRw2ZBi_5aX6L68CbOkhoKBFp6csWfT8Ye4_41Zzp9-etowXGR1d_fGzmxyxDc.; hng=CN%7Czh-CN%7CCNY; lid=xiaoxm_001; pnm_cku822=; t=0c7f408b84b590fbc69989916f491575; uc3=lg2=VFC%2FuZ9ayeYq2g%3D%3D&vt3=F8dByus%2B2Gg4F6q%2FuOM%3D&nk2=G4mgLCtQ61Ct4Q%3D%3D&id2=VAYhfVsUHpas; tracknick=xiaoxm_001; uc4=nk4=0%40GToWF7xjYYbAUv7x%2Fo2bwumbKiqP&id4=0%40Vh%2BzeYCIjUuF6BHgRPA5dDOIqLo%3D; lgc=xiaoxm_001; _tb_token_=e1dfeb3a306e; cookie2=11fe8bce6afc6cc4de9118c4ebecad78; _l_g_=Ug%3D%3D; _nk_=xiaoxm_001; dnk=xiaoxm_001; dnk=xiaoxm_001; uc1=cookie16=UtASsssmPlP%2Ff1IHDsDaPRu%2BPw%3D%3D&cookie21=VFC%2FuZ9ainBZ&cookie15=VFC%2FuZ9ayeYq2g%3D%3D&existShop=false&pas=0&cookie14=UoTbmE0pYW6duw%3D%3D&tag=8&lng=zh_CN; _l_g_=Ug%3D%3D; unb=779592136; cookie1=BxoBh8tJNYJ8aIsSu%2Bo62b6SDl1SOXU%2Fivzz8KLg3r0%3D; login=true; cookie17=VAYhfVsUHpas; _nk_=xiaoxm_001; sg=169; csg=097330ee"
        }
        self.assertEqual(actDto,expDto)
    
    def testReadUrlParam(self):
        str = """
        GET /i/asynSearch.htm?_ksTS=1575667351284_693&callback=jsonp694&mid=w-14896417856-0&wid=14896417856&path=/category.htm HTTP/1.1

Host: davebella.world.tmall.com

User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0

Accept: text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01

Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2

Accept-Encoding: gzip, deflate, br

Referer: https://davebella.world.tmall.com/category.htm

X-Requested-With: XMLHttpRequest

Connection: keep-alive

Cookie: cna=HkxQFdkfLWgCAS04mzUPF9vr; isg=BNzcapCY7QV0fJla2e3ZODixrvpO_ahU-AfgILbd_EeqAXyL3WWmD2JwZalckrjX; l=dBrlw9eIq8sAj4aGBOCwcuIRMGQ97IOYYuPRw2ZBi_5aX6L68CbOkhoKBFp6csWfT8Ye4_41Zzp9-etowXGR1d_fGzmxyxDc.; hng=CN%7Czh-CN%7CCNY; lid=xiaoxm_001; pnm_cku822=; t=0c7f408b84b590fbc69989916f491575; uc3=lg2=VFC%2FuZ9ayeYq2g%3D%3D&vt3=F8dByus%2B2Gg4F6q%2FuOM%3D&nk2=G4mgLCtQ61Ct4Q%3D%3D&id2=VAYhfVsUHpas; tracknick=xiaoxm_001; uc4=nk4=0%40GToWF7xjYYbAUv7x%2Fo2bwumbKiqP&id4=0%40Vh%2BzeYCIjUuF6BHgRPA5dDOIqLo%3D; lgc=xiaoxm_001; _tb_token_=e1dfeb3a306e; cookie2=11fe8bce6afc6cc4de9118c4ebecad78; _l_g_=Ug%3D%3D; _nk_=xiaoxm_001; dnk=xiaoxm_001; dnk=xiaoxm_001; uc1=cookie16=UtASsssmPlP%2Ff1IHDsDaPRu%2BPw%3D%3D&cookie21=VFC%2FuZ9ainBZ&cookie15=VFC%2FuZ9ayeYq2g%3D%3D&existShop=false&pas=0&cookie14=UoTbmE0pYW6duw%3D%3D&tag=8&lng=zh_CN; _l_g_=Ug%3D%3D; unb=779592136; cookie1=BxoBh8tJNYJ8aIsSu%2Bo62b6SDl1SOXU%2Fivzz8KLg3r0%3D; login=true; cookie17=VAYhfVsUHpas; _nk_=xiaoxm_001; sg=169; csg=097330ee"""
        actUrl,actParamDto,err =req.Req().readUrlParam(str)
        self.assertIsNone(err)
        expParamDto={
            "_ksTS": "1575667351284_693",
            "callback": "jsonp694",
            "mid": "w-14896417856-0",
            "wid": "14896417856",
            "path": "/category.htm"
        }
        expUrl="/i/asynSearch.htm"
        self.assertEqual(actUrl,expUrl)
        self.assertEqual(actParamDto,expParamDto)

    def testReadUrlParamFile(self):
        filePath = utils.absPath("tests/data/header.txt")
        actUrl,actParamDto,err =req.Req().readUrlParamFile(filePath)
        self.assertIsNone(err)
        expParamDto={
            "_ksTS": "1575667351284_693",
            "callback": "jsonp694",
            "mid": "w-14896417856-0",
            "wid": "14896417856",
            "path": "/category.htm"
        }
        expUrl="/i/asynSearch.htm"
        self.assertEqual(actUrl,expUrl)
        self.assertEqual(actParamDto,expParamDto)
    # # 需要先网页打开，并且按F12 定位到XHR
    # def testWrite(self):
    #     subPath = "test_data/davebella"
    #     url ="https://davebella.world.tmall.com/category.htm"
    #     err =req.Req(subPath).write(url,name="asynSearch.htm")
    #     self.assertIsNone(err)
