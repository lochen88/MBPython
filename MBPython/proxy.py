# -*- coding:utf-8 -*-
from ctypes import (
    c_int,
    c_ushort
)
from .wkeStruct import wkeProxy

class Proxy():
    def __init__(self,miniblink):     

        self.mb=miniblink
  
    def wkeSetProxy(self,ip,port,proxy_type=1,user=None,password=None):

        if not all([ip,port]):return
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
        proxy= wkeProxy(type=c_int(proxy_type), hostname=ip, port=c_ushort(port),username=user,password=password)
        self.mb.wkeSetProxy(proxy)
    
    def wkeSetViewProxy(self,webview,ip,port,proxy_type=1,user=None,password=None):
        
        if not all([ip,port]):return
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
        proxy= wkeProxy(type=c_int(proxy_type), hostname=ip, port=c_ushort(port),username=user,password=password)
        self.mb.wkeSetViewProxy(webview,proxy)