# -*- coding:utf-8 -*-
from ctypes import windll
from .winConst import WinConst
import win32gui, win32ui
from struct import pack
import collections
import zlib


user32=windll.user32
def to_png(data, size, level=6, file_name=None):
    width, height = size
    line = width * 3
    png_filter = pack(">B", 0)
    scanlines = b"".join(
        [png_filter + data[y * line : y * line + line] for y in range(height)]
    )

    magic = pack(">8B", 137, 80, 78, 71, 13, 10, 26, 10)
    
 
    ihdr = [b"", b"IHDR", b"", b""]
    ihdr[2] = pack(">2I5B", width, height, 8, 2, 0, 0, 0)
    ihdr[3] = pack(">I", zlib.crc32(b"".join(ihdr[1:3])) & 0xFFFFFFFF)
    ihdr[0] = pack(">I", len(ihdr[2]))

  
    idat = [b"", b"IDAT", zlib.compress(scanlines, level), b""]
    idat[3] = pack(">I", zlib.crc32(b"".join(idat[1:3])) & 0xFFFFFFFF)
    idat[0] = pack(">I", len(idat[2]))

    
    iend = [b"", b"IEND", b"", b""]
    iend[3] = pack(">I", zlib.crc32(iend[1]) & 0xFFFFFFFF)
    iend[0] = pack(">I", len(iend[2]))

    if not file_name:
        return magic + b"".join(ihdr + idat + iend)
    with open(file_name, "wb") as f:
        f.write(magic+ b"".join(ihdr + idat + iend))
    return None
class pixelsParse:
    __slots__ = {"__rgb", "pos", "raw", "size"}
    def __init__(self, data, left=0,top=0,width=0,height=0, size=None):

        _Pos = collections.namedtuple("Pos", "left, top")
        _Size = collections.namedtuple("Size", "width, height")
        self.__rgb = None  
        self.raw = data
        self.pos = _Pos(left, top)
        if size is not None:
            self.size = size
        else:
            self.size = _Size(width, height)
    @property
    def height(self):
        return self.size.height
    @property
    def left(self):
        return self.pos.left
    @property
    def rgb(self):
        
        if not self.__rgb:
            rgb = bytearray(self.height * self.width * 3)
            raw = self.raw
            rgb[0::3] = raw[2::4]
            rgb[1::3] = raw[1::4]
            rgb[2::3] = raw[0::4]
            self.__rgb = bytes(rgb)
        return self.__rgb
    @property
    def top(self):
        return self.pos.top
    @property
    def width(self):
        return self.size.width
def generate_bitBmp(hwnd=0,screenDC=0,left=0,top=0,width=0,height=0,cx=0,cy=0):

    if screenDC==0:

        screenDC = user32.GetWindowDC(hwnd)

    mfcDC = win32ui.CreateDCFromHandle(screenDC)

    saveDC = mfcDC.CreateCompatibleDC()

    saveBitMap = win32ui.CreateBitmap()

    saveBitMap.CreateCompatibleBitmap(mfcDC,width,height)
    
    saveDC.SelectObject(saveBitMap)
    
    saveDC.BitBlt((0,0), (width,height), mfcDC, (0, 0), WinConst.SRCCOPY)
    
    pixels = saveBitMap.GetBitmapBits(True)
    img=pixelsParse(data=bytearray(pixels), left=left
    ,top=top,width=width,height=height)
    pixels=None
    return img

def screen_shot(file_name,hwnd=0,screenDC=0,left=0,top=0,width=0,height=0):
    if not all([width,height]):return False
    img=generate_bitBmp(hwnd=hwnd, screenDC=screenDC,left=left,top=top,width=width,height=height,cx=0,cy=0)
    to_png(img.rgb, img.size, level=6, file_name=file_name)
    img=None
    return True
def whole_screenshot(mb,webview,file_name):

    left=0
    top=0
    width=mb.wkeGetContentWidth(webview)
    height=mb.wkeGetContentHeight(webview)
    pixels=create_string_buffer(width*height*4)
    mb.wkeResize(webview,width,height)
    mb.wkeUpdate()
    mb.wkePaint(webview,byref(pixels),0)
    img=pixelsParse(data=bytearray(pixels), left=left
        ,top=top,width=width,height=height)
    to_png(img.rgb, img.size, level=6, file_name=file_name)
    pixels=None
    img=None
    return True        

