# -*- coding:utf-8 -*-

from ctypes import (
    CFUNCTYPE,
    c_longlong,
    c_float,
    c_void_p,
    c_wchar_p
)
from .method import method
from . import _LRESULT

class JsRunPy():
    def __init__(self,miniblink):

        self.mb=miniblink

    def get_js_args_val(self,es,arg_count):
        val_ls=[None]*arg_count
        for i in range(arg_count):

            arg_type=self.mb.jsArgType(es,i)
            
            if arg_type==0:
                val=self.mb.jsArg(es,i)
                val=self.mb.jsToInt(es, c_longlong(val))
            elif arg_type==1:
                val=self.mb.jsArg(es,i)
                val=self.mb.jsToTempStringW(es, c_longlong(val))            
            elif arg_type==2:
                val=self.mb.jsArg(es,i)
                val=self.mb.jsToTempStringW(es, c_longlong(val))
                if val=='false':
                    val=False
                else:
                    val=True
           
            elif arg_type==5 or arg_type==7:
                val=None
            elif arg_type==6:
         
                val=self.mb.jsArg(es,i)
                lens=self.mb.jsGetLength(es,c_longlong(val))
                tmp_arr=[None]*lens
                for j in range(lens):
                    tmp_val=self.mb.jsGetAt(es,c_longlong(val),j)            
                    if self.mb.jsIsNumber(tmp_val)==1:
                        tmp_val=self.mb.jsToInt(es, c_longlong(tmp_val))
                    elif self.mb.jsIsString(tmp_val)==1:
                        tmp_val=self.mb.jsToTempStringW(es, c_longlong(tmp_val))
                        tmp_val=c_wchar_p(tmp_val).value
                    elif self.mb.jsIsBoolean(tmp_val)==1:
                        tmp_val=self.mb.jsToTempStringW(es, c_longlong(tmp_val))
                        if tmp_val=='false':
                            tmp_val=False
                        else:
                            tmp_val=True
                    tmp_arr[j]=tmp_val
                val=tmp_arr
            else:
                val=self.mb.jsArg(es,i)
                val=self.mb.jsToTempStringW(es, c_longlong(val))
            val_ls[i]=val
      
        return val_ls
  
    def to_js_args_val(self,es,val):

        if isinstance(val,str):
            val=self.mb.jsStringW(es,val)
        elif isinstance(val,int):
            val=self.mb.jsInt(val)
        elif isinstance(val,float):
            val=self.mb.jsFloat(val)
        elif isinstance(val,bool):
            val=self.mb.jsBoolean(val)

        elif isinstance(val,list):
            lens=len(val)
            tmp_arr=self.mb.jsEmptyArray(es)
            for i in range(lens):
                if isinstance(val[i],int):
                    tmp_val=self.mb.jsInt(val[i])
                elif isinstance(val[i],str):
                    tmp_val=self.mb.jsStringW(es,val[i])
                elif isinstance(val[i],float):
                    tmp_val=self.mb.jsFloat(c_float(val[i]))
                self.mb.jsSetAt(es, c_longlong(tmp_arr), i, c_longlong(tmp_val))
            val=tmp_arr
        elif isinstance(val,dict): 
            tmp_obj=self.mb.jsEmptyObject(es)
            for k,v in val.items():
                if isinstance(v,int):
                    v=self.mb.jsInt(v)
                elif isinstance(v,str):
                    v=self.mb.jsStringW(es,v)
                elif isinstance(v,float):
                    v=self.mb.jsFloat(c_float(v))
                self.mb.jsSet(es,c_longlong(tmp_obj),k.encode(),c_longlong(v))
            val=tmp_obj
        return val
 
    def bind_func(self,func_name,arg_count=0,param=0):
        js_bind_func=getattr(self,func_name)
        func_name=func_name.encode()
        self.mb.wkeJsBindFunction(func_name,js_bind_func,param,arg_count)   

    @method(CFUNCTYPE(c_longlong, _LRESULT, c_void_p))
    def call_py_func(self,es,param):

        if hasattr(self,'python_func'):
            return self.python_func(es=es,param=param)
        return 0