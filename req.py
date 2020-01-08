from pyautogui import *
import utils
import file_
import dto
import error


class Req:

    def __init__(self, ):
        pass

    def readParamPostFile(self,filePath):
        contents,err=file_.read(filePath)
        if err != None:
            return err
        return self.readParamPost(contents)

    def readParamPost(self,contents):
        return utils.strToDict(contents)

    def readHeaderFile(self,filePath):
        contents,err=file_.read(filePath)
        if err != None:
            return None,err
        return self.readHeader(contents),None

    def readHeader(self,contents):
        lines=contents.split("\n")
        header ={}
        for line in lines:
            ls = line.strip()
            if len(ls) ==0: # empty line
                continue
            k,v,err = utils.parseSep(content=ls)
            if err !=None:
                continue
            header[k] = v
        return header

    def readUrlParamFile(self,filePath):
        contents,err=file_.read(filePath)
        if err != None:
            return None,None,err
        return self.readUrlParam(contents)

    def readUrlParam(self,contents):
        lines=contents.split("\n")
        url,param=None,None
        for line in lines:
            ls = line.strip()
            if len(ls) ==0: # empty line
                continue
            if self._hasPathParam(ls):
                url,param,err=self._readPathParam(ls)
                if err != None:
                    return None,err
        return url,param,None

    def _readPathParam(self,content):
        if self._hasPathParam(content) == False:
            return None,None,error.invalid("url params")
        list=content.split(" ")
        path = list[1]
        sep = path.find("?")
        if sep == -1:
            return path,{},None
        url = path[:sep]
        paramstr = path[sep+1:]
        params=utils.strToDict(paramstr,"&","=")
        return url,params,None
    
    def _hasPathParam(self,content):
        for method in ["GET","POST","PUT","DELELT","PATCH"]:
            if content.startswith(method):
                return True
        return False
 
    

    

    
