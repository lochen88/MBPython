# -*- coding:utf-8 -*-
from .winConst import *
from .myctypes import *
from .wkeStruct import (wkeRect,wkeWindowFeatures,wkeMemBuf,mPos)
from .method import method
from .defaultcallbackfunc import destroy_func
from config import _LRESULT
from win32gui import SetWindowLong
import json
user32.CallWindowProcW.argtypes=[_LRESULT,HWND, UINT,WPARAM,LPARAM]
user32.CallWindowProcW.restype=_LRESULT


'''
注意
param参数设计只允许str,int,float,tuple,list,dict类型
'''
class CallBack():
    def __init__(self,miniblink,width=360,height=480):
        self.mb=miniblink  
        self.width=width
        self.height=height
        self.wkeWindowDestroyCallback=destroy_func
    def wkeOnCreateView(self,webview,param=0):
        param=self.param_to_string(param)
        self.mb.wkeOnCreateView(webview,self._wkeCreateViewCallback,param)
    def wkeOnWindowClosing(self,webview,param=0):
        param=self.param_to_string(param)
        self.mb.wkeOnWindowClosing(webview,self._wkeWindowClosingCallback,param)
    def wkeOnWindowDestroy(self,webview,param=0):
        # if param!=0 and not isinstance(param,str):
        #     print('param类型错误，请传str类型')
        #     return
        # elif param!=0:
        #     param=self.mb.wkeCreateStringW(param,len(param))
        self.mb.wkeOnWindowDestroy(webview,self._wkeWindowDestroyCallback,param)
    def wkeOnPaintUpdated(self,webview,param=0):
        param=self.param_to_string(param)
        self.mb.wkeOnPaintUpdated(webview,self._wkePaintUpdatedCallback ,param)
    def wkeOnPaintBitUpdated(self,webview,param=0):
        param=self.param_to_string(param)
        self.mb.wkeOnPaintBitUpdated(webview, self._wkePaintBitUpdatedCallback,param)
    def wkeOnNavigation(self,webview,param=0):
        param=self.param_to_string(param)
        self.mb.wkeOnNavigation(webview,self._wkeNavigationCallback,param)
    def wkeOnTitleChanged(self,webview,param=0):
        param=self.param_to_string(param)
        self.mb.wkeOnTitleChanged(webview,self._wkeTitleChangedCallback,param)
    def wkeOnURLChanged2(self,webview,param=0):
        param=self.param_to_string(param)
        self.mb.wkeOnURLChanged2(webview,self._wkeURLChangedCallback2,param)
    def wkeOnMouseOverUrlChanged(self,webview,param=0):
        param=self.param_to_string(param)
        self.mb.wkeOnMouseOverUrlChanged(webview,self._wkeMouseOverUrlChangedCallback,param)
    def wkeOnAlertBox(self,webview,param=0):
        param=self.param_to_string(param)
        self.mb.wkeOnAlertBox(webview,self._wkeAlertBoxCallback,param)
    def wkeOnConfirmBox(self,webview,param=0):
        param=self.param_to_string(param)
        self.mb.wkeOnConfirmBox(webview,self._wkeConfirmBoxCallback,param)
    def wkeOnPromptBox(self,webview,param=0):
        param=self.param_to_string(param)
        self.mb.wkeOnPromptBox(webview,self._wkePromptBoxCallback,param)
    def wkeOnConsole(self,webview,param=0):
        self.mb.wkeOnConsole(webview,self._wkeConsoleCallback,param)
    def wkeOnDownload(self,webview,param=0):
        param=self.param_to_string(param)
        self.mb.wkeOnDownload(webview,self._wkeDownloadCallback,param)
    def wkeOnDocumentReady2(self,webview,param=0):
        param=self.param_to_string(param)
        self.mb.wkeOnDocumentReady2(webview,self._wkeDocumentReady2Callback,param)
    def wkeNetOnResponse(self,webview,param=0):
        param=self.param_to_string(param)
        self.mb.wkeNetOnResponse(webview,self._wkeNetResponseCallback,param)
    def wkeOnLoadUrlBegin(self,webview,param=0):
        param=self.param_to_string(param)
        self.mb.wkeOnLoadUrlBegin(webview,self._wkeLoadUrlBeginCallback,param)
    def wkeOnLoadUrlEnd(self,webview,param=0):
        param=self.param_to_string(param)
        self.mb.wkeOnLoadUrlEnd(webview,self._wkeLoadUrlEndCallback,param)
    def wkeOnLoadUrlFail(self,webview,param=0):
        param=self.param_to_string(param)
        self.mb.wkeOnLoadUrlFail(webview,self._wkeLoadUrlFailCallback,param)
    def wkeOnLoadingFinish(self,webview,param=0):
        param=self.param_to_string(param)
        self.mb.wkeOnLoadingFinish(webview,self._wkeLoadingFinishCallback,param)
    def wkeNetGetFavicon(self,webview,param=0):
        param=self.param_to_string(param)
        self.mb.wkeNetGetFavicon(webview,self._wkeOnNetGetFaviconCallback,param)





    def wkeOnWndProc(self,webview):
        hwnd=self.mb.wkeGetWindowHandle(webview)
        self.oldWndProc=SetWindowLong(hwnd,WinConst.GWL_WNDPROC,self._wkeWndProcCallback)

    '''
    ------------------回调函数---------------
    ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
    ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
    ------------------回调函数---------------
    '''
    @method(CFUNCTYPE(c_bool, _LRESULT, c_void_p))
    def _wkeWindowClosingCallback(self,webview, param):
        #webview若是真窗口模式,收到WM_CLODE消息触发此回调,返回False拒绝关闭窗口,返回True允许关闭
        if hasattr(self,'wkeWindowClosingCallback'):
            param=self.get_param_value(param)
            return self.wkeWindowClosingCallback(webview=webview,param=param)
        return True
    @method(CFUNCTYPE(None, _LRESULT, c_void_p))
    def _wkeWindowDestroyCallback(self,webview, param):
        if hasattr(self,'wkeWindowDestroyCallback'):
            param=self.get_param_value(param)
            self.wkeWindowDestroyCallback(webview=webview,param=param)
    @method(CFUNCTYPE(None,_LRESULT,c_void_p,_LRESULT,c_int,c_int,c_int,c_int))
    def _wkePaintUpdatedCallback(self,webview,param,hdc,x,y,cx,cy):
        if hasattr(self,'wkePaintUpdatedCallback'):
            param=self.get_param_value(param)
            self.wkePaintUpdatedCallback(webview=webview,param=param,hdc=hdc,x=x,y=y,cx=cx,cy=cy)
    @method(CFUNCTYPE(None,_LRESULT,c_void_p,_LRESULT,POINTER(wkeRect),c_int,c_int))
    def _wkePaintBitUpdatedCallback(self,webview,param,buf,rect,width,height):
        param=self.get_param_value(param)
        if hasattr(self,'wkePaintBitUpdatedCallback'):
            self.wkePaintBitUpdatedCallback(webview=webview,param=param,buf=buf,rect=rect,width=width,height=height)  
    @method(CFUNCTYPE(None,_LRESULT,c_void_p,c_void_p))
    def _wkeDocumentReady2Callback(self,webview,param,frameId):
        if hasattr(self,'wkeDocumentReady2Callback'):
            param=self.get_param_value(param)
            self.wkeDocumentReady2Callback(webview=webview,param=param,frameId=frameId)
    @method(CFUNCTYPE(_LRESULT, _LRESULT, c_void_p,c_int,c_void_p,POINTER(wkeWindowFeatures)))
    def _wkeCreateViewCallback(self,webview,param,navigationType,url,windowFeatures):
        #调用了window.open或者点击了<a target="_blank" .../>弹出新窗口回调
        #要开启弹出新窗口才生效
        # 返回0表示不创建新窗口
        if hasattr(self,'wkeCreateViewCallback'):
            url=self.mb.wkeGetStringW(url)
            param=self.get_param_value(param)
            return self.wkeCreateViewCallback(webview=webview,param=param,navigationType=navigationType,url=url,windowFeatures=windowFeatures)
        return 0
    @method(CFUNCTYPE(None, _LRESULT, c_void_p,c_int,c_void_p))
    def _wkeNavigationCallback(self,webview,param,navigationType,url):
        #网页开始浏览 回调函数
        #navigationType 0:LINKCLICK,1:FORMSUBMITTE,2:BACKFORWARD,
        #3:RELOAD,4:FORMRESUBMITT,5:OTHER
        if hasattr(self,'wkeNavigationCallback'):
            url=self.mb.wkeGetStringW(url)
            param=self.get_param_value(param)
            self.wkeNavigationCallback(webview=webview,param=param,navigationType=navigationType,url=url)
    @method(CFUNCTYPE(None, _LRESULT, c_void_p, c_void_p))
    def _wkeTitleChangedCallback(self,webview, param, title):
        if hasattr(self,'wkeTitleChangedCallback'):
            title=self.mb.wkeGetStringW(title)
            param=self.get_param_value(param)
            self.wkeTitleChangedCallback(webview=webview, param=param, title=title)
    @method(CFUNCTYPE(None, _LRESULT, c_void_p, c_void_p))
    def _wkeMouseOverUrlChangedCallback(self,webview, param, url):
        #鼠标滑过url标签
        if hasattr(self,'wkeMouseOverUrlChangedCallback'):
            url=self.mb.wkeGetStringW(url)
            param=self.get_param_value(param)
            self.wkeMouseOverUrlChangedCallback(webview=webview, param=param, url=url)
    @method(CFUNCTYPE(None, _LRESULT, c_void_p,c_int,c_void_p))
    def _wkeURLChangedCallback2(self,webview,param,frameId,url):
        # print(self.mb.wkeGetStringW(url))
        if hasattr(self,'wkeURLChangedCallback2'):
            url=self.mb.wkeGetStringW(url)
            param=self.get_param_value(param)
            self.wkeURLChangedCallback2(webview=webview, param=param,frameId=frameId,url=url)
    @method(CFUNCTYPE(None, _LRESULT, c_void_p,c_void_p))
    def _wkeAlertBoxCallback(self,webview,param,msg):
        #运行这个回调后 alert不再弹出
        #可以用来自定义弹出框
        if hasattr(self,'wkeAlertBoxCallback'):
            msg=self.mb.wkeGetStringW(msg)
            param=self.get_param_value(param)
            self.wkeAlertBoxCallback(webview=webview, param=param,msg=msg)

    @method(CFUNCTYPE(c_bool, _LRESULT, c_void_p,c_void_p))
    def _wkeConfirmBoxCallback(self,webview,param,msg):
        #运行这个回调后 confirm不再弹出
        #可以用来自定义弹出框
        #返回True 表示点击了确认按钮
        #返回False 表示未点击确认按钮
        if hasattr(self,'wkeConfirmBoxCallback'):
            msg=self.mb.wkeGetStringW(msg)
            param=self.get_param_value(param)
            return self.wkeConfirmBoxCallback(webview=webview, param=param,msg=msg)
        return False
    @method(CFUNCTYPE(c_bool, _LRESULT, c_void_p,c_void_p,c_void_p,c_void_p))
    def _wkePromptBoxCallback(self,webview,param,msg,defaultResult,result):
        #运行这个回调后 prompt不再弹出
        #可以用来自定义弹出框
        #提示信息:msg
        #默认值:defaultResult
        #返回值:result
        #返回True执行确认,False不执行
        if hasattr(self,'wkePromptBoxCallback'):
            msg=self.mb.wkeGetStringW(msg)
            defaultResult=self.mb.wkeGetStringW(defaultResult)
            param=self.get_param_value(param)
            return self.wkePromptBoxCallback(webview=webview, param=param,msg=msg,defaultResult=defaultResult,result=result)
        return False
    @method(CFUNCTYPE(None, _LRESULT,c_void_p, c_int,c_void_p,c_void_p,c_ulonglong,c_void_p))
    def _wkeConsoleCallback(self,webview,param,level,msg,sourceName,sourceLine,stackTrace):
        #console
        if hasattr(self,'wkeConsoleCallback'):
            msg=self.mb.wkeGetStringW(msg)
            sourceName=self.mb.wkeGetStringW(sourceName)
            stackTrace=self.mb.wkeGetStringW(stackTrace)
            param=self.get_param_value(param)
            self.wkeConsoleCallback(webview=webview, param=param,level=level,msg=msg,sourceName=sourceName,sourceLine=sourceLine,stackTrace=stackTrace)
    @method(CFUNCTYPE(c_bool,_LRESULT,c_void_p,c_char_p))
    def _wkeDownloadCallback(self,webview,param,url):
        #下载回调
        #获取下载链接 下载自己写(下载最好起一个线程下载)
        #返回True或False没区别
        if hasattr(self,'wkeDownloadCallback'):
            url=url.decode()
            param=self.get_param_value(param)
            self.wkeDownloadCallback(webview=webview, param=param,url=url)
        return True
    @method(CFUNCTYPE(c_bool,_LRESULT,c_void_p,c_char_p,c_void_p))
    def _wkeNetResponseCallback(self,webview,param,url,job):
        #一个网络请求发送后,收到服务器response 回调函数
        #返回True不再访问,False继续访问
        if hasattr(self,'wkeNetResponseCallback'):
            url=url.decode()
            param=self.get_param_value(param)
            return self.wkeNetResponseCallback(webview=webview, param=param,url=url,job=job)
        return False
    @method(CFUNCTYPE(c_bool,_LRESULT,c_void_p,c_char_p,c_void_p))
    def _wkeLoadUrlBeginCallback(self,webview,param,url,job):
        #任何网络网络即将加载 回调函数
        # 运行wkeNetHookRequest方法,wkeOnLoadUrlEnd才生效
        #True表示mb不再发送网络请求,False表示mb依然会发送网络请求
        if hasattr(self,'wkeLoadUrlBeginCallback'):
            url=url.decode()
            param=self.get_param_value(param)
            return self.wkeLoadUrlBeginCallback(webview=webview, param=param,url=url,job=job)
        return False
    @method(CFUNCTYPE(None,_LRESULT,c_void_p,c_char_p,c_void_p,c_void_p,c_int))
    def _wkeLoadUrlEndCallback(self,webview,param,url,job,buf,lens):
        #任何网络加载结束 回调函数
        if hasattr(self,'wkeLoadUrlEndCallback'):
            url=url.decode()
            param=self.get_param_value(param)
            self.wkeLoadUrlEndCallback(webview=webview, param=param,url=url,job=job,buf=buf,lens=lens)
    @method(CFUNCTYPE(None,_LRESULT,c_void_p,c_char_p,c_void_p))
    def _wkeLoadUrlFailCallback(self,webview,param,url,job):
        #网络加载失败 回调函数,一般用在代理失败 重新设置代理
        # if 'about:blank' in url:return
        if hasattr(self,'wkeLoadUrlFailCallback'):
            url=url.decode()
            param=self.get_param_value(param)
            self.wkeLoadUrlFailCallback(webview=webview, param=param,url=url,job=job)
    @method(CFUNCTYPE(None,_LRESULT,c_void_p,c_void_p,c_int,c_void_p))
    def _wkeLoadingFinishCallback(self,webview,param,url,result,failedReason):
        #页面加载完成回调函数
        #result 0:succeed,1:failed,2:canceled
        if hasattr(self,'wkeLoadingFinishCallback'):
            url=self.mb.wkeGetStringW(url)
            failedReason=self.mb.wkeGetStringW(failedReason)
            param=self.get_param_value(param)
            self.wkeLoadingFinishCallback(webview=webview, param=param,url=url,result=result,failedReason=failedReason)
    @method(CFUNCTYPE(None, _LRESULT, c_void_p,c_char_p,POINTER(wkeMemBuf)))
    def _wkeOnNetGetFaviconCallback(self,webview,param,url,buf):
        #获取favicon 回调函数
        #此接口必须在wkeOnLoadingFinish回调里调用
        if hasattr(self,'wkeOnNetGetFaviconCallback'):
            url=url.decode()
            param=self.get_param_value(param)
            self.wkeOnNetGetFaviconCallback(webview=webview, param=param,url=url,buf=buf)







    @method(WINFUNCTYPE(None,HWND, UINT,UINT,DWORD))
    def _timerProc(self,hwnd,msg,nid,dwTime):
        if hasattr(self,'timerProc'):
            self.timerProc(hwnd=hwnd,msg=msg,nid=nid,dwTime=dwTime)

    @method(WINFUNCTYPE(_LRESULT,HWND, UINT,WPARAM,LPARAM))
    def _wkeWndProcCallback(self,hwnd,msg,wParam,lParam):
        if hasattr(self,'wkeWndProcCallback'):
            self.wkeWndProcCallback(hwnd=hwnd,msg=msg,wParam=wParam,lParam=lParam)
        return user32.CallWindowProcW(self.oldWndProc, hwnd, msg, wParam, lParam)



    def param_to_string(self,param):
        if param!=0:
            _type=0
            if isinstance(param,str):
                _type='1'
            elif isinstance(param,int):
                _type='2'
            elif isinstance(param,float):
                _type='3'
            elif isinstance(param,list):
                _type='4'
            elif isinstance(param,tuple):
                _type='5'
                param=list(param)
            elif isinstance(param,dict):
                _type='6'
            else:
                param=0
            if _type in ['4','5','6']:
                param=json.dumps(param)
            if _type!=0:
                param=f'{_type}-|-lochen-119182686-|-{param}'
                param=self.mb.wkeCreateStringW(param,len(param))
        return param
    def get_param_value(self,param):
        if param!=None:
            param_str=self.mb.wkeGetStringW(param)
            ls=param_str.split('-|-lochen-119182686-|-')
            # print(param_str,ls)
            _type=ls[0]
            _param=ls[1]
            if _type=='1':
                ...
            elif _type=='2':
                _param=int(_param)
            elif _type=='3':
                _param=float(_param)
            elif _type in ['4','5','6']:
                _param=json.loads(_param)
            if _type=='5':
                _param=tuple(_param)
            return _param