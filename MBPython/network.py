# -*- coding:utf-8 -*-
from ctypes import c_char
import binascii
class NetWork():
    def __init__(self,miniblink):     
        self.types=['.jpg','.png','.mp4','.ts','.mp3','.avi','.gif']
        self.bufs=[]
        self.mb=miniblink
    def wkeLoadURLW(self,webview,url):
        self.mb.wkeLoadURLW(webview,url)
    def wkeLoadHTMLW(self,webview,html):
        self.mb.wkeLoadHTMLW(webview,html)
    def wkeLoadFile(self,webview,file_path):
        file_path=file_path.encode()
        self.mb.wkeLoadFile(webview,file_path)
    def wkePostURLW(self,webview,url,data):
        data=data.encode()
        lens=len(data)
        self.mb.wkeLoadURLW(webview,data,lens)
    def wkeReload(self,webview):
        self.mb.wkeReload(webview)
    def wkeStopLoading(self,webview):
        self.mb.wkeStopLoading(webview)
    def wkeGetURL(self,webview):
        url=self.mb.wkeGetURL(webview)
        return url.decode()
    def wkeGetFrameUrl(self,webview,frameId):
        url=self.mb.wkeGetFrameUrl(webview,frameId)
        return url.decode('utf8')  
    def wkeGetSource(self,webview):
        source=self.mb.wkeGetSource(webview)
        return source.decode()
    def wkeUtilSerializeToMHTML(self,webview):
        mhtml_content=self.mb.wkeUtilSerializeToMHTML(webview)
 
        return mhtml_content
    def get_type(self,url):
        for x in self.types:
            if x in url:
                return x
        return    
 
    def save_buf_data(self,url,buf,lens):
   
        if lens==0:return
        contents=(c_char * lens).from_address(buf)
        _type=self.get_type(url)
        if _type==None:return
        name=binascii.crc32(url.encode())
        file_name=f'{name}{_type}'
        try:
            with open(file_name,'wb') as f:
                f.write(contents)
            self.bufs.append({url:file_name})
        except:
            ...
        finally:
            ...
 
    def cancel_request(self,job,url,ident_ls=['.jpg']):

        for x in ident_ls:
            if  x in url:
                self.mb.wkeNetCancelRequest(job)
                return True
        return False
    def set_response_data(self,job,data='',file_name=None):

        lens=len(data)
        if lens!=0:
            self.mb.wkeNetSetData(job,data,lens)
            return True
        elif file_name!=None:
            with open(file_name) as f:
                data=f.read()
                data=data.encode()
                lens=len(data)
            if lens!=0:
                if '.js' in file_name:
                    self.mb.wkeNetSetMIMEType(job,b'text/javascript')
                elif '.html' in file_name:
                    self.mb.wkeNetSetMIMEType(job,b'text/html')
                self.mb.wkeNetSetData(job,data,lens)
                return True
        return False    
   
    def get_post_data(self,job,url,ident=''):
        
        if ident not in url:return '',0,None
        elements=self.mb.wkeNetGetPostBody(job)
        try:
            data=elements.contents.element.contents.contents.data.contents.data
            lens=elements.contents.element.contents.contents.data.contents.length
        except:
            return '',0,None
        data=data[:lens].decode('utf8','ignore')
        print('post_data',data,lens)
        return data,lens,elements