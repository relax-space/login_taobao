from typing import List

class Generic:
    @classmethod
    def fromDict(cls, dict):
        obj = cls()
        obj.__dict__.update(dict)
        return obj

class LocationDto:
    x=0
    y=0
    def __init__(self,x,y):
        self.x = x
        self.y = y


class ReqDto:
    def __init__(self,url="",headers={},params={},proxies={}):
        self.url = url
        self.headers=headers
        self.params=params
        self.proxies=proxies
    def __eq__(self,other):
        return self.url == other.url \
        and self.headers == other.headers \
        and self.params == other.params