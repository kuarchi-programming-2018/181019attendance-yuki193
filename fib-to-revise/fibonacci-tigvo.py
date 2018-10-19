# -*- coding: utf-8 -*-


def fib(n):
    x=0
    y=1
    for i in range(n):
        z=x+y
        x=y
        y=z
    return x
            

print(fib(2018)) 