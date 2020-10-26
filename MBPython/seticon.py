# -*- coding:utf-8 -*-
from ctypes import windll
from .winConst import WinConst
from os import path

user32 = windll.user32
kernel32= windll.kernel32
RelPath = lambda file : path.join(path.dirname(path.abspath(__file__)), file)

def set_icon(hwnd, filename):
    if not filename.endswith('.ico'):
        return False
    hModel = kernel32.GetModuleHandleW(None)
    hIcon = user32.LoadImageW(hModel,RelPath(filename),WinConst.IMAGE_ICON,48, 48,WinConst.LR_LOADFROMFILE | WinConst.LR_CREATEDIBSECTION)
    user32.SendMessageW(hwnd, WinConst.WM_SETICON, WinConst.ICON_BIG, hIcon)
    return True
def set_icon_2(hwnd,filename):
    if not filename.endswith('.ico'):
        return False
    import win32api
    import win32gui
    icon_big = win32gui.LoadImage(
        None, RelPath(filename), WinConst.IMAGE_ICON,
        48, 48, WinConst.LR_LOADFROMFILE)
    win32api.SendMessage(hwnd, WinConst.WM_SETICON,WinConst.ICON_BIG, icon_big)
    return True
