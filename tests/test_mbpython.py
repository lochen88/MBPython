# -*- coding:utf-8 -*-
import os
import sys
from pathlib import Path
current_folder = Path(__file__).absolute().parent
father_folder = str(current_folder.parent)
os.chdir(str(current_folder))
sys.path.append(father_folder)


from MBPython import miniblink 

def test():   
    wke=miniblink.MiniBlink
    mb=wke.init()
    if mb==0:return
    window=wke.window
    callback=wke.callback
    network=wke.network

    webview=window.wkeCreateWebWindow(0,0,0,0,860,760)
    callback.wkeOnWindowDestroy(webview)

    network.wkeLoadURLW(webview,'https://www.baidu.com/')

    window.wkeShowWindow(webview)
    
    window.wkeRunMessageLoop()

if __name__=='__main__':
    test()
    ...
