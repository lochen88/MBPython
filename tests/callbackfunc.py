
from ctypes import c_char_p
class callBackTest():
    def __init__(self,miniblink,runjs,callback,network):
        self.mb=miniblink
        self.js=runjs
        self.cb=callback
        self.network=network
    def document_ready_func(self,**kwargs):
        webview=kwargs['webview']
        param=kwargs['param']
        frameId=kwargs['frameId']
        url=self.mb.wkeGetFrameUrl(webview,frameId).decode()
        if 'about:blank' in url:return
        if self.mb.wkeIsDocumentReady(webview)!=0:
            print('wkeDocumentReady2Callback',frameId,param,url)
            self.test_js(webview=webview,frameId=frameId)
    def test_js(self,webview,frameId=1):
        # self.js.run_js(webview,js_code='return 1+1')
        # self.js.run_js(webview, js_code='return document.body.innerHTML')
        # self.js.run_js(webview, js_code='return window.parent.frames["contentFrame"].document.getElementsByClassName("m-cvrlst f-cb")[0].innerHTML')
        # self.js.run_js(webview, js_code='return document.getElementById("testiframe").contentWindow.document.body.innerHTML')
        # self.js.run_js(webview, js_code='document.write(666)')
        # self.js.run_js(webview, js_code='return 1+1.1')
        # self.js.run_js(webview, js_code='return PyRunJS("hi"," baby")')
        # self.js.run_js_byframe(webview, frameId, 'return document.body.innerHTML', isInClosure=True)
        # self.js.run_js_global(webview,'globaljs',['good'])
        ...


