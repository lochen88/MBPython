# -*- coding:utf-8 -*-

from .pyrunjs import PyRunJS
class Cookie():
    def __init__(self,miniblink):        
        self.mb=miniblink
        self.js=PyRunJS(miniblink)
    def wkeGetCookieW(self,webview):

        return self.mb.wkeGetCookieW(webview)

    def wkeSetCookie(self,webview,url,cookie):

        cookie=cookie.split(';')
        for x in cookie:
            self.mb.wkeSetCookie(webview,url.encode('utf8'),x.encode('utf8'))
 
        self.mb.wkePerformCookieCommand(webview,2)

    def set_cookie_by_js(self,webview,url,cookie):
       
        js_code=f"var cookie='{cookie}';"+'''
        cookie.split(';').forEach(function(e){
        document.cookie=e
        })'''
        self.js.run_js(webview,js_code)
       
        self.mb.wkeLoadURLW(webview, url)
 
    def wkeSetCookieJarPath(self,webview,path):
        
        self.mb.wkeSetCookieJarPath(webview,path)
   
    def wkeSetCookieJarFullPath(self,webview,path):
      
        self.mb.wkeSetCookieJarFullPath(webview,path)
    
    def wkeClearCookie(self,webview):

        self.mb.wkeClearCookie(webview)