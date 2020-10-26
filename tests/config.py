# -*- coding:utf-8 -*-
from os import getcwd
from ctypes import (c_longlong,c_int)
import platform


init_path=getcwd()
icon_path=f'{init_path}/logo.ico'
node_path=f'{init_path}/node.dll'
# node_path=f'{init_path}/miniblink_x64.dll'

_LRESULT = c_longlong if node_path.endswith('x64.dll') and platform.architecture()[0]=='64bit' else c_int