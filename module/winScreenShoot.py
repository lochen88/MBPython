
from module.wkeStruct import *
import collections
from struct import pack
import zlib

Pos = collections.namedtuple("Pos", "left, top")
Size = collections.namedtuple("Size", "width, height")

#像素矩阵转pnge二进制
def to_png(data, size, level=6, file_name=None):
    # type: (bytes, Tuple[int, int], int, Optional[str]) -> Optional[bytes]
    width, height = size
    line = width * 3
    png_filter = pack(">B", 0)
    scanlines = b"".join(
        [png_filter + data[y * line : y * line + line] for y in range(height)]
    )

    magic = pack(">8B", 137, 80, 78, 71, 13, 10, 26, 10)
    
    # Header: size, marker, data, CRC32
    ihdr = [b"", b"IHDR", b"", b""]
    ihdr[2] = pack(">2I5B", width, height, 8, 2, 0, 0, 0)
    ihdr[3] = pack(">I", zlib.crc32(b"".join(ihdr[1:3])) & 0xFFFFFFFF)
    ihdr[0] = pack(">I", len(ihdr[2]))

    # Data: size, marker, data, CRC32
    idat = [b"", b"IDAT", zlib.compress(scanlines, level), b""]
    idat[3] = pack(">I", zlib.crc32(b"".join(idat[1:3])) & 0xFFFFFFFF)
    idat[0] = pack(">I", len(idat[2]))

    # Footer: size, marker, None, CRC32
    iend = [b"", b"IEND", b"", b""]
    iend[3] = pack(">I", zlib.crc32(iend[1]) & 0xFFFFFFFF)
    iend[0] = pack(">I", len(iend[2]))

    if not file_name:
        # 文件名为空返回图片字节集bytes
        return magic + b"".join(ihdr + idat + iend)

    with open(file_name, "wb") as f:
        f.write(magic+ b"".join(ihdr + idat + iend))

    return None
class ScreenShot:
    __slots__ = {"__rgb", "pos", "raw", "size"}
    def __init__(self, data, monitor, size=None):
        # type: (bytearray, Monitor, Optional[Size]) -> None

        self.__rgb = None  # type: Optional[bytes]
        self.raw = data
        self.pos = Pos(monitor["left"], monitor["top"])
        if size is not None:
            self.size = size
        else:
            self.size = Size(monitor["width"], monitor["height"])

    @property
    def height(self):

        return self.size.height

    @property
    def left(self):

        return self.pos.left

    @property
    def rgb(self):
        # type: () -> bytes
        """
        Compute RGB values from the BGRA raw pixels.

        :return bytes: RGB pixels.
        """

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
class WinShot():
    __slots__ = {"_bmp_info", "_data"}
    bmp = None
    def __init__(self, **_):
        super().__init__()
        bmp_info = BITMAPINFO()
        bmp_info.bmiHeader.biSize = sizeof(BITMAPINFOHEADER)
        bmp_info.bmiHeader.biPlanes = 1#必须设置为1
        bmp_info.bmiHeader.biBitCount = 32
        bmp_info.bmiHeader.biXPelsPerMeter=3780
        bmp_info.bmiHeader.biYPelsPerMeter=3780
        bmp_info.bmiHeader.biCompression = 0#0不压缩
        bmp_info.bmiHeader.biClrUsed = 0
        bmp_info.bmiHeader.biClrImportant = 0
        self._bmp_info = bmp_info

    def grab(self,hwnd=0,screenDC=0,width=0,height=0,x=0,y=0,cx=0,cy=0,file_name=None):
        #hwnd=0默认是win窗口
        if screenDC==0:
            #获取窗口DC
            screenDC = user32.GetWindowDC(hwnd)

        #获取位图DC
        hMemDC = gdi32.CreateCompatibleDC(screenDC)

        self._bmp_info.bmiHeader.biWidth = width
        self._bmp_info.bmiHeader.biHeight = -height
        self._data = create_string_buffer(width * height * 4)#Array[c_char]

        if WinShot.bmp:
            gdi32.DeleteObject(WinShot.bmp)
        # 为bmp设置宽高
        WinShot.bmp = gdi32.CreateCompatibleBitmap(screenDC, width, height)
        gdi32.SelectObject(hMemDC, WinShot.bmp)

        gdi32.BitBlt(hMemDC,cx,cy,width,height,screenDC,x,y,13369376 | 1073741824)#SRCCOPY | CAPTUREBLT
        gdi32.GetDIBits(hMemDC, WinShot.bmp, 0, height, self._data, byref(self._bmp_info),0)#DIB_RGB_COLORS=0
        
        monitor = {"top": x, "left": y, "width": width, "height": height}
        img=ScreenShot(bytearray(self._data), monitor)

        gdi32.DeleteObject(WinShot.bmp)
        gdi32.DeleteDC(hMemDC)
        gdi32.DeleteDC(screenDC)

        return to_png(img.rgb, img.size, level=6, file_name=file_name)

