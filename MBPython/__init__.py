# -*- coding:utf-8 -*-
from ctypes import c_int
from platform import architecture
bit=architecture()[0]
_LRESULT=c_int
if bit == '64bit':
    from ctypes import c_longlong
    _LRESULT=c_longlong
from .seticon import set_icon
from .screenshot import screen_shot
from .wndproc import WndProcHook
from .timer import Timer
from . import miniblink