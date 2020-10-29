# -*- coding:utf-8 -*-
from ctypes import (
    c_int,
    c_ulonglong,
    c_char_p,
    c_bool,
    c_void_p,
    POINTER,
    windll,
    CFUNCTYPE
)
from .winConst import WinConst
from .wkeStruct import (wkeRect,wkeWindowFeatures,wkeMemBuf,mPos)
from .method import method
from . import _LRESULT
import json

user32=windll.user32
class CallBack():
    def __init__(self,miniblink,width=360,height=480):
        self.mb=miniblink
        self.width=width
        self.height=height
    def wkeOnCreateView(self,webview,param=0):
        param=self.param_to_string(param)
        self.mb.wkeOnCreateView(webview,self._wkeCreateViewCallback,_LRESULT(param))
    def wkeOnWindowClosing(self,webview,param=0):
        param=self.param_to_string(param)
        self.mb.wkeOnWindowClosing(webview,self._wkeWindowClosingCallback,_LRESULT(param))
    def wkeOnWindowDestroy(self,webview,param=0):
 
        self.mb.wkeOnWindowDestroy(webview,self._wkeWindowDestroyCallback,_LRESULT(param))
    def wkeOnPaintUpdated(self,webview,param=0):
        param=self.param_to_string(param)
        self.mb.wkeOnPaintUpdated(webview,self._wkePaintUpdatedCallback ,_LRESULT(param))
    def wkeOnPaintBitUpdated(self,webview,param=0):
        param=self.param_to_string(param)
        self.mb.wkeOnPaintBitUpdated(webview, self._wkePaintBitUpdatedCallback,_LRESULT(param))
    def wkeOnNavigation(self,webview,param=0):
        param=self.param_to_string(param)
        self.mb.wkeOnNavigation(webview,self._wkeNavigationCallback,_LRESULT(param))
    def wkeOnTitleChanged(self,webview,param=0):
        param=self.param_to_string(param)
        self.mb.wkeOnTitleChanged(webview,self._wkeTitleChangedCallback,_LRESULT(param))
    def wkeOnURLChanged2(self,webview,param=0):
        param=self.param_to_string(param)
        self.mb.wkeOnURLChanged2(webview,self._wkeURLChangedCallback2,_LRESULT(param))
    def wkeOnMouseOverUrlChanged(self,webview,param=0):
        param=self.param_to_string(param)
        self.mb.wkeOnMouseOverUrlChanged(webview,self._wkeMouseOverUrlChangedCallback,_LRESULT(param))
    def wkeOnAlertBox(self,webview,param=0):
        param=self.param_to_string(param)
        self.mb.wkeOnAlertBox(webview,self._wkeAlertBoxCallback,_LRESULT(param))
    def wkeOnConfirmBox(self,webview,param=0):
        param=self.param_to_string(param)
        self.mb.wkeOnConfirmBox(webview,self._wkeConfirmBoxCallback,_LRESULT(param))
    def wkeOnPromptBox(self,webview,param=0):
        param=self.param_to_string(param)
        self.mb.wkeOnPromptBox(webview,self._wkePromptBoxCallback,_LRESULT(param))
    def wkeOnConsole(self,webview,param=0):
        self.mb.wkeOnConsole(webview,self._wkeConsoleCallback,_LRESULT(param))
    def wkeOnDownload(self,webview,param=0):
        param=self.param_to_string(param)
        self.mb.wkeOnDownload(webview,self._wkeDownloadCallback,_LRESULT(param))
    def wkeOnDocumentReady2(self,webview,param=0):
        param=self.param_to_string(param)
        self.mb.wkeOnDocumentReady2(webview,self._wkeDocumentReady2Callback,_LRESULT(param))
    def wkeNetOnResponse(self,webview,param=0):
        param=self.param_to_string(param)
        self.mb.wkeNetOnResponse(webview,self._wkeNetResponseCallback,_LRESULT(param))
    def wkeOnLoadUrlBegin(self,webview,param=0):
        param=self.param_to_string(param)
        self.mb.wkeOnLoadUrlBegin(webview,self._wkeLoadUrlBeginCallback,_LRESULT(param))
    def wkeOnLoadUrlEnd(self,webview,param=0):
        param=self.param_to_string(param)
        self.mb.wkeOnLoadUrlEnd(webview,self._wkeLoadUrlEndCallback,_LRESULT(param))
    def wkeOnLoadUrlFail(self,webview,param=0):
        param=self.param_to_string(param)
        self.mb.wkeOnLoadUrlFail(webview,self._wkeLoadUrlFailCallback,_LRESULT(param))
    def wkeOnLoadingFinish(self,webview,param=0):
        param=self.param_to_string(param)
        self.mb.wkeOnLoadingFinish(webview,self._wkeLoadingFinishCallback,_LRESULT(param))
    def wkeNetGetFavicon(self,webview,param=0):
        param=self.param_to_string(param)
        self.mb.wkeNetGetFavicon(webview,self._wkeOnNetGetFaviconCallback,_LRESULT(param))







    @method(CFUNCTYPE(c_bool, _LRESULT, c_void_p))
    def _wkeWindowClosingCallback(self,webview, param):

        if hasattr(self,'wkeWindowClosingCallback'):
            param=self.get_param_value(param)
            return self.wkeWindowClosingCallback(webview=webview,param=param)
        return True
    @method(CFUNCTYPE(None, _LRESULT, c_void_p))
    def _wkeWindowDestroyCallback(self,webview, param):
        if hasattr(self,'wkeWindowDestroyCallback'):
            param=self.get_param_value(param)
            self.wkeWindowDestroyCallback(webview=webview,param=param)
        user32.PostQuitMessage(0)
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

        if hasattr(self,'wkeCreateViewCallback'):
            url=self.mb.wkeGetStringW(url)
            param=self.get_param_value(param)
            return self.wkeCreateViewCallback(webview=webview,param=param,navigationType=navigationType,url=url,windowFeatures=windowFeatures)
        return 0
    @method(CFUNCTYPE(None, _LRESULT, c_void_p,c_int,c_void_p))
    def _wkeNavigationCallback(self,webview,param,navigationType,url):
  
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

        if hasattr(self,'wkeMouseOverUrlChangedCallback'):
            url=self.mb.wkeGetStringW(url)
            param=self.get_param_value(param)
            self.wkeMouseOverUrlChangedCallback(webview=webview, param=param, url=url)
    @method(CFUNCTYPE(None, _LRESULT, c_void_p,c_int,c_void_p))
    def _wkeURLChangedCallback2(self,webview,param,frameId,url):
  
        if hasattr(self,'wkeURLChangedCallback2'):
            url=self.mb.wkeGetStringW(url)
            param=self.get_param_value(param)
            self.wkeURLChangedCallback2(webview=webview, param=param,frameId=frameId,url=url)
    @method(CFUNCTYPE(None, _LRESULT, c_void_p,c_void_p))
    def _wkeAlertBoxCallback(self,webview,param,msg):
  
        if hasattr(self,'wkeAlertBoxCallback'):
            msg=self.mb.wkeGetStringW(msg)
            param=self.get_param_value(param)
            self.wkeAlertBoxCallback(webview=webview, param=param,msg=msg)

    @method(CFUNCTYPE(c_bool, _LRESULT, c_void_p,c_void_p))
    def _wkeConfirmBoxCallback(self,webview,param,msg):
   
        if hasattr(self,'wkeConfirmBoxCallback'):
            msg=self.mb.wkeGetStringW(msg)
            param=self.get_param_value(param)
            return self.wkeConfirmBoxCallback(webview=webview, param=param,msg=msg)
        return False
    @method(CFUNCTYPE(c_bool, _LRESULT, c_void_p,c_void_p,c_void_p,c_void_p))
    def _wkePromptBoxCallback(self,webview,param,msg,defaultResult,result):
    
        if hasattr(self,'wkePromptBoxCallback'):
            msg=self.mb.wkeGetStringW(msg)
            defaultResult=self.mb.wkeGetStringW(defaultResult)
            param=self.get_param_value(param)
            return self.wkePromptBoxCallback(webview=webview, param=param,msg=msg,defaultResult=defaultResult,result=result)
        return False
    @method(CFUNCTYPE(None, _LRESULT,c_void_p, c_int,c_void_p,c_void_p,c_ulonglong,c_void_p))
    def _wkeConsoleCallback(self,webview,param,level,msg,sourceName,sourceLine,stackTrace):

        if hasattr(self,'wkeConsoleCallback'):
            msg=self.mb.wkeGetStringW(msg)
            sourceName=self.mb.wkeGetStringW(sourceName)
            stackTrace=self.mb.wkeGetStringW(stackTrace)
            param=self.get_param_value(param)
            self.wkeConsoleCallback(webview=webview, param=param,level=level,msg=msg,sourceName=sourceName,sourceLine=sourceLine,stackTrace=stackTrace)
    @method(CFUNCTYPE(c_bool,_LRESULT,c_void_p,c_char_p))
    def _wkeDownloadCallback(self,webview,param,url):

        if hasattr(self,'wkeDownloadCallback'):
            url=url.decode()
            param=self.get_param_value(param)
            self.wkeDownloadCallback(webview=webview, param=param,url=url)
        return True
    @method(CFUNCTYPE(c_bool,_LRESULT,c_void_p,c_char_p,c_void_p))
    def _wkeNetResponseCallback(self,webview,param,url,job):
    
        if hasattr(self,'wkeNetResponseCallback'):
            url=url.decode()
            param=self.get_param_value(param)
            return self.wkeNetResponseCallback(webview=webview, param=param,url=url,job=job)
        return False
    @method(CFUNCTYPE(c_bool,_LRESULT,c_void_p,c_char_p,c_void_p))
    def _wkeLoadUrlBeginCallback(self,webview,param,url,job):

        if hasattr(self,'wkeLoadUrlBeginCallback'):
            url=url.decode()
            param=self.get_param_value(param)
            return self.wkeLoadUrlBeginCallback(webview=webview, param=param,url=url,job=job)
        return False
    @method(CFUNCTYPE(None,_LRESULT,c_void_p,c_char_p,c_void_p,c_void_p,c_int))
    def _wkeLoadUrlEndCallback(self,webview,param,url,job,buf,lens):
        if hasattr(self,'wkeLoadUrlEndCallback'):
            url=url.decode()
            param=self.get_param_value(param)
            self.wkeLoadUrlEndCallback(webview=webview, param=param,url=url,job=job,buf=buf,lens=lens)
    @method(CFUNCTYPE(None,_LRESULT,c_void_p,c_char_p,c_void_p))
    def _wkeLoadUrlFailCallback(self,webview,param,url,job):
        if hasattr(self,'wkeLoadUrlFailCallback'):
            url=url.decode()
            param=self.get_param_value(param)
            self.wkeLoadUrlFailCallback(webview=webview, param=param,url=url,job=job)
    @method(CFUNCTYPE(None,_LRESULT,c_void_p,c_void_p,c_int,c_void_p))
    def _wkeLoadingFinishCallback(self,webview,param,url,result,failedReason):
        if hasattr(self,'wkeLoadingFinishCallback'):
            url=self.mb.wkeGetStringW(url)
            if result==1:
                failedReason=self.mb.wkeGetStringW(failedReason)
            param=self.get_param_value(param)
            self.wkeLoadingFinishCallback(webview=webview, param=param,url=url,result=result,failedReason=failedReason)
    @method(CFUNCTYPE(None, _LRESULT, c_void_p,c_char_p,POINTER(wkeMemBuf)))
    def _wkeOnNetGetFaviconCallback(self,webview,param,url,buf):
        if hasattr(self,'wkeOnNetGetFaviconCallback'):
            url=url.decode()
            param=self.get_param_value(param)
            self.wkeOnNetGetFaviconCallback(webview=webview, param=param,url=url,buf=buf)







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
