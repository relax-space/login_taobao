import os

def write(prePath,fileName, contents,mode="w",encoding='utf-8'):
    try:
        ensureDir(prePath)
        path = os.path.join(prePath,fileName).replace("\\","/")
        with open(path, mode, encoding=encoding) as fp:
            fp.write(contents)
        return None
    except Exception as inst:
        return str(inst)

def read(path,mode="rt",encoding='utf-8'):
    try:
        with open(path, mode, encoding=encoding) as fp:
            contents=fp.read()
        return contents,None
    except Exception as inst:
        return None,str(inst)

def ensureDir(dirs):
    if not os.path.exists(dirs):
        os.makedirs(dirs)

def fileList(directory,suffix=None):
    list = []
    if os.path.exists(directory) == False:
        return None,error.invalid("directory %s" % (directory))
    files = os.listdir(directory)
    for file in files:
        m = os.path.join(directory,file)
        m = m.replace("\\","/")
        if os.path.isfile(m) == True:
            if suffix == None:
                list.append(m)
            elif suffix != None and m.endswith(suffix):
                list.append(m)
    return list,None
        
