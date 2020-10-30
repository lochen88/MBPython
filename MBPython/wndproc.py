# -*- coding:utf-8 -*-
from .winConst import WinConst
from .wkeStruct import COPYDATASTRUCT
from ctypes import (cast,c_char_p,py_object,sizeof,byref,string_at,create_string_buffer,POINTER)
import win32gui
import win32api
import json

PCOPYDATASTRUCT = POINTER(COPYDATASTRUCT)
class WndProcHook:
    def __init__(self,hwnd,webview=None):
        self.webview=webview
        self.hwnd=hwnd
        self.msg_func_dict = {}
    def hook_WndProc(self):
        self.oldWndProc = win32gui.SetWindowLong(self.hwnd, WinConst.GWL_WNDPROC, self._onWndProcCallback)
    def unhook_WndProc(self):
        win32api.SetWindowLong(self.hwnd, WinConst.GWL_WNDPROC, self.oldWndProc)
    def add_msg_func(self,webview,hwnd,msg,msg_func):
        self.msg_func_dict[msg] = msg_func
    def _onWndProcCallback(self, hwnd, msg, wParam, lParam):

        if msg in self.msg_func_dict:
            argcount=self.msg_func_dict[msg].__code__.co_argcount
            ret=None
            if argcount==5:
                arg_vals=self.msg_func_dict[msg].__code__.co_varnames
                if arg_vals[0]=='self':
                    ret=self.msg_func_dict[msg](self.webview,hwnd,wParam, lParam)
            elif argcount==4:
                ret=self.msg_func_dict[msg](self.webview,hwnd,wParam, lParam)
            elif argcount==3:
                ret=self.msg_func_dict[msg](hwnd,wParam, lParam)
            elif argcount==2:
                ret=self.msg_func_dict[msg](wParam, lParam)
            if ret!=None:
                return ret
        if hasattr(self,'onWndProcCallback'):
            ret=self.onWndProcCallback(hwnd=hwnd, msg=msg, wParam=wParam, lParam=lParam)
            if ret!=None:
                return ret
        if msg == WinConst.WM_DESTROY: 
            self.unhook_WndProc()
        return win32gui.CallWindowProc(self.oldWndProc, hwnd, msg, wParam, lParam)

    @staticmethod
    def value_to_msg(value,copydate=False):
        if copydate:
            cds=COPYDATASTRUCT()
            cds.dwData=0
            value=json.dumps(value).encode()
            cds.cbData = sizeof(create_string_buffer(value))
            cds.lpData = c_char_p(value)
            return byref(cds)
        else:
            value=json.dumps(value).encode()
            return c_char_p(value)
    @staticmethod
    def msg_to_value(wParam,lParam,copydate=False):
        if lParam!=0:
            try:
                if copydate:
                    pCDS=cast(lParam, PCOPYDATASTRUCT)
                    value=string_at(pCDS.contents.lpData).decode()
                else:
                    value=cast(lParam, c_char_p).value.decode()
            except:
                return
            value=json.loads(value)
            return value