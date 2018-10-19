# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 16:57:19 2018

@author: Takuto
"""
def fib(n):
    if n >= 2:
        return fib(n-1) + fib(n-2)
    else:
        return 1
print(fib(2018))


print(fib(5))