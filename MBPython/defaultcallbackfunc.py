# -*- coding:utf-8 -*-

from ctypes import windll
def destroy_func(**kwargs):
    print('quit')
    windll.user32.PostQuitMessage(0)

    return