# -*- coding:utf-8 -*-
from .winConst import *
from .myctypes import *
from .wkeStruct import (wkeRect,wkeWindowFeatures,wkeMemBuf)
from .method import method
from .defaultcallbackfunc import destroy_func
from config import _LRESULT

class CallBack():
    def __init__(self,miniblink,width=360,height=480):
        self.mb=miniblink  
        self.width=width
        self.height=height
        self.wkeWindowDestroyCallback=destroy_func

    def wkeOnCreateView(self,webview,param=0):
        self.mb.wkeOnCreateView(webview,self._wkeCreateViewCallback,param)
    def wkeOnWindowClosing(self,webview,param=0):
        self.mb.wkeOnWindowClosing(webview,self._wkeWindowClosingCallback,param)
    def wkeOnWindowDestroy(self,webview,param=0):
        self.mb.wkeOnWindowDestroy(webview,self._wkeWindowDestroyCallback,param)
    def wkeOnPaintUpdated(self,webview,param=0):
        self.mb.wkeOnPaintUpdated(webview,self._wkePaintUpdatedCallback ,param)
    def wkeOnPaintBitUpdated(self,webview,param=0):
        self.mb.wkeOnPaintBitUpdated(webview, self._wkePaintBitUpdatedCallback,param)
    def wkeOnNavigation(self,webview,param=0):
        self.mb.wkeOnNavigation(webview,self._wkeNavigationCallback,param)
    def wkeOnTitleChanged(self,webview,param=0):
        self.mb.wkeOnTitleChanged(webview,self._wkeTitleChangedCallback,param)
    def wkeOnURLChanged2(self,webview,param=0):
        self.mb.wkeOnURLChanged2(webview,self._wkeURLChangedCallback2,param)
    def wkeOnMouseOverUrlChanged(self,webview,param=0):
        self.mb.wkeOnMouseOverUrlChanged(webview,self._wkeMouseOverUrlChangedCallback,param)
    def wkeOnAlertBox(self,webview,param=0):
        self.mb.wkeOnAlertBox(webview,self._wkeAlertBoxCallback,param)
    def wkeOnConfirmBox(self,webview,param=0):
        self.mb.wkeOnConfirmBox(webview,self._wkeConfirmBoxCallback,param)
    def wkeOnPromptBox(self,webview,param=0):
        self.mb.wkeOnPromptBox(webview,self._wkePromptBoxCallback,param)
    def wkeOnConsole(self,webview,param=0):
        self.mb.wkeOnConsole(webview,self._wkeConsoleCallback,param)
    def wkeOnDownload(self,webview,param=0):
        self.mb.wkeOnDownload(webview,self._wkeDownloadCallback,param)
    def wkeOnDocumentReady2(self,webview,param=0):
        self.mb.wkeOnDocumentReady2(webview,self._wkeDocumentReady2Callback,param)
    def wkeNetOnResponse(self,webview,param=0):
        self.mb.wkeNetOnResponse(webview,self._wkeNetResponseCallback,param)
    def wkeOnLoadUrlBegin(self,webview,param=0):
        self.mb.wkeOnLoadUrlBegin(webview,self._wkeLoadUrlBeginCallback,param)
    def wkeOnLoadUrlEnd(self,webview,param=0):
        self.mb.wkeOnLoadUrlEnd(webview,self._wkeLoadUrlEndCallback,param)
    def wkeOnLoadUrlFail(self,webview,param=0):
        self.mb.wkeOnLoadUrlFail(webview,self._wkeLoadUrlFailCallback,param)
    def wkeOnLoadingFinish(self,webview,param=0):
        self.mb.wkeOnLoadingFinish(webview,self._wkeLoadingFinishCallback,param)
    def wkeNetGetFavicon(self,webview,param=0):
        self.mb.wkeNetGetFavicon(webview,self._wkeOnNetGetFaviconCallback,param)

    @method(CFUNCTYPE(c_bool, _LRESULT, c_void_p))
    def _wkeWindowClosingCallback(self,webview, param):
        if hasattr(self,'wkeWindowClosingCallback'):
            return self.wkeWindowClosingCallback(webview=webview,param=param)
        return True
    @method(CFUNCTYPE(None, _LRESULT, c_void_p))
    def _wkeWindowDestroyCallback(self,webview, param):
        if hasattr(self,'wkeWindowDestroyCallback'):
            self.wkeWindowDestroyCallback(webview=webview,param=param)
    @method(CFUNCTYPE(None,_LRESULT,c_void_p,_LRESULT,c_int,c_int,c_int,c_int))
    def _wkePaintUpdatedCallback(self,webview,param,hdc,x,y,cx,cy):
        if hasattr(self,'wkePaintUpdatedCallback'):
            return self.wkePaintUpdatedCallback(webview=webview,param=param,hdc=hdc,x=x,y=y,cx=cx,cy=cy)
    @method(CFUNCTYPE(None,_LRESULT,c_void_p,_LRESULT,POINTER(wkeRect),c_int,c_int))
    def _wkePaintBitUpdatedCallback(self,webview,param,buf,rect,width,height):
        if hasattr(self,'wkePaintBitUpdatedCallback'):
            return self.wkePaintBitUpdatedCallback(webview=webview,param=param,buf=buf,rect=rect,width=width,height=height)  
    @method(CFUNCTYPE(None,_LRESULT,c_void_p,c_void_p))
    def _wkeDocumentReady2Callback(self,webview,param,frameId):
        if hasattr(self,'wkeDocumentReady2Callback'):
            return self.wkeDocumentReady2Callback(webview=webview,param=param,frameId=frameId)
    @method(CFUNCTYPE(_LRESULT, _LRESULT, c_void_p,c_int,c_void_p,POINTER(wkeWindowFeatures)))
    def _wkeCreateViewCallback(self,webview,param,navigationType,url,windowFeatures):

        if hasattr(self,'wkeCreateViewCallback'):
            return self.wkeCreateViewCallback(webview=webview,param=param,navigationType=navigationType,url=url,windowFeatures=windowFeatures)
        return 0
    @method(CFUNCTYPE(None, _LRESULT, c_void_p,c_int,c_void_p))
    def _wkeNavigationCallback(self,webview,param,navigationType,url):

        if hasattr(self,'wkeNavigationCallback'):
            return self.wkeNavigationCallback(webview=webview,param=param,navigationType=navigationType,url=url)
    @method(CFUNCTYPE(None, _LRESULT, c_void_p, c_void_p))
    def _wkeTitleChangedCallback(self,webview, param, title):
        if hasattr(self,'wkeTitleChangedCallback'):
            return self.wkeTitleChangedCallback(webview=webview, param=param, title=title)
    @method(CFUNCTYPE(None, _LRESULT, c_void_p, c_void_p))
    def _wkeMouseOverUrlChangedCallback(self,webview, param, url):
 
        if hasattr(self,'wkeMouseOverUrlChangedCallback'):
            return self.wkeMouseOverUrlChangedCallback(webview=webview, param=param, url=url)
    @method(CFUNCTYPE(None, _LRESULT, c_void_p,c_int,c_void_p))
    def _wkeURLChangedCallback2(self,webview,param,frameId,url):
        if hasattr(self,'wkeURLChangedCallback2'):
            return self.wkeURLChangedCallback2(webview=webview, param=param,frameId=frameId,url=url)
    @method(CFUNCTYPE(None, _LRESULT, c_void_p,c_void_p))
    def _wkeAlertBoxCallback(self,webview,param,msg):

        if hasattr(self,'wkeAlertBoxCallback'):
            return self.wkeAlertBoxCallback(webview=webview, param=param,msg=msg)

    @method(CFUNCTYPE(c_bool, _LRESULT, c_void_p,c_void_p))
    def _wkeConfirmBoxCallback(self,webview,param,msg):

        if hasattr(self,'wkeConfirmBoxCallback'):
            return self.wkeConfirmBoxCallback(webview=webview, param=param,msg=msg)
        return False
    @method(CFUNCTYPE(c_bool, _LRESULT, c_void_p,c_void_p,c_void_p,c_void_p))
    def _wkePromptBoxCallback(self,webview,param,msg,defaultResult,result):

        if hasattr(self,'wkePromptBoxCallback'):
            return self.wkePromptBoxCallback(webview=webview, param=param,msg=msg,defaultResult=defaultResult,result=result)
        return False
    @method(CFUNCTYPE(None, _LRESULT,c_void_p, c_int,c_void_p,c_void_p,c_ulonglong,c_void_p))
    def _wkeConsoleCallback(self,webview,param,level,msg,sourceName,sourceLine,stackTrace):

        if hasattr(self,'wkeConsoleCallback'):
            return self.wkeConsoleCallback(webview=webview, param=param,level=level,msg=msg,sourceName=sourceName,sourceLine=sourceLine,stackTrace=stackTrace)
    @method(CFUNCTYPE(c_bool,_LRESULT,c_void_p,c_char_p))
    def _wkeDownloadCallback(self,webview,param,url):

        if hasattr(self,'wkeDownloadCallback'):
            self.wkeDownloadCallback(webview=webview, param=param,url=url)
        return True
    @method(CFUNCTYPE(c_bool,_LRESULT,c_void_p,c_char_p,c_void_p))
    def _wkeNetResponseCallback(self,webview,param,url,job):
    
        if hasattr(self,'wkeNetResponseCallback'):
            return self.wkeNetResponseCallback(webview=webview, param=param,url=url,job=job)
        return False
    @method(CFUNCTYPE(c_bool,_LRESULT,c_void_p,c_char_p,c_void_p))
    def _wkeLoadUrlBeginCallback(self,webview,param,url,job):

        if hasattr(self,'wkeLoadUrlBeginCallback'):
            return self.wkeLoadUrlBeginCallback(webview=webview, param=param,url=url,job=job)
        return False
    @method(CFUNCTYPE(None,_LRESULT,c_void_p,c_char_p,c_void_p,c_void_p,c_int))
    def _wkeLoadUrlEndCallback(self,webview,param,url,job,buf,lens):
    
        if hasattr(self,'wkeLoadUrlEndCallback'):
            return self.wkeLoadUrlEndCallback(webview=webview, param=param,url=url,job=job,buf=buf,lens=lens)
    @method(CFUNCTYPE(None,_LRESULT,c_void_p,c_char_p,c_void_p))
    def _wkeLoadUrlFailCallback(self,webview,param,url,job):

        if hasattr(self,'wkeLoadUrlFailCallback'):
            return self.wkeLoadUrlFailCallback(webview=webview, param=param,url=url,job=job)
    @method(CFUNCTYPE(None,_LRESULT,c_void_p,c_void_p,c_int,c_void_p))
    def _wkeLoadingFinishCallback(self,webview,param,url,result,failedReason):
 
        if hasattr(self,'wkeLoadingFinishCallback'):
            return self.wkeLoadingFinishCallback(webview=webview, param=param,url=url,result=result,failedReason=failedReason)
    @method(CFUNCTYPE(None, _LRESULT, c_void_p,c_char_p,POINTER(wkeMemBuf)))
    def _wkeOnNetGetFaviconCallback(self,webview,param,url,buf):
  
        if hasattr(self,'wkeOnNetGetFaviconCallback'):
            return self.wkeOnNetGetFaviconCallback(webview=webview, param=param,url=url,buf=buf)
    

    @method(WINFUNCTYPE(None,HWND, UINT,UINT,DWORD))
    def _timerProc(self,hwnd,msg,nid,dwTime):
        return self.timerProc(hwnd=hwnd,msg=msg,nid=nid,dwTime=dwTime)
