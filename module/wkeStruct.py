from ctypes import c_int,c_short,c_ushort,c_ulong,c_long,c_longlong,c_ulonglong,c_float,c_char,c_char_p,c_wchar_p,c_bool,c_void_p,c_size_t,Structure,byref,POINTER,windll,cdll,CFUNCTYPE,WINFUNCTYPE
class wkeProxy(Structure):

    _fields_ = [('wkeProxyType', c_int),('hostname', c_char *100),('port', c_ushort ),('user', c_char *50),('password',c_char *50)]
class wkeRect(Structure):

    _fields_=[('x',c_int),('y',c_int),('w',c_int),('h',c_int)]
class wkeMemBuf(Structure):

    _fields_=[('size',c_int),('data',c_char_p),('length',c_size_t)]
class wkeString(Structure):
    ...
class wkePostBodyElement(Structure):

    _fields_=[('size',c_int),('type',c_int),('data',POINTER(wkeMemBuf)),('filePath',wkeString),('fileStart',c_longlong),('fileLength',c_longlong)]
    ...
class wkePostBodyElements(Structure):

    _fields_ =[('size',c_int),('element',POINTER(POINTER(wkePostBodyElement))),('elementSize',c_size_t),('isDirty',c_bool)]
class wkeScreenshotSettings(Structure):

    _fields_=[('structSize',c_int),('width',c_int),('height',c_int)]
class wkeWindowFeatures(Structure):

    _fields_=[('x',c_int),('y',c_int),('width',c_int),('height',c_int),('menuBarVisible',c_bool),('statusBarVisible',c_bool),('toolBarVisible',c_bool),('locationBarVisible',c_bool),('scrollbarsVisible',c_bool),('resizable',c_bool),('fullscreen',c_bool)]
class wkePrintSettings(Structure):

    _fields_=[('structSize',c_int),('dpi',c_int),('width',c_int),('height',c_int),('marginTop',c_int),('marginBottom',c_int),('marginLeft',c_int),('marginRight',c_int),('isPrintPageHeadAndFooter',c_bool),('isPrintBackgroud',c_bool),('isLandscape',c_bool)]
class wkePdfDatas(Structure):

    _fields_=[('count',c_int),('sizes',c_size_t),('datas',c_void_p)]

class Rect(Structure):

    _fields_=[('Left',c_int),('Top',c_int),('Right',c_int),('Bottom',c_int)]
class mPos(Structure):

    _fields_=[('x',c_int),('y',c_int)]
class mSize(Structure):

    _fields_=[('cx',c_int),('cy',c_int)]
class bitMap(Structure):

    _fields_=[('bmType',c_int),('bmWidth',c_int),('bmHeight',c_int),('bmWidthBytes',c_int),('bmPlanes',c_short),('bmBitsPixel',c_short),('bmBits',c_int)]
class blendFunction(Structure):

    _fields_=[('BlendOp',c_char_p),('BlendFlags',c_char_p),('SourceConstantAlpha',c_char_p),('AlphaFormat',c_char_p)]
class PAINTSTRUCT(Structure):

    _fields_=[('hdc',c_int),('fErase',c_int),('rcPaint',Rect),('fRestore',c_int),('fIncUpdate',c_int),('hdc',c_int),('rgbReserved',c_char *32)]
class COMPOSITIONFORM(Structure):

    _fields_=[('dwStyle',c_int),('ptCurrentPos',mPos),('rcArea',Rect)]