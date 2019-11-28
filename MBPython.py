#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: lochen88
@site: https://github.com/lochen88/MBPython3
@qq: 1191826896
@description: 基于miniblink封装 普通版不支持多线程调用
"""

from module.wkeStruct import *
from module.winConst import *
import win32gui
import threading
import os
# import requests
init_path=os.getcwd()
m_oldProc=0



def method(prototype):
    class MethodDescriptor(object):
        __slots__ = ['func', 'bound_funcs']
        def __init__(self, func):
            self.func = func
            self.bound_funcs = {} # 保留引用 防止gc回收
        def __get__(self, obj, type=None):
            if obj!=None:
                try:
                    return self.bound_funcs[obj,type]
                except:
                    ret = self.bound_funcs[obj,type] = prototype(
                        self.func.__get__(obj, type))
                    return ret
    return MethodDescriptor
    
class MBPython3(threading.Thread):

    def __init__(self, *args, **kwargs):
        super(MBPython3,self).__init__(*args, **kwargs)
        self._width=360
        self._height=480
        self._url="http://www.baidu.com"
        self.webview=0

    def run(self):

        self.mb=self.mb_init(f'{init_path}/module/node.dll')
        webview=self.create_window(0,self._width, self._height)
        view_hwnd=self.get_hwnd(webview)
        self.js_bind_func('mouseMsg',arg_count=1,param=view_hwnd)

        #关闭跨域
        # self.set_csp(webview,False)
        #开启弹出新窗口
        # self.set_new_window_enable(webview,True)
        #开启flash播放
        # self.set_plugin_path(webview,init_path+'/plugins')
        #开启开发者工具
        # self.set_debug_config(webview,'showDevTools',init_path+'/front_end/inspector.html')

        self.move_to_center(webview)
        self.set_window_title(webview, 'QQ-1191826896-TEST')
        self.show_window(webview, True)

        # self.set_storage_path(webview,f'{init_path}/LocalStorage')
        # self.set_cookie_path(webview,init_path)
        # self.test_proxy(1,'117.70.39.105','4276',webview=webview)
        self.test_all_callback(webview)
        

        self.load_url(webview, self._url)
        # self.mb.wkeLoadFile(webview,b'mouseMsg/mouseMsg.html')
 

        self.message_loop(webview)

    def message_loop(self,webview=None):

        msg = MSG()
        ret=1
        while ret > 0:
            ret=user32.GetMessageW(byref(msg), None, 0, 0)
            user32.TranslateMessage(byref(msg))
            user32.DispatchMessageW(byref(msg))

    #-------------------------------------
    #参数void* param可以传任意类型 
    def wkeOnCreateView(self,webview,param=0):
        self.mb.wkeOnCreateView(webview,self.onCreateView,param)
    def wkeOnPaintUpdated(self,webview,callbackParam=0):
        self.mb.wkeOnPaintUpdated(webview,self.onPaintUpdated,callbackParam)
    def wkeOnPaintBitUpdated(self,webview,callbackParam=0):
        self.mb.wkeOnPaintBitUpdated(webview,self.onPaintBitUpdated,callbackParam)
    def wkeOnNavigation(self,webview,param=0):
        self.mb.wkeOnNavigation(webview,self.onNavigation,c_char_p(b'hi'))
    def wkeOnTitleChanged(self,webview,callbackParam=0):
        self.mb.wkeOnTitleChanged(webview,self.onTitleChanged,callbackParam)
    def wkeOnURLChanged2(self,webview,callbackParam=0):
        self.mb.wkeOnURLChanged2(webview,self.onURLChanged2,callbackParam)
    def wkeOnMouseOverUrlChanged(self,webview,callbackParam=0):
        self.mb.wkeOnMouseOverUrlChanged(webview,self.onMouseOverUrlChanged,callbackParam)
    def wkeOnAlertBox(self,webview,callbackParam=0):
        self.mb.wkeOnAlertBox(webview,self.onAlertBox,callbackParam)
    def wkeOnConfirmBox(self,webview,callbackParam=0):
        self.mb.wkeOnConfirmBox(webview,self.onConfirmBox,callbackParam)
    def wkeOnPromptBox(self,webview,callbackParam=0):
        self.mb.wkeOnPromptBox(webview,self.onPromptBox,callbackParam)
    def wkeOnConsole(self,webview,param=0):
        self.mb.wkeOnConsole(webview,self.onConsole,param)
    def wkeOnDownload(self,webview,param=0):
        self.mb.wkeOnDownload(webview,self.onDownload,param)
    def wkeOnDocumentReady2(self,webview,param=0):
        self.mb.wkeOnDocumentReady2(webview,self.onDocumentReady2,param)
    def wkeNetOnResponse(self,webview,param=0):
        self.mb.wkeNetOnResponse(webview,self.onResponse,param)
    def wkeOnLoadUrlBegin(self,webview,callbackParam=0):
        self.mb.wkeOnLoadUrlBegin(webview,self.onLoadUrlBegin,callbackParam)
    def wkeOnLoadUrlEnd(self,webview,callbackParam=0):
        self.mb.wkeOnLoadUrlEnd(webview,self.onLoadUrlEnd,callbackParam)
    def wkeOnLoadUrlFail(self,webview,callbackParam=0):
        self.mb.wkeOnLoadUrlFail(webview,self.onLoadUrlFail,callbackParam)
    def wkeOnLoadingFinish(self,webview,param=0):
        self.mb.wkeOnLoadingFinish(webview,self.onLoadingFinish,param)
    def wkeNetGetFavicon(self,webview,param=0):

        #此接口必须在wkeOnLoadingFinish回调里调用
        self.mb.wkeNetGetFavicon(webview,self.onNetGetFavicon,param)
    def wkeOnWindowClosing(self,webview,param=0):

        self.mb.wkeOnWindowClosing(webview,self.onWindowClosing,param)
    def wkeOnWindowDestroy(self,webview,param=0):

        self.mb.wkeOnWindowDestroy(webview,self.onWindowDestroy, param)
    #-----------------回调函数--------------------
    @method(CFUNCTYPE(c_int, c_int, c_void_p,c_int,c_void_p,POINTER(wkeWindowFeatures)))
    def onCreateView(self,webview,param,navigationType,url,windowFeatures):
        #创建新页面 回调函数
        #比如说调用了window.open或者点击了<a target="_blank" .../>

        url = c_wchar_p(self.mb.wkeGetStringW(url)).value
        # print('onCreateView:',url,navigationType)

        if navigationType==0:
            new_webview=self.create_window(0,self._width, self._height)
            self.mb.wkeLoadURLW(new_webview,url)
            self.mb.wkeShowWindow(new_webview,True)
            # self.test_all_callback(new_webview)
            return new_webview
        #返回0表示不创建新窗口
        return 0

    @method(CFUNCTYPE(None,c_int,c_void_p,c_void_p,c_int,c_int,c_int,c_int))
    def onPaintUpdated(self,webview,param,hdc,x,y,cx,cy):
        #页面刷新 回调函数
        # print('onPaintUpdated:',hdc,x,y,cx,cy,param)
        if param==None:return
        hwnd=param
        ret=user32.GetWindowLongW(hwnd,WinConst.GWL_EXSTYLE)
        if (ret & WinConst.WS_EX_LAYERED)== WinConst.WS_EX_LAYERED:
            #离屏渲染（待实现）
            rectDest=MBPython3.get_client_rect(hwnd)
            sizeDest=mSize(rectDest.Right - rectDest.Left,rectDest.Bottom - rectDest.Top)
            pointSource=mPos()
            bmp=bitMap()
            hBmp = win32gui.GetCurrentObject(hdc, WinConst.OBJ_BITMAP)
            gdi32.GetObjectA(hBmp, 24, byref(bmp))
            sizeDest.cx = bmp.bmWidth
            sizeDest.cy = bmp.bmHeight

            hdcScreen = user32.GetDC(hwnd)

            blend=blendFunction()
            blend.BlendOp = 0   #AC_SRC_OVER
            blend.BlendFlags = 0
            blend.SourceConstantAlpha = 255
            blend.AlphaFormat = 1  #AC_SRC_ALPHA
            callOk = user32.UpdateLayeredWindow(hwnd, hdcScreen, 0, byref(sizeDest), hdc, byref(pointSource),RGB(255,255,255), byref(blend), WinConst.ULW_ALPHA) #ULW_ALPHA

            if callOk==0:
                hdcMemory = gdi32.CreateCompatibleDC (hdcScreen)
                hbmpMemory = gdi32.CreateCompatibleBitmap (hdcScreen, sizeDest.cx, sizeDest.cy)
                hbmpOld = gdi32.SelectObject (hdcMemory, hbmpMemory)

                gdi32.BitBlt(hdcMemory, 0, 0, sizeDest.cx, sizeDest.cy, hdc, 0, 0, WinConst.SRCCOPY | WinConst.CAPTUREBLT)

                gdi32.BitBlt(hdc, 0, 0, sizeDest.cx, sizeDest.cy, hdcMemory, 0, 0,WinConst.SRCCOPY | WinConst.CAPTUREBLT)

                callOk = user32.UpdateLayeredWindow(hwnd, hdcScreen, 0, byref(sizeDest), hdcMemory, byref(pointSource), RGB(255,255,255), byref(blend), WinConst.ULW_ALPHA)

                gdi32.SelectObject(hdcMemory, hbmpOld)
                gdi32.DeleteObject(hbmpMemory)
                gdi32.DeleteDC(hdcMemory)
            user32.ReleaseDC(hwnd, hdcScreen)
        else:
            rc=Rect(x,y,x+cx,y+cy)
            user32.InvalidateRect(hwnd, byref(rc), True)

        # rectDest=MBPython3.get_client_rect(hwnd)
        # self.set_resize(webview,rectDest.Right - rectDest.Left,rectDest.Bottom - rectDest.Top)
        return
    @method(CFUNCTYPE(None,c_int,c_void_p,c_void_p,POINTER(wkeRect),c_int,c_int))
    def onPaintBitUpdated(self,webview,param,buf,r,width,height):

        x=r.contents.x
        y=r.contents.y

        # print('onPaintBitUpdated:',buf,x,y,width,height,param)
        ...
        return
    @method(CFUNCTYPE(None, c_int, c_void_p,c_int,c_void_p))
    def onNavigation(self,webview,param,navigationType,url):
        #网页开始浏览 回调函数
        #navigationType 0:LINKCLICK,1:FORMSUBMITTE,2:BACKFORWARD,
        #3:RELOAD,4:FORMRESUBMITT,5:OTHER
        url = c_wchar_p(self.mb.wkeGetStringW(url)).value
        # print("navigate:", url, " TrigType:", navigationType)
        return
    @method(CFUNCTYPE(None, c_int, c_void_p, c_void_p))
    def onTitleChanged(self,webview, param, title):

        title = c_wchar_p(self.mb.wkeGetStringW(title)).value
        print(f'TitleChanged:{title}')
        return
    @method(CFUNCTYPE(None, c_int, c_void_p,c_int,c_void_p))
    def onURLChanged2(self,webview,param,frameId,url):

        url = c_wchar_p(self.mb.wkeGetStringW(url)).value
        # print(f'URLChanged2:{url}',f'frameId:{frameId}')

        ...
        return
    @method(CFUNCTYPE(None, c_int, c_void_p,c_void_p))
    def onMouseOverUrlChanged(self,webview,param,url):
        url = c_wchar_p(self.mb.wkeGetStringW(url)).value
        # print('MouseOverUrl:',url)
        return
    @method(CFUNCTYPE(None, c_int, c_void_p,c_void_p))
    def onAlertBox(self,webview,param,msg):
        #网页调用alert 回调函数
        #运行这个会回调后 alert不再弹出
        #可以用来自定义弹出框
        msg = c_wchar_p(self.mb.wkeGetStringW(msg)).value
        print(msg)
        return
    @method(CFUNCTYPE(c_bool, c_int, c_void_p,c_void_p))
    def onConfirmBox(self,webview,param,msg):

        msg = c_wchar_p(self.mb.wkeGetStringW(msg)).value
        print('msg',msg)
 
        return True
        #return False
    @method(CFUNCTYPE(c_bool, c_int, c_void_p,c_void_p,c_void_p,c_void_p))
    def onPromptBox(self,webview,param,msg,defaultResult,result):
  
        #提示信息:msg
        msg = c_wchar_p(self.mb.wkeGetStringW(msg)).value
        print('msg:',msg)
        #默认值:defaultResult
        defaultResult = c_wchar_p(self.mb.wkeGetStringW(defaultResult)).value
        print('defaultResult',defaultResult)
        #返回值:result
        new_result='测试测试'
        #对result结构体设置文本
        self.set_wkestring(result,new_result)
        #返回True执行确认,False不执行
        return True
        #return False
    @method(CFUNCTYPE(None, c_int,c_void_p, c_int,c_void_p,c_void_p,c_ulonglong,c_void_p))
    def onConsole(self,webview,param,level,msg,sourceName,sourceLine,stackTrace):

        # msg= c_wchar_p(self.mb.wkeGetStringW(msg)).value
        # sourceName=c_wchar_p(self.mb.wkeGetStringW(sourceName)).value
        # print('onConsole:',msg)
        ...
        return
    @method(CFUNCTYPE(c_bool,c_int,c_void_p,c_char_p))
    def onDownload(self,webview,param,url):
  
        url=url.decode()
        print('onDownload:',url)
        #获取下载链接 下载另外写

        # response=requests.get(url)
        # with open(r'C:\Users\Administrator\Desktop\1.exe', 'wb') as f:
        #     f.write(response.content)
        #返回True或False没区别
        return True

    @method(CFUNCTYPE(None,c_int,c_void_p,c_void_p))
    def onDocumentReady2(self,webview,param,frameId):

        url=self.get_frame_url(webview,frameId)
        print('onDocumentReady2:',frameId,'url:',url)
        if self.mb.wkeIsDocumentReady(webview)!=0:
            # print(self.get_source(webview))

            # self.test_js(webview)

            # self.test_device(webview)

            # print(self.get_cookie(webview))

            ...
        return
    @method(CFUNCTYPE(c_bool,c_int,c_void_p,c_char_p,c_void_p))
    def onResponse(self,webview,param,url,job):
        #response响应 回调函数

        url = url.decode()
        # print('onResponse',url)
        #返回True不再访问,False继续访问
        return False
    @method(CFUNCTYPE(c_bool,c_int,c_void_p,c_char_p,c_void_p))
    def onLoadUrlBegin(self,webview,param,url,job):
        url=url.decode('utf8')
        #任何网络网络即将加载 回调函数
        # print('onLoadUrlBegin:',url)

        if url=='https://www.baidu.com/':
            #运行wkeNetHookRequest方法
            #wkeOnLoadUrlEnd才生效
            self.mb.wkeNetHookRequest(job)
            ...


        #请求类型,1:get 2:post
        request_stype=self.mb.wkeNetGetRequestMethod(job)
        if request_stype==2:
            # data,lens,elements=self.get_post_data(job,url=url,ident='')
            # print('posturl:',url,data)
            ...

        #True表示mb不再发送网络请求,False表示mb依然会发送网络请求
        return False
    @method(CFUNCTYPE(None,c_int,c_void_p,c_char_p,c_void_p,c_void_p,c_int))
    def onLoadUrlEnd(self,webview,param,url,job,buf,lens):
        url=url.decode('utf8')

        # print('onLoadUrlEnd:',url)

        if url=='https://www.baidu.com/':
            data='我在你头上'
            data=data.encode()+c_char_p(buf).value
            self.set_response_data(job,data)
        return
    @method(CFUNCTYPE(None,c_int,c_void_p,c_char_p,c_void_p))
    def onLoadUrlFail(self,webview,param,url,job):

        url=url.decode()
        print('onLoadUrlFail:',url)

        # if 'https://www.baidu.com' in url:
        #     self.set_proxy('115.213.186.155','4285')
        #     self.mb.wkeLoadURLW(webview, url)
        #     ...


        return
    @method(CFUNCTYPE(None,c_int,c_void_p,c_void_p,c_int,c_void_p))
    def onLoadingFinish(self,webview,param,url,result,failedReason):

        #result 0:succeed,1:failed,2:canceled
        url = c_wchar_p(self.mb.wkeGetStringW(url)).value
        failedReason=c_wchar_p(self.mb.wkeGetStringW(failedReason)).value
        # print('onLoadingFinish:',url,result,failedReason)

        self.wkeNetGetFavicon(webview,0)


        return

    @method(CFUNCTYPE(None, c_int, c_void_p,c_char_p,POINTER(wkeMemBuf)))
    def onNetGetFavicon(self,webview,param,url,buf):
  
        url=url.decode()
        print('onNetGetFavicon',url)

    @method(CFUNCTYPE(c_bool, c_int, c_void_p))
    def onWindowClosing(self,webview, param):

        # print('onWindowClosing')
        return True

    @method(CFUNCTYPE(None, c_int, c_void_p))
    def onWindowDestroy(self,webview, param):

        print('onWindowDestroy')
        # self.clear_all_cookie(webview)
        webview=None
        MBPython3.mb_quit()
        return
    #------------------js-py交互-------------------
    @method(CFUNCTYPE(c_longlong, c_int, c_void_p))
    def mouseMsg (self,es,param):
        #js调用py函数例子
        arg_count=self.mb.jsArgCount(es)
        if arg_count==0:return 0
        val_ls=self.get_js_args_val(es,arg_count)
        #print(val_ls,'mouseMsg')

        hwnd=param
        if val_ls[0]=='move':
            user32.ReleaseCapture()
            #发送按标题栏的消息
            user32.SendMessageW(hwnd,161, 2, 0)
            return self.to_js_args_val(es,'我在移动')

        elif val_ls[0]=='close':
            self.mb_quit()
        elif val_ls[0]=='max':
            ismax=user32.IsZoomed(hwnd)
            if ismax==0:
                user32.ShowWindow(hwnd,3)
            elif ismax==1:
                user32.ShowWindow(hwnd,1)
        elif val_ls[0]=='min':
            user32.ShowWindow(hwnd,2)
        return 0

    #运行本地js文件
    def run_js_file(self,webview,file_name):
        with open(file_name) as f:
            js_code=f.read()
            self.run_js(webview,js_code)

    #py调用js方法一
    def run_js(self,webview,js_code):

        es=self.mb.wkeGlobalExec(webview)
        val=self.mb.wkeRunJSW(webview,js_code)
        val=self.mb.jsToStringW(es,c_longlong(val))
        val=c_wchar_p(val)
        print(val.value,'run_js')
        return val.value


    #py调用js方法二 指定frame运行js
    def run_js_byframe(self,webview,frameId,js_code,isInClosure=True):
        #isInClosure表示是否在外层包个function(){}形式的闭包
        #isInClosure若为True,其实最后传给mb的js代码是这样:'functiuon(){window.onJsCall(1, "str", 1.3);}
        js_code=js_code.encode()
        val=self.mb.wkeRunJsByFrame(webview,frameId,js_code,isInClosure)
        es = self.mb.wkeGetGlobalExecByFrame(webview, frameId)
        val=self.mb.jsToTempStringW(es, c_longlong(val))
        val=c_wchar_p(val).value
        print(val,'run_js_byframe')
        return val

    #py调js方法三 调用html的全局js函数
    def run_js_global(self,webview,func_name,param_ls,this_func=None):
        #this_func 若func_name是成员函数 则需要填this_func
        #func_name 要调用的js函数
        #若func_name是window.xxx类型,直接取xxx名称即可
        #this_func.func_name???
        es=self.mb.wkeGlobalExec(webview)
        if this_func==None:
            this_func=0
            func_name=func_name.encode()
            func=self.mb.jsGetGlobal(es,c_char_p(func_name))
        else:
            #调用成员函数未实现
            # this_func=this_func.encode()
            # this_func=self.mb.jsGetGlobal(es,c_char_p(this_func))
            # func_name=func_name.encode()
            # func=self.mb.jsGet(es,c_char_p(this_func),c_char_p(func_name))
            # print(func)
            ...


        argCount=len(param_ls)
        args_ls=(c_longlong *argCount)()
        #param 要传递的js参数 根据类型转换成相应的js类型
        i=0
        for param in param_ls:
            if type(param)==str:
                param=self.mb.jsStringW(es,c_wchar_p(param))
            elif type(param)==int:
                param=self.mb.jsInt(param)
            elif type(param)==float:
                param=self.mb.jsFloat(c_float(param))
            elif type(param)==bool:
                param=self.mb.jsBoolean(param)
            args_ls[i]=param
            i+=1

        callRet=self.mb.jsCall(es,c_longlong(func),c_longlong(this_func),byref(args_ls),argCount)


        val=self.mb.jsToStringW(es,c_longlong(callRet))
        val=c_wchar_p(val).value
        print(val,'run_js_global 3')
        return val

    #绑定py函数给js调用
    def js_bind_func(self,func_name,arg_count=1,param=0):
        bind_func=getattr(self,func_name)
        func_name=func_name.encode()
        self.mb.wkeJsBindFunction(c_char_p(func_name),bind_func,param,arg_count)
    #获取js调用绑定函数时传过来的参数值转换
    def get_js_args_val(self,es,arg_count):
        val_ls=[None]*arg_count
        for i in range(arg_count):
            #arg_type,0:int,1:string,2:bool,3:object,4:function,5:undefined,6:array,7:null

            arg_type=self.mb.jsArgType(es,i)
            # print(arg_type,i)
            if arg_type==0:
                val=self.mb.jsArg(es,i)
                val=self.mb.jsToInt(es, c_longlong(val))
            elif arg_type==1:
                val=self.mb.jsArg(es,i)
                val=self.mb.jsToTempStringW(es, c_longlong(val))
                val=c_wchar_p(val).value
            elif arg_type==2:
                val=self.mb.jsArg(es,i)
                val=self.mb.jsToTempStringW(es, c_longlong(val))
                val=c_wchar_p(val).value
                if val=='false':
                    val=False
                else:
                    val=True
            elif arg_type==5 or arg_type==7:
                val=0
            elif arg_type==6:
                #只封装了整数、字符串、逻辑型数组
                val=self.mb.jsArg(es,i)
                lens=self.mb.jsGetLength(es,c_longlong(val))
                tmp_arr=[None]*lens
                for i in range(lens):
                    tmp_val=self.mb.jsGetAt(es,c_longlong(val),i)
                    if self.mb.jsIsNumber(c_longlong(tmp_val))==1:
                        tmp_val=self.mb.jsToInt(es, c_longlong(tmp_val))
                    elif self.mb.jsIsString(c_longlong(tmp_val))==1:
                        tmp_val=self.mb.jsToTempStringW(es, c_longlong(tmp_val))
                        tmp_val=c_wchar_p(tmp_val).value
                    elif self.mb.jsIsBoolean(c_longlong(tmp_val))==1:
                        tmp_val=self.mb.jsToTempStringW(es, c_longlong(tmp_val))
                        tmp_val=c_wchar_p(tmp_val).value
                        if tmp_val=='false':
                            tmp_val=False
                        else:
                            tmp_val=True
                    tmp_arr[i]=tmp_val
                val=tmp_arr
            else:
                val=self.mb.jsArg(es,i)
                val=self.mb.jsToTempStringW(es, c_longlong(val))
                val=c_wchar_p(val).value
            val_ls[i]=val
        return val_ls

    #绑定函数返回给js的值转换
    def to_js_args_val(self,es,val):

        if type(val)==str:
            val=self.mb.jsStringW(es,c_wchar_p(val))
        elif type(val)==int:
            val=self.mb.jsInt(val)
        elif type(val)==float:
            val=self.mb.jsFloat(c_float(val))
        elif type(val)==bool:
            val=self.mb.jsBoolean(val)
        elif type(val)==list:
            lens=len(val)
            tmp_arr=self.mb.jsEmptyArray(es)
            for i in range(lens):
                if type(val[i])==int:
                    tmp_val=self.mb.jsInt(val[i])
                elif type(val[i])==str:
                    tmp_val=self.mb.jsStringW(es,c_wchar_p(val[i]))
                elif type(val[i])==float:
                    tmp_val=self.mb.jsFloat(c_float(val[i]))
                self.mb.jsSetAt(es, c_longlong(tmp_arr), i, c_longlong(tmp_val))
            val=tmp_arr
        elif type(val)==dict:
            tmp_obj=self.mb.jsEmptyObject(es)
            for k,v in val.items():
                if type(v)==int:
                    v=self.mb.jsInt(v)
                elif type(v)==str:
                    v=self.mb.jsStringW(es,c_wchar_p(v))
                elif type(v)==float:
                    v=self.mb.jsFloat(c_float(v))
                self.mb.jsSet(es,c_longlong(tmp_obj),k.encode(),c_longlong(v))
            val=tmp_obj
        return val
    #-------------cookie\代理操作------------
    def set_storage_path(self,webview,path):
        #格式如"c:\mb\LocalStorage\" 
        self.mb.wkeSetLocalStorageFullPath(webview,c_wchar_p(path))

    def set_cookie_enable(self,webview,_bool):
        #这个接口只是影响blink，并不会设置curl。所以还是会生成curl的cookie文件
        self.mb.wkeSetCookieEnabled(webview,_bool)

    def get_cookie(self,webview):
        cookie=c_wchar_p(self.mb.wkeGetCookieW(webview))
        return cookie.value

    @method(CFUNCTYPE(c_bool,c_void_p,c_char_p,c_char_p,c_char_p,c_char_p,c_char_p,c_int,c_int))
    def onCookieVisitor(self,params,name,value,domain,path,secure,httpOnly,expires):

        name=name.decode()
        value=value.decode()
        domain=domain.decode()
        # print(name,':',value,domain)
        return False

    def visit_all_cookie(self,webview,params=0):

        self.mb.wkeVisitAllCookie(webview,params,self.onCookieVisitor)
    #设置cookie  
    def set_cookie(self,webview,url,cookie):
        #cookie格式PERSONALIZE=123;expires=Monday, 13-Jun-2022 03:04:55 GMT

        cookie=cookie.split(';')
        for x in cookie:
            self.mb.wkeSetCookie(webview,url.encode('utf8'),x.encode('utf8'))
        #设置后要写入cookies.dat文件,才生效
        self.mb.wkePerformCookieCommand(webview,2)

    def set_cookie_path(self,webview,path):
        #如c:\mb
        self.mb.wkeSetCookieJarPath(webview,c_wchar_p(path))

    def set_cookie_full_path(self,webview,file_name):
        #如c:\mb\mycookie.dat
        self.mb.wkeSetCookieJarFullPath(webview,c_wchar_p(file_name))
    #清除所有cookie 
    def clear_all_cookie(self,webview):

        self.mb.wkeClearCookie(webview)

    #设置mb全局代理
    def set_proxy(self,ip,port,proxy_type=1,user=None,password=None):
        # proxy_type={
        # 0:WKE_PROXY_NONE,
        # 1:WKE_PROXY_HTTP,
        # 2:WKE_PROXY_SOCKS4,
        # 3:WKE_PROXY_SOCKS4A,
        # 4:WKE_PROXY_SOCKS5,
        # 5:WKE_PROXY_SOCKS5HOSTNAME}
        if user==None:
            user=b''
        else:
            user=user.encode('utf8')
        if password==None:
            password=b''
        else:
            password=password.encode('utf8')
        ip=ip.encode('utf8')
        port=int(port)
        proxy= wkeProxy(wkeProxyType=c_int(proxy_type), hostname=ip, port=c_ushort(port),user=user,password=password)
        self.mb.wkeSetProxy(byref(proxy))

        ...
    #设置指定webview的代理
    def set_webview_proxy(self,webview,ip,port,proxy_type=1,user=None,password=None):
        # proxy_type={
        # 0:WKE_PROXY_NONE,
        # 1:WKE_PROXY_HTTP,
        # 2:WKE_PROXY_SOCKS4,
        # 3:WKE_PROXY_SOCKS4A,
        # 4:WKE_PROXY_SOCKS5,
        # 5:WKE_PROXY_SOCKS5HOSTNAME}
        # ip='49.87.18.53'
        # port=4221
        if user==None:
            user=b''
        else:
            user=user.encode('utf8')
        if password==None:
            password=b''
        else:
            password=password.encode('utf8')
        ip=ip.encode('utf8')
        port=int(port)
        proxy= wkeProxy(wkeProxyType=c_int(proxy_type), hostname=ip, port=c_ushort(port),user=user,password=password)
        self.mb.wkeSetViewProxy(webview,byref(proxy))
    #----------------拦截过滤-----------------
    #保存mb缓存文件
    def mb_save_img(self,file_name,buf,lens):
        #在onLoadUrlEnd回调里面用 
        #file_name D:/test.jpg
        ret=(c_char *lens).from_address(buf)
        with open(file_name,'wb') as f:
            f.write(ret)

    #过滤链接 
    def cancel_request(self,job,url,ident_ls=['.jpg']):
        #在onLoadUrlBegin回调里面用

        for x in ident_ls:
            if  x in url:
                self.mb.wkeNetCancelRequest(job)
                return True
        return False

    #修改返回的内容 参数data类型bytes,file_name本地js文件
    def set_response_data(self,job,data=b'',file_name=None):
        #在onLoadUrlBegin、onLoadUrlEnd回调里面用  
        #data类型bytes
        #在onLoadUrlBegin用,可以hook某个js替换为本地js文件
        #如http://baidu.com/a.js替换为本地c:\mb\b.js

        lens=len(data)
        if lens!=0:
            self.mb.wkeNetSetData(job,c_char_p(data),lens)
            return True
        elif file_name!=None:
            with open(file_name) as f:
                data=f.read()
                data=data.encode()
                lens=len(data)
            if lens!=0:
                if '.js' in file_name:
                    self.mb.wkeNetSetMIMEType(job,c_char_p(b'text/javascript'))
                elif '.html' in file_name:
                    self.mb.wkeNetSetMIMEType(job,c_char_p(b'text/html'))
                self.mb.wkeNetSetData(job,c_char_p(data),lens)
                return True
        return False

    #获取post的数据(偶然会多几个字符)
    def get_post_data(self,job,url,ident=''):
        #在onLoadUrlBegin回调里面用
        if ident not in url:return '',0,None
        self.mb.wkeNetGetPostBody.restype=POINTER(wkePostBodyElements)
        elements=self.mb.wkeNetGetPostBody(job)
        try:
            data=elements.contents.element.contents.contents.data.contents.data
        except:
            return '',0,None

        lens=len(data)
        data=data.decode('utf8','ignore')

        return data,lens,elements

    #---------------------------------------
    #开启模拟触屏模式
    def set_touch(self,webview,_bool):
        b = not _bool
        self.mb.wkeSetTouchEnabled(webview,_bool)
        #开启触屏后，关闭鼠标消息
        self.mb.wkeSetMouseEnabled(webview,b)
    #模拟设备
    def simulate_device(self,webview):
        #设置操作系统
        self.mb.wkeSetDeviceParameter(webview, b"navigator.platform",b'Android',0,0)
        #设置cpu核心数
        self.mb.wkeSetDeviceParameter(webview, b"navigator.hardwareConcurrency",b'',8,0)
        #设置触摸点数
        self.mb.wkeSetDeviceParameter(webview, b"navigator.maxTouchPoints",b'',4,0)
        #设置屏幕宽度
        self.mb.wkeSetDeviceParameter(webview, b"screen.width",b'',360,0)
        #设置屏幕高度
        self.mb.wkeSetDeviceParameter(webview, b"screen.height",b'',480,0)
        #设置屏幕可用宽度
        self.mb.wkeSetDeviceParameter(webview, b"screen.availWidth",b'',360,0)
        #设置屏幕可用高度
        self.mb.wkeSetDeviceParameter(webview, b"screen.availHeight",b'',480,0)
        #设置色彩分辨率
        self.mb.wkeSetDeviceParameter(webview, b"screen.pixelDepth",b'',32,0)
        #设置色彩深度
        self.mb.wkeSetDeviceParameter(webview, b"screen.colorDepth",b'',32,0)

    def set_browser_name(self,webview,name):

        self.mb.wkeSetWebViewName(webview,name.encode())

    def set_zoom_factor(self,webview,factor):
        #默认是1
        self.mb.wkeSetZoomFactor(webview,c_float(factor))

    def set_new_window_enable(self,webview,_bool):

        self.mb.wkeSetNavigationToNewWindowEnable(webview,_bool)

    def Set_contextmenu_enabled(self,webview,_bool):

        self.mb.wkeSetContextMenuEnabled(webview,_bool)

    #设置无头模式,提高性能(目前无头和窗口模式不能同时实现)
    def set_headless(self,webview,_bool):

        self.mb.wkeSetHeadlessEnabled(webview,_bool)
    #设置关闭拖拽文件加载网页
    def set_drag_enable(self,webview,_bool):

        self.mb.wkeSetHeadlessEnabled(webview,_bool)

    #设置组件目录 用于flash播放
    def set_plugin_path(self,webview,_path):

        self.mb.wkeAddPluginDirectory(webview,_path)
    #开启关闭npapi插件，如flash
    def set_npapi_plugin_enable(self,webview,_bool,_path=None):

        if _path!=None:
            self.set_plugin_path(webview,_path)
        self.mb.wkeSetNpapiPluginsEnabled(webview,_bool)
    #设置开启跨域
    def set_csp(self,webview,_bool=False):
        #如果一个页面里面嵌入了另一个web应用的页面,这里可以把跨域检查关掉
        #关闭后，跨域检查将被禁止，此时可以做任何跨域操作，如跨域ajax，跨域设置iframe
        self.mb.wkeSetCspCheckEnable(webview,_bool)
    #设置调试配置选项
    def set_debug_config(self,webview,debug_text,param):
        #"showDevTools"开启开发者工具，此时param要填写开发者工具的资源路径，如file:///c:/miniblink-release/front_end/inspector.html。注意param此时必须是utf8编码。"wakeMinInterval"设置帧率，默认值是10，值越大帧率越低。"drawMinInterval"设置帧率，默认值是3，值越大帧率越低。"antiAlias"设置抗锯齿渲染。param必须设置为1。"minimumFontSize"最小字体。"minimumLogicalFontSize"最小逻辑字体。"defaultFontSize"默认字体。"defaultFixedFontSize"默认fixed字体。
        self.mb.wkeSetDebugConfig(webview,debug_text.encode(),param.encode())

    def set_wkestring(self,wkeString,text):
        text=text.encode('utf8')
        lens=len(text)
        return self.mb.wkeSetString(wkeString,text,lens)

    def set_focus(self,webview=0,hwnd=0):
        #如果webveiw关联了窗口，窗口也会有焦点

        # self.mb.wkeSetFocus(webview)
        if hwnd==0 and webview!=0:
            hwnd=self.get_hwnd(webview)
        if hwnd==0:return
        user32.SetFocus(hwnd)

    #---------------------------------------
    def mb_init(self,_path=None):
        #初始化整个mb。此句必须在所有mb api前最先调用。并且所有mb api必须和调用wkeInit的线程为同个线程
        if _path==None: return 0
        mb = cdll.LoadLibrary(_path)
        mb.wkeInit()
        return mb

    #创建窗口
    def create_window(self,_type,width,height,x=0,y=0,hwnd=0):
        #_type 0:普通窗口,1:透明窗口(可用于离屏渲染),2:嵌入式窗口
        #若要嵌入在父窗口里的子窗口,hwnd需要设置
        webview =self.mb.wkeCreateWebWindow(
            _type,hwnd, x, y,
            width, height
        )
        return webview

    def set_window_title(self,webview,title):

        self.mb.wkeSetWindowTitleW(webview, title)

    #创建一个webview,不是创建真窗口
    def create_webview(self):
        webview=self.mb.wkeCreateWebView()
        return webview

    def set_transparent(self,webview,_bool):
        #通知无窗口模式下,webview开启透明模式

        self.mb.wkeSetTransparent(webview,_bool)

    def set_hwnd_offset(self,webview,x,y):
        #设置无窗口模式下的绘制偏移。在某些情况下（主要是离屏模式），绘制的地方不在真窗口的(0, 0)处，就需要手动调用此接口
        self.mb.wkeSetHandleOffset(webview,x,y)
    
    #设置无窗口模式下的webview对应的窗口句柄
    def set_hwnd(self,webview,hwnd):

        self.mb.wkeSetHandle(webview,hwnd)

    def set_resize(self,webview,width=0,height=0):
        if width==0 or height==0:return False
        self.mb.wkeResize(webview,width,height)
        return True


    def show_window(self,webview,_bool):

        self.mb.wkeShowWindow(webview, _bool)

    def move_window(self,webview,x,y,w=0,h=0):
        if w==0 or h==0:
            self.mb.wkeMoveWindow(webview,x,y,self._width,self._height)
        else:
            self.mb.wkeMoveWindow(webview,x,y,w,h)

    def move_to_center(self,webview):

        self.mb.wkeMoveToCenter(webview)

    def go_forward(self,webview):

        self.mb.wkeGoForward(webview)

    def go_back(self,webview):

        self.mb.wkeGoBack(webview)

    def load_url(self,webview,url):

        self.mb.wkeLoadURLW(webview,url)
   
    def load_html_file(self,webview,file_name):

        self.mb.wkeLoadFile(webview,file_name.encode())

    def reload(self,webview):

        self.mb.wkeReload(webview)

    def stop_loading(self,webview):

        self.mb.wkeStopLoading(webview)

    def get_width(self,webview):

        return self.mb.wkeWidth(webview)

    def get_height(self,webview):

        return self.mb.wkeHeight(webview)

    def get_content_width(self,webview):

        return self.mb.wkeContentsWidth(webview)

    def get_content_height(self,webview):

        return self.mb.wkeContentsWidth(webview)
    #获取webview的窗口句柄
    def get_hwnd(self,webview):
        hwnd=self.mb.wkeGetWindowHandle(webview)
        return hwnd

    def get_url(self,webview):
        url=self.mb.wkeGetURL(webview)
        url=c_char_p(url).value
        return url.decode()

    def get_frame_url(self,webview,frameId):
        url=self.mb.wkeGetFrameUrl(webview,frameId)
        url=c_char_p(url).value
        return url.decode()

    def get_source(self,webview):
        source=self.mb.wkeGetSource(webview)
        source=c_char_p(source).value
        return source.decode()

    def get_mhtml(self,webview):

        mhtml=self.mb.wkeUtilSerializeToMHTML(webview)
        mhtml=c_char_p(mhtml).value
        # mhtml.decode()
        return mhtml
    #打印pdf(待完善)
    def get_pdf(self,webview,frameId=0,structSize=62370,dpi=720,width=297,height=210,marginTop=10,marginBottom=10,marginLeft=10,marginRight=10,isPrintPageHeadAndFooter=True,isPrintBackgroud=True,isLandscape=True):
        settings=wkePrintSettings(structSize,dpi,width,height,marginTop,marginBottom,marginLeft,marginRight,isPrintPageHeadAndFooter,isPrintBackgroud,isLandscape)
        self.mb.wkeUtilPrintToPdf.restype=(wkePdfDatas)
        data=self.mb.wkeUtilPrintToPdf(webview,frameId,byref(settings))
        print(data)
        return data

    def get_hdc(self,webview):

        hdc=self.mb.wkeGetViewDC(webview)
        return hdc

    def fire_mouse_event(self,webview,msg,x,y,flags=0):
        #flags可取值有WKE_CONTROL、WKE_SHIFT、WKE_LBUTTON、WKE_MBUTTON、WKE_RBUTTON，可通过“或”操作并联
        return self.mb.wkeFireMouseEvent(webview,msg,x,y,flags)
    #WM_KEYDOWN
    def fire_keydown_event(self,webview,virtualKeyCode,flags=0):

        return self.mb.wkeFireKeyDownEvent(webview,virtualKeyCode,flags,False)
    #WM_KEYUP
    def fire_keyup_event(self,webview,virtualKeyCode,flags=0):
        #可取值有WKE_REPEAT、WKE_EXTENDED，可通过“或”操作并联
        return self.mb.wkeFireKeyUpEvent(webview,virtualKeyCode,flags,False)

    def fire_press_event(self,webview,virtualKeyCode,flags):

        return self.mb.wkeFireKeyPressEvent(webview,virtualKeyCode,flags,False)

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

    @staticmethod
    def mb_quit():
        user32.PostQuitMessage(0)
        # os._exit(0)


    @method(WINFUNCTYPE(c_long,HWND, UINT,WPARAM,LPARAM))
    def onWndProc(self,hwnd,msg,wParam,lParam):
        global m_oldProc
        if msg==WinConst.WM_PAINT:
            if WinConst.WS_EX_LAYERED!=(WinConst.WS_EX_LAYERED & user32.GetWindowLongW(hwnd,WinConst.GWL_EXSTYLE)):
                self.mb.wkeRepaintIfNeeded(self.webview)
                ps=PAINTSTRUCT()
                hdc=user32.BeginPaint(hwnd,byref(ps))

                rcClip = ps.rcPaint
                rcClient=MBPython3.get_client_rect(hwnd)
                rcInvalid=rcClient

                if (rcClip.Right != rcClip.Left and rcClip.Bottom != rcClip.Top):
                    user32.IntersectRect(byref(rcInvalid),byref(rcClip),byref(rcClient))
                    srcX = rcInvalid.Left - rcClient.Left
                    srcY = rcInvalid.Top - rcClient.Top
                    destX = rcInvalid.Left
                    destY = rcInvalid.Top
                    width = rcInvalid.Right - rcInvalid.Left
                    height = rcInvalid.Bottom - rcInvalid.Top

                    if width!=0 and height!=0:
                        tmp_dc=self.get_hdc(self.webview)
                        gdi32.BitBlt(hdc,destX, destY, width, height,tmp_dc,srcX, srcY,WinConst.SRCCOPY)
                    user32.EndPaint(hwnd,byref(ps))

                    return 0
        if msg==WinConst.WM_ERASEBKGND:
            return 1
        if msg==WinConst.WM_SIZE:
            width= lParam & 65535
            height= lParam >> 16
            self.set_resize(self.webview,width,height)
            self.mb.wkeRepaintIfNeeded(self.webview)
            self.mb.wkeWake(self.webview)
            return 0
        if msg==WinConst.WM_KEYDOWN:
            virtualKeyCode=wParam
            flags=0
            if ((lParam >> 16) & WinConst.KF_REPEAT)!=0:
                flags=flags | 0x4000#WKE_REPEAT
            if ((lParam >> 16)  & WinConst.KF_EXTENDED)!=0:
                flags=flags | 0x0100#WKE_EXTENDED
            if self.fire_keydown_event(self.webview,virtualKeyCode,flags)!=0:
                return 0
        if msg==WinConst.WM_KEYUP:
            virtualKeyCode=wParam
            flags=0
            # if virtualKeyCode==123:#F12
            #     self.set_debug_config(self.webview,'showDevTools',init_path+'/front_end/inspector.html')
            if virtualKeyCode==116:#F5
                self.reload(self.webview)
            if ((lParam >> 16) & WinConst.KF_REPEAT)!=0:
                flags=flags | 0x4000#WKE_REPEAT
            if ((lParam >> 16) & WinConst.KF_EXTENDED)!=0:
                flags=flags | 0x0100#WKE_EXTENDED
            if self.fire_keyup_event(self.webview,virtualKeyCode,flags)!=0:
                return 0
        if msg==WinConst.WM_CHAR:
            virtualKeyCode=wParam
            flags=0
            if ((lParam >> 16) & WinConst.KF_REPEAT)!=0:
                flags=flags | 0x4000#WKE_REPEAT
            if self.fire_press_event(self.webview,virtualKeyCode,flags)!=0:
                return 0

        if msg==WinConst.WM_LBUTTONDOWN:

            ...
        if msg==WinConst.WM_MBUTTONDOWN:

            ...
        if msg==WinConst.WM_RBUTTONDOWN:
            ...
        if msg==WinConst.WM_LBUTTONDBLCLK:
            ...
        if msg==WinConst.WM_MBUTTONDBLCLK:
            ...
        if msg==WinConst.WM_RBUTTONDBLCLK:
            ...
        if msg==WinConst.WM_LBUTTONUP:

            ...
        if msg==WinConst.WM_MBUTTONUP:
            ...
        if msg==WinConst.WM_RBUTTONUP:
            ...

        if msg in [WinConst.WM_LBUTTONDOWN,WinConst.WM_MBUTTONDOWN,WinConst.WM_RBUTTONDOWN,WinConst.WM_LBUTTONDBLCLK,WinConst.WM_MBUTTONDBLCLK,WinConst.WM_RBUTTONDBLCLK,WinConst.WM_LBUTTONUP,WinConst.WM_MBUTTONUP,WinConst.WM_RBUTTONUP]:
            x=lParam & 65535
            y=lParam >> 16
            flags=0
            if msg in [WinConst.WM_LBUTTONDOWN,WinConst.WM_MBUTTONDOWN,WinConst.WM_RBUTTONDOWN]:
                if user32.GetFocus()!=hwnd:
                    user32.SetFocus(hwnd)
                user32.SetCapture(hwnd)

            elif msg in [WinConst.WM_LBUTTONUP,WinConst.WM_MBUTTONUP,WinConst.WM_RBUTTONUP]:
                user32.ReleaseCapture()

            if (wParam & WinConst.MK_CONTROL)!=0:
                flags=flags | 8#WKE_CONTROL
            if (wParam & WinConst.MK_SHIFT)!=0:
                flags=flags | 4#WKE_SHIFT
            if (wParam & WinConst.MK_LBUTTON)!=0:
                flags=flags | 1#WKE_LBUTTON
            if (wParam & WinConst.MK_MBUTTON)!=0:
                flags=flags | 16#WKE_MBUTTON
            if (wParam & WinConst.MK_RBUTTON)!=0:
                flags=flags | 2#WKE_RBUTTON
            if self.fire_mouse_event(self.webview, msg, x, y, flags)!=0:
                return 0
        if msg==WinConst.WM_MOUSEMOVE:
            x=lParam & 65535
            y=lParam >> 16
            flags=0
            if (wParam & WinConst.MK_LBUTTON)!=0:
                flags=flags | 1#WKE_LBUTTON
            if self.fire_mouse_event(self.webview, msg, x, y, flags)!=0:
                return 0
        if msg==WinConst.WM_CONTEXTMENU:
            pt=mPos()
            pt.x=lParam & 65535
            pt.y=lParam >> 16
            if pt.x!=-1 and pt.y!=-1:
                user32.ScreenToClient(hwnd,byref(pt))
            flags=0
            if (wParam & WinConst.MK_CONTROL)!=0:
                flags=flags | 8
            if (wParam & WinConst.MK_SHIFT)!=0:
                flags=flags | 4
            if (wParam & WinConst.MK_LBUTTON)!=0:
                flags=flags | 1
            if (wParam & WinConst.MK_MBUTTON)!=0:
                flags=flags | 16
            if (wParam & WinConst.MK_RBUTTON)!=0:
                flags=flags | 2

            if self.mb.wkeFireContextMenuEvent(self.webview,pt.x,pt.y, flags)!=0:
                return 0
        if msg==WinConst.WM_MOUSEWHEEL:
            pt=mPos()
            pt.x=lParam & 65535
            pt.y=lParam >> 16
            user32.ScreenToClient(hwnd,byref(pt))
            delta= wParam >> 16
            flags=0

            if (wParam & WinConst.MK_CONTROL)!=0:
                flags=flags | 8
            if (wParam & WinConst.MK_SHIFT)!=0:
                flags=flags | 4
            if (wParam & WinConst.MK_LBUTTON)!=0:
                flags=flags | 1
            if (wParam & WinConst.MK_MBUTTON)!=0:
                flags=flags | 16
            if (wParam & WinConst.MK_RBUTTON)!=0:
                flags=flags | 2
            if self.mb.wkeFireMouseWheelEvent(self.webview,pt.x,pt.y,delta,flags)!=0:
                return 0
        if msg==WinConst.WM_SETFOCUS:
            self.set_focus(hwnd=hwnd)
            return 0
        if msg==WinConst.WM_KILLFOCUS:
            self.mb.wkeKillFocus(self.webview)
            return 0
        if msg==WinConst.WM_IME_STARTCOMPOSITION:
            self.mb.wkeGetCaretRect.restype=(wkeRect)
            caret=self.mb.wkeGetCaretRect(self.webview)

            mposForm=COMPOSITIONFORM()
            mposForm.dwStyle = 2 | 32#CFS_POINT|CFS_FORCE_POSITION
            mposForm.ptCurrentPos.x = caret.x
            mposForm.ptCurrentPos.y = caret.y
            hIMC=imm32.ImmGetContext(hwnd)
            imm32.ImmSetCompositionWindow(hIMC,byref(mposForm))
            imm32.ImmReleaseContext(hwnd,hIMC)
            return 0
        if msg==WinConst.WM_NCHITTEST:
            if self.isZoom:
                if user32.IsZoomed(hwnd)!=0:
                    return 1
                pt=mPos()
                pt.x=lParam & 65535
                pt.y=lParam >> 16
                user32.ScreenToClient(hwnd,byref(pt))
                rc=MBPython3.get_client_rect(hwnd)
                iWidth = rc.Right - rc.Left
                iHeight = rc.Bottom - rc.Top
                if user32.PtInRect(byref(Rect(5, 0, iWidth - 5, 5)),pt.x, pt.y):
                    retn=12#HTTOP
                elif user32.PtInRect(byref(Rect(0, 5, 5, iHeight - 5)),pt.x, pt.y):
                    retn=10#HTLEFT
                elif user32.PtInRect(byref(Rect(iWidth - 5, 5, iWidth, iHeight - 10)),pt.x, pt.y):
                    retn=11#HTRIGHT
                elif user32.PtInRect(byref(Rect(5, iHeight - 5, iWidth - 10, iHeight)),pt.x, pt.y):
                    retn=15#HTBOTTOM
                elif user32.PtInRect(byref(Rect(0, 0, 5, 5)),pt.x, pt.y):
                    retn=13#HTTOPLEFT
                elif user32.PtInRect(byref(Rect(0, iHeight - 5, 5, iHeight)),pt.x, pt.y):
                    retn=16#HTBOTTOMLEFT
                elif user32.PtInRect(byref(Rect(iWidth - 5, 0, iWidth, 5)),pt.x, pt.y):
                    retn=14#HTTOPRIGHT
                elif user32.PtInRect(byref(Rect(iWidth - 10, iHeight - 10, iWidth, iHeight)),pt.x, pt.y):
                    retn=17#HTBOTTOMRIGHT
                else:
                    retn=1
                return retn
        if msg==WinConst.WM_SETCURSOR:
            if self.fire_window_message(self.webview,hwnd,WinConst.WM_SETCURSOR,wParam,lParam,0)!=0:
                return 0


        if msg==WinConst.WM_INPUTLANGCHANGE:
            return user32.DefWindowProcA(hwnd, msg, wParam, lParam)
        return user32.CallWindowProcW(m_oldProc, hwnd, msg, wParam, lParam)

    #绑定wkeCreateWebView创建的webview
    def bind_webview(self,webview=0,hwnd=0,isTransparent=False):
        if webview==0:
            self.webview=webview=self.create_webview()
            if webview==0:
                return False
        global m_oldProc

        self.set_hwnd(webview,hwnd)
        self.wkeOnPaintUpdated(webview,hwnd)

        if isTransparent:
            self.set_transparent(webview,True)
            exStyle=user32.GetWindowLongW(hwnd,WinConst.GWL_EXSTYLE)
            user32.SetWindowLongW(hwnd,WinConst.GWL_EXSTYLE,exStyle | WinConst.WS_EX_LAYERED)

        else:
            self.set_transparent(webview,False)


        m_oldProc=user32.SetWindowLongW(hwnd,WinConst.GWL_WNDPROC,self.onWndProc)

        rc=MBPython3.get_client_rect(hwnd)
        self.set_resize(webview,rc.Right - rc.Left, rc.Bottom - rc.Top)

        return True

    #绑定wkeCreateWebWindow创建的窗口
    def bind_window(self,hwnd=0,url='',html_file='',show=True):
        if hwnd==0:return 0
        webview=self.create_window(2,300,300,hwnd=hwnd)

        rc=MBPython3.get_client_rect(hwnd)
        width = rc.Right - rc.Left
        height = rc.Bottom - rc.Top

        if url!='':
            self.load_url(webview,url)
        if html_file!='':
            self.load_html_file(webview,html_file)

        self.set_resize(webview,width,height)
        if show:
            self.show_window(webview,True)
        return webview


    #---------------test----------------
    def test_proxy(self,func,ip,port,webview=0):
        if func==1:
            self.set_proxy(ip,port)
        else:
            self.set_webview_proxy(webview,ip,port)
    def test_js(self,webview):

        self.run_js(webview,'return test_1("mb")')

     
        mainFrame = self.mb.wkeWebFrameGetMainFrame(webview)
        self.run_js_byframe(webview,mainFrame,'window.test_2(1,2)',False)

        self.run_js_global(webview,'test_2',[3.14,0.06])

        ...
    def test_device(self,webview):
        self.set_touch(webview,True)
        self.simulate_device(webview)
        self.run_js(webview,'return navigator.platform')
        self.run_js(webview,'return navigator.hardwareConcurrency')
        self.run_js(webview,'return navigator.maxTouchPoints')
        self.run_js(webview,'return screen.width')
        self.run_js(webview,'return screen.height')
        self.run_js(webview,'return screen.availWidth')
        self.run_js(webview,'return screen.availHeight')
        self.run_js(webview,'return screen.pixelDepth')
        self.run_js(webview,'return screen.colorDepth')
        self.run_js(webview,'return navigator.userAgent')
    def test_all_callback(self,webview):
    
        # self.wkeOnWindowDestroy(webview, 0)
        # return
        self.wkeOnCreateView(webview, 0)
        # self.wkeOnPaintUpdated(webview, 0)
        self.wkeOnPaintBitUpdated(webview,0)
        self.wkeOnNavigation(webview,c_char_p(b'hi'))
        self.wkeOnTitleChanged(webview,0)
        self.wkeOnURLChanged2(webview,0)
        self.wkeOnMouseOverUrlChanged(webview,0)
        self.wkeOnAlertBox(webview,0)
        self.wkeOnConfirmBox(webview,0)
        self.wkeOnPromptBox(webview,0)
        self.wkeOnConsole(webview,0)
        self.wkeOnDownload(webview,0)
        self.wkeOnLoadingFinish(webview,0)
        self.wkeOnDocumentReady2(webview,0)
        self.wkeNetOnResponse(webview,0)
        # self.wkeOnLoadUrlBegin(webview,0)
        # self.wkeOnLoadUrlEnd(webview,0)
        self.wkeOnLoadUrlFail(webview,0)
        self.wkeOnWindowClosing(webview,0)
        self.wkeOnWindowDestroy(webview, 0)


if __name__ == '__main__':

    # window = MBPython3()
    # window.start()

    window = MBPython3()
    window.mb=window.mb_init(f'{init_path}/module/node.dll')
    webview=window.create_window(0,360,480)
    window.wkeOnWindowDestroy(webview,0)
    window.load_url(webview,'https://www.baidu.com/')
    window.wkeOnCreateView(webview,0)
    window.show_window(webview,True)
    window.message_loop()
    


