# -*- coding:utf-8 -*-
def method(prototype):
    class MethodDescriptor(object):
        __slots__ = ['func', 'bound_funcs']
        def __init__(self, func):
            self.func = func
            self.bound_funcs = {} 
        def __get__(self, obj, type=None):
            if obj!=None:
                try:
                    return self.bound_funcs[obj,type]
                except:
                    ret = self.bound_funcs[obj,type] = prototype(
                        self.func.__get__(obj, type))
                    return ret
    return MethodDescriptor