# -*- coding:utf-8 -*-
from ctypes import (
    c_int,
    c_short,
    c_ushort,
    c_ulong,
    c_long,
    c_longlong,
    c_ulonglong,
    c_float,
    c_char,
    c_char_p,
    c_wchar_p,
    c_bool,
    c_void_p,
    c_size_t,
    Structure,
    byref,
    POINTER,
    create_string_buffer,
    sizeof,
    windll,
    cdll,
    CFUNCTYPE,
    WINFUNCTYPE,
    addressof
    )

from ctypes.wintypes import (
    DWORD,
    HWND,
    INT,
    LONG,
    LPARAM,
    UINT,
    WORD,
    WPARAM,
    RGB,
    MSG,
    HMODULE,
    LPCWSTR,
    HINSTANCE,
    HANDLE,
    LPVOID,
    BYTE
)
user32 = windll.user32
gdi32 = windll.gdi32
imm32= windll.imm32
kernel32= windll.kernel32

