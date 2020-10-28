# -*- coding:utf-8 -*-
from ctypes import (c_longlong,byref)
from .method import method


class PyRunJS():
    def __init__(self,miniblink):

        self.mb=miniblink
  
    def run_js(self,webview,js_code):

        es=self.mb.wkeGlobalExec(webview)
        val=self.mb.wkeRunJSW(webview,js_code)
        val=self.mb.jsToStringW(es,val)
        if val=='undefined':
            val=None
        return val
  
    def run_js_file(self,webview,file_name):
        with open(file_name) as f:
            js_code=f.read()
            return self.run_js(webview,js_code)        
    def run_js_byframe(self,webview,frameId,js_code,isInClosure=True):
        
        js_code=js_code.encode()
        val=self.mb.wkeRunJsByFrame(webview,frameId,js_code,isInClosure)
        es = self.mb.wkeGetGlobalExecByFrame(webview, frameId)
        val=self.mb.jsToTempStringW(es, c_longlong(val))
        return val
 
    def run_js_global(self,webview,func_name,param_ls=[],this_func=0):
       
        es=self.mb.wkeGlobalExec(webview)
        if this_func==0:
            func_name=func_name.encode()
            func=self.mb.jsGetGlobal(es,func_name)
        else:
            ...
        argCount=len(param_ls)
        args_ls=(c_longlong *argCount)()

        for i,param in enumerate(param_ls):
            if isinstance(param,str):
                param=self.mb.jsStringW(es,param)
            elif isinstance(param,int):
                param=self.mb.jsInt(c_longlong(param))
            elif isinstance(param,float):
                param=self.mb.jsFloat(param)
            elif isinstance(param,bool):
                param=self.mb.jsBoolean(param)
            args_ls[i]=param

        callRet=self.mb.jsCall(es,c_longlong(func),c_longlong(this_func),byref(args_ls),c_longlong(argCount))
        val=self.mb.jsToStringW(es,c_longlong(callRet))
        return val        