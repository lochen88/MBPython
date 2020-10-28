# -*- coding:utf-8 -*-
import os
import sys
from pathlib import Path
current_folder = Path(__file__).absolute().parent
father_folder = str(current_folder.parent)
os.chdir(str(current_folder))
sys.path.append(father_folder)

from callbackfunc import callBackTest
from MBPython import miniblink
from config import node_path

import win32gui
from win32con import *
from ctypes import windll
user32=windll.user32
def WndProc(hwnd,msg,wParam,lParam):
    if msg == WM_DESTROY:
        win32gui.PostQuitMessage(0)
        sys.exit(0)
        return 0
    return win32gui.DefWindowProc(hwnd,msg,wParam,lParam)
def get_hwnd():
    wc = win32gui.WNDCLASS()
    wc.hbrBackground = COLOR_BTNFACE + 1
    wc.hCursor = win32gui.LoadCursor(0,IDI_APPLICATION)
    wc.lpszClassName = "MBPython"
    wc.style =  CS_GLOBALCLASS|CS_VREDRAW | CS_HREDRAW
    wc.lpfnWndProc = WndProc
    reg = win32gui.RegisterClass(wc)
    hwnd = win32gui.CreateWindow(reg,'MBPython-webview绑定测试-1191826896',WS_CLIPCHILDREN|WS_CLIPSIBLINGS|WS_POPUP|WS_MINIMIZEBOX,300,100,860,760,0,0,0,None)
    return hwnd
def test_js_run_py(**kwargs):
    es=kwargs['es']
    param=kwargs['param']
    arg_count=jsrunpy.mb.jsArgCount(es)
    val_ls=jsrunpy.get_js_args_val(es,arg_count)
    print(val_ls,'test_js_run_py')
    
    hwnd=param
    if val_ls[0]=='move':
        user32.ReleaseCapture()
        user32.SendMessageW(hwnd,161, 2, 0)
    elif val_ls[0]=='close':
        win32gui.PostQuitMessage(0)
    elif val_ls[0]=='max':
        ismax=user32.IsZoomed(hwnd)
        if ismax==0:
            user32.ShowWindow(hwnd,3)
        elif ismax==1:
            user32.ShowWindow(hwnd,1)
    elif val_ls[0]=='min':
        user32.ShowWindow(hwnd,2)
    elif val_ls[0]=='menu':
        return jsrunpy.to_js_args_val(es,'click-menu')
    elif val_ls[0]=='loadurl':
        j_webview=window.wkeCreateWebWindow(0,0,0,0,360,480)
        network.wkeLoadURLW(j_webview,'https://www.baidu.com/')
        window.wkeShowWindow(j_webview)
    return 0
def test():
    mbpython=miniblink.Miniblink
    mb=mbpython.init(node_path)
    wke=mbpython(mb)
    if mb==0:return
    global jsrunpy,window,network
    window=wke.window
    callback=wke.callback
    network=wke.network
    pyrunjs=wke.pyrunjs
    jsrunpy=wke.jsrunpy
    bindwebview=wke.bindwebview
    cbtest=callBackTest(mb,pyrunjs,callback,network)
    
    callback.wkeDocumentReady2Callback=cbtest.document_ready_func
    jsrunpy.python_func=test_js_run_py

    hwnd=get_hwnd()
    jsrunpy.bind_func('call_py_func', arg_count=2, param=hwnd)
    webview=bindwebview.bind_webview(hwnd=hwnd,isTransparent=True,isZoom=True)
    param='测试绑定webview'

    callback.wkeOnDocumentReady2(webview,param)

    # network.wkeLoadURLW(webview,'https://www.baidu.com/')
    

    # win32gui.ShowWindow(hwnd,SW_SHOWNORMAL)
    win32gui.ShowWindow(hwnd,SW_SHOWNORMAL)

    network.wkeLoadFile(webview,'/testjs/testjs.html')
    
    win32gui.PumpMessages()
if __name__=='__main__':
    test()