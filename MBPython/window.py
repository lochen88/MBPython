# -*- coding:utf-8 -*-
from ctypes import (
    c_float,
    byref,
    windll
)
from ctypes.wintypes import MSG
from .wkeStruct import Rect

user32=windll.user32
class Window():
    def __init__(self,miniblink):
        self.width=360
        self.height=480
        self.mb=miniblink
    def wkeCreateWebWindow(self,_type=0,hwnd=0,x=0,y=0,width=360,height=480):
        
        webview =self.mb.wkeCreateWebWindow(
            _type,hwnd, x, y,
            width, height
        )
        return webview
    def wkeShowWindow(self,webview,_bool=True):
        self.mb.wkeShowWindow(webview,_bool)
    def wkeCreateWebView(self):
   
        return self.mb.wkeCreateWebView()
    def wkeDestroyWebView(self,webview):
        self.mb.wkeDestroyWebView(webview)
    def wkeMoveToCenter(self,webview):
        self.mb.wkeMoveToCenter(webview)
    def wkeRunMessageLoop(self):
        self.mb.wkeRunMessageLoop(0)
    def wkeSetUserAgentW(self,webview,ua):
        self.mb.wkeSetUserAgentW(webview,ua)
    def wkeGetUserAgent(self,webview):
        ua=self.mb.wkeGetUserAgent(webview)
        return ua.decode()        
    def wkeSetDragEnable(self,webview,_bool):
   
        self.mb.wkeSetDragEnable(webview,_bool)
    def wkeAddPluginDirectory(self,webview,_path):
 
        self.mb.wkeAddPluginDirectory(webview,_path)
    def wkeSetNpapiPluginsEnabled(self,webview,_bool,_path=None):
      
        if _path!=None:
            self.wkeAddPluginDirectory(webview,_path)
        self.mb.wkeSetNpapiPluginsEnabled(webview,_bool)
    def wkeSetCspCheckEnable(self,webview,_bool=False):

        self.mb.wkeSetCspCheckEnable(webview,_bool)
    def wkeSetDebugConfig(self,webview,debug,param):
       
        debug=debug.encode()
        if isinstance(param,str):
            param=param.encode()
        self.mb.wkeSetDebugConfig(webview,debug,param)
    def wkeSetHeadlessEnabled(self,webview,_bool):
      
        self.mb.wkeSetHeadlessEnabled(webview,_bool)
    def wkeSetNavigationToNewWindowEnable(self,webview,_bool):
       
        self.mb.wkeSetNavigationToNewWindowEnable(webview,_bool)
    def wkeSetWebViewName(self,webview,name):
        self.mb.wkeSetWebViewName(webview,name.encode())
    def wkeSetZoomFactor(self,webview,factor):
 
        self.mb.wkeSetZoomFactor(webview,factor)
    def wkeSetContextMenuEnabled(self,webview,_bool):
        
        self.mb.wkeSetContextMenuEnabled(webview,_bool)
    def wkeSetWindowTitleW(self,webview,title):
        self.mb.wkeSetWindowTitleW(webview, title)
    def wkeSetTransparent(self,webview,_bool):
  
        self.mb.wkeSetTransparent(webview,_bool)
    def wkeSetHandleOffset(self,webview,x,y):
      
        self.mb.wkeSetHandleOffset(webview,x,y)
    def wkeSetHandle(self,webview,hwnd):

        self.mb.wkeSetHandle(webview,hwnd)
    def wkeResize(self,webview,width=0,height=0):
        
        if width==0 or height==0:return False
        self.mb.wkeResize(webview,width,height)
        return True
    def wkeWidth(self,webview):
  
        return self.mb.wkeWidth(webview)
    def wkeHeight(self,webview):
     
        return self.mb.wkeHeight(webview)
    def wkeContentsWidth(self,webview):
      
        return self.mb.wkeContentsWidth(webview)
    def wkeContentsHeight(self,webview):
       
        return self.mb.wkeContentsHeight(webview)
    def wkeGoForward(self,webview):
        self.mb.wkeGoForward(webview)
    def wkeGoBack(self,webview):
        self.mb.wkeGoBack(webview)
    def wkeGetWindowHandle(self,webview):
     
        return self.mb.wkeGetWindowHandle(webview)

    def wkeGetViewDC(self,webview):
     
        hdc=self.mb.wkeGetViewDC(webview)
        return hdc
    def wkeSetTouchEnabled(self,webview,_bool):
   
        b=not _bool
        self.mb.wkeSetTouchEnabled(webview,_bool)
      
        self.mb.wkeSetMouseEnabled(webview,b)
    def simulate_device(self,webview,key,value,_int,_float):
   
        key=key.encode()
        if value=='':
            value=b''
        else:
            value=value.encode()
        self.mb.wkeSetDeviceParameter(webview, key,value,_int,c_float(_float))
    def bind_window(self,hwnd=0,show=True):
   
        if hwnd==0:
            user32.PostQuitMessage(0)
            return 0
        webview=self.wkeCreateWebWindow(_type=2,hwnd=hwnd)
        rc=Window.get_client_rect(hwnd)
        width = rc.Right - rc.Left
        height = rc.Bottom - rc.Top
 
        self.wkeResize(webview,width,height)
        self.wkeShowWindow(webview,show)
        return webview
    def message_loop(self,webview=None):
    
        msg = MSG()
        while user32.GetMessageW(byref(msg), None, 0, 0) > 0:
            user32.TranslateMessage(byref(msg))
            user32.DispatchMessageW(byref(msg))


    @staticmethod
    def get_window_rect(hwnd):
        rect=Rect()
        user32.GetWindowRect(hwnd,byref(rect))
        return rect

    @staticmethod
    def get_client_rect(hwnd):
        rect=Rect()
        user32.GetClientRect(hwnd,byref(rect))
        return rect
