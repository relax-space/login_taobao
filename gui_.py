

import error
from pyautogui import *
import clipboard
import dto

class Gui:
    def __init__(self):
        self.first_point =dto.LocationDto(20,20)
        self.tools_network= dto.LocationDto(327,76)
        self.tools_network_html= dto.LocationDto(108,137) # 
        self.tools_network_xhr= dto.LocationDto(210,137) # 
        self.tools_network_content = dto.LocationDto(300, 190)
    
    def reqUrl(self,url):
        try:
            click(x=self.first_point.x, y=self.first_point.y)
            keyDown('alt')
            press('d')
            keyUp('alt')
            time.sleep(2)
            clipboard.copy(url)
            hotkey('ctrl', 'v', interval=0.15)
            press('del')
            time.sleep(0.5)
            press('enter')
            time.sleep(8)

            press('f12')
            time.sleep(3)
            click(x=self.tools_network.x, y=self.tools_network.y)
            time.sleep(0.5)
            return None
        except Exception as inst:
            return error.abort(inst)
    
    def copyHTMLPostLoop(self,name):
        click(x=self.tools_network_html.x, y=self.tools_network_html.y)
        header,param =None,None
        for i  in range(0,20):
            increment = i*30
            contents,err = self._copyContent(increment=increment)
            contents = contents.strip()
            if err != None:
                return None,error.invalid("gui header")
            if 'Cookie' not in contents:
                continue
            elif contents.startswith("POST") == False:
                continue
            elif name not in contents:
                continue
            header=contents
            param,err = self._copyContent(command="D",increment=increment)
            if err != None:
                return None,error.invalid("gui param")
            break
        if header ==None or param == None:
            return None,error.invalid("gui header or param")
        return header,param,None
    
    def copyXHRLoop(self,name):
        click(x=self.tools_network_xhr.x, y=self.tools_network_xhr.y)
        reqStr =None
        for i  in range(0,2):
            increment = i*30
            contents,err = self._copyContent(increment=increment)
            if err != None:
                return None,error.invalid("gui reqPath")
            if 'Cookie' not in contents:
                continue
            elif name not in contents:
                continue
            reqStr=contents
            break
        if reqStr ==None:
            return None,error.invalid("gui reqPath")
        return reqStr,None
    
    def _copyContent(self,command='q', increment=0):
        try:
            click(x=self.tools_network_content.x, y=self.tools_network_content.y+increment, button='right')
            time.sleep(1)
            press('c')
            time.sleep(0.5)
            press(command)
            time.sleep(0.5)
            press('enter')
            contents = clipboard.paste()
            return contents,None
        except Exception as inst:
            return None,error.abort(inst)