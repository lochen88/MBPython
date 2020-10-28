# -*- coding:utf-8 -*-
from .winConst import WinConst
import win32gui
import win32api


class WndProcHook:
    def __init__(self,webview,hwnd):
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
            ret=self.msg_func_dict[msg](self.webview,hwnd,wParam, lParam)
            if ret!=None:
                return ret
        if hasattr(self,'onWndProcCallback'):
            ret=self.onWndProcCallback(hwnd=hwnd, msg=msg, wParam=wParam, lParam=lParam)
            if ret!=None:
                return ret
        if msg == WinConst.WM_DESTROY: 
            self.unhook_WndProc()
        return win32gui.CallWindowProc(self.oldWndProc, hwnd, msg, wParam, lParam)