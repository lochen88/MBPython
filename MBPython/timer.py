# -*- coding:utf-8 -*-
from ctypes import (
    c_void_p,
    windll,
    WINFUNCTYPE
)
from ctypes.wintypes import (
    DWORD,
    HWND,
    UINT
)
from .method import method
user32=windll.user32


class Timer:
    def __init__(self):
        self.timer_func_dict={}
    def setTimer(self,hwnd,nid,dwTime,is_timer_one=True):
        self.is_timer_one=is_timer_one
        return user32.SetTimer (hwnd,nid, dwTime, self._timerCallBack)
    @method(WINFUNCTYPE(c_void_p,HWND,c_void_p,UINT,DWORD))
    def _timerCallBack(self,hwnd,msg,nid,dwTime):
        if hasattr(self,'timerCallBack'):
            if self.is_timer_one:
                self.timerCallBack(hwnd=hwnd,msg=msg,nid=nid,dwTime=dwTime)
                user32.KillTimer(hwnd,nid)
                return 0
            return self.timerCallBack(hwnd=hwnd,msg=msg,nid=nid,dwTime=dwTime)
