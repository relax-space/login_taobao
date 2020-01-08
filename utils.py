import re
import os

DATA_PATH = "data"
DATA_PATH_HEADER = "header.txt"
DATA_PATH_PARAM = "param.txt"


def strToDict(contents,sep1="\n",sep2="="):
    dict={}
    lines = contents.strip().split(sep1)
    for line in lines:
        ln=line.strip()
        if len(ln)==0:
            continue
        index = ln.find(sep2)
        if index == -1:
            dict[ln] = ""
            continue
        factor1=ln[:index] 
        factor2=ln[index+1:] 
        dict[factor1] = factor2
    return dict
    
def parseSep(content,sep=": "):
    index = content.find(sep)
    if index == -1:
        return None,None,"no found sep:': '"
    k,v = content[0:index],content[index+1:]
    if k==None or k == None:
        return None,None,err
    return k.strip(),v.strip(),None

def regex(contents,sep1,sep2="\n"):
    contents=contents+sep2
    patten = r"%s(.+?)%s|$" % (sep1,sep2)
    result = re.findall(patten, contents)[0]
    return result

def regexSub(contents,replace,sep1,sep2="\n"):
    contents=contents+sep2
    patten = r"%s(.+?)%s" % (sep1,sep2)
    result = re.sub(patten,replace, contents)
    return result.strip()


def regexEn(contents):
    pat = re.compile('[a-zA-Z]+')
    words = pat.findall(contents)
    return words

def regexChina(contents):
    pat = re.compile(r'[\u4e00-\u9fa5]+')
    words = pat.findall(contents)
    return words


def regexNum(contents):
    pat = re.compile('[0-9]+|$')
    words = pat.findall(contents)
    return words

def formatHtml(reqHtml,startStr):
        if startStr ==None:
            return None,error.invalid("html")
        if len(reqHtml) < len(startStr)+4:
            return None,error.invalid("html")
        html = reqHtml[len(startStr)+2:-2]
        html = html.replace(r'\"',r'"')
        return html,None
def printLevel(content,level=2):
    if level == 2:
        print("  %s" % (content))
    else:
        print(content)


def bfKongStr(bf):
    if bf == None:
        return ""
    return bf.get_text().strip()

def bfKongInt(bf):
    try:
        if bf == None:
            return 0
        return int(bf.get_text().strip())
    except Exception as inst:
        return 0
def bfKongFloat(bf):
    try:
        if bf == None:
            return 0
        return float(bf.get_text().strip())
    except Exception as inst:
        return 0
    

def absPath(file):
    # 获取当前文件路径
    current_path = os.path.abspath(__file__)
    # 获取当前文件的父目录
    father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")
    # file文件路径,获取当前目录的父目录的父目录与file拼接
    config_file_path=os.path.join(os.path.abspath(os.path.dirname(current_path)),file)
    path = config_file_path.replace("\\","/")
    return path 


