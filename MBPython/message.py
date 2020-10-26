# -*- coding:utf-8 -*-
from ctypes import (
    windll,
    c_long,
    c_ulong,
    c_ushort
)
from .wkeStruct import mPos

user32 = windll.user32
class Message():
    def __init__(self,miniblink):

        self.mb=miniblink
    def wkeFireMouseEvent(self,webview,msg,x,y,flags=0):

        return self.mb.wkeFireMouseEvent(webview,msg,x,y,flags)
    def wkeFireKeyDownEvent(self,webview,virtualKeyCode,flags=0):
    
        return self.mb.wkeFireKeyDownEvent(webview,virtualKeyCode,flags,False)
    def wkeFireKeyUpEvent(self,webview,virtualKeyCode,flags=0):

        return self.mb.wkeFireKeyUpEvent(webview,virtualKeyCode,flags,False)
    def wkeFireKeyPressEvent(self,webview,virtualKeyCode,flags):
        return self.mb.wkeFireKeyPressEvent(webview,virtualKeyCode,flags,False)
    def wkeFireWindowsMessage(self,webview,hwnd,msg,wParam,lParam,result):

        return self.mb.wkeFireWindowsMessage(webview,hwnd,msg,wParam,lParam,result)
    
    @staticmethod
    def fire_mouse_msg(hwnd,msg,x,y):
        pos=c_long(c_ushort(x).value | c_ulong(c_ushort(y).value).value << 16).value
        return user32.PostMessageW(hwnd,msg,0,pos)
    
    @staticmethod
    def fire_keyboard_msg(hwnd,virtualKeyCode,msg):
        return user32.SendMessageW(hwnd,msg,virtualKeyCode,0)

    @staticmethod
    def get_mouse_pos():
        p=mPos()
        user32.GetCursorPos(byref(p))

        return p
