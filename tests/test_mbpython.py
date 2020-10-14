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
from MBPython import set_icon
from config import icon_path
from ctypes import windll
import win32gui
user32=windll.user32


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
        return jsrunpy.to_js_args_val(es,'点击菜单')
    elif val_ls[0]=='loadurl':
        j_webview=window.wkeCreateWebWindow(0,0,0,360,480)
        network.wkeLoadURLW(j_webview,'https://www.baidu.com/')
        window.wkeShowWindow(j_webview)
    return 0
def test():
    global jsrunpy,window,network
    
    wke=miniblink.MiniBlink
    mb=wke.init()
    if mb==0:return
    
    window=wke.window
    callback=wke.callback
    network=wke.network
    pyrunjs=wke.pyrunjs
    jsrunpy=wke.jsrunpy
    cbtest=callBackTest(mb,pyrunjs,callback,network)

    webview=window.wkeCreateWebWindow(0,0,0,860,760)
    window.wkeMoveToCenter(webview)
    window.wkeShowWindow(webview)
    # window.wkeShowWindow(webview)
    window.wkeSetWindowTitleW(webview,'MBPython-测试-1191826896')
    window.wkeSetCspCheckEnable(webview,False)
    
    window.wkeSetUserAgentW(webview,'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Mobile Safari/537.36')
    jsrunpy.python_func=test_js_run_py
    callback.wkeDocumentReady2Callback=cbtest.document_ready_func

    param='测试传参'.encode('utf8')
    callback.wkeOnDocumentReady2(webview,param=param)
    callback.wkeOnWindowDestroy(webview)


    # network.wkeLoadURLW(webview,'https://www.baidu.com/')
    # network.wkeLoadURLW(webview,'https://music.163.com/')
    network.wkeLoadFile(webview,'/testjs/testjs.html')
    # network.wkeLoadHTMLW(webview,'<div>1191826896</div>')


    hwnd=window.wkeGetWindowHandle(webview)
    jsrunpy.bind_func(func_name='call_py_func', arg_count=1, param=hwnd)
    set_icon(hwnd,icon_path)

    window.wkeRunMessageLoop()

if __name__=='__main__':
    test()
    ...
