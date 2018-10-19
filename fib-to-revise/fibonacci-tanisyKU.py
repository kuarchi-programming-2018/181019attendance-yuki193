# -*- coding: utf-8 -*-
"""
Spyderエディタ

これは一時的なスクリプトファイルです
"""

    #実験
    #F(0) = 0
    #F(1) = 1
    #F(2) = F(0) + F(1)
    #F(3) = F(1) + F(2)

#def fib(n):
    #return F(n)

#def F(m):
    #if m == 0:
        #return 0
    #elif m == 1:
        #return 1
    #else:
        #return F(m-1) + F(m-2)

#1から10まで
#for i in range(40):
    #print(F(i))
#print(fib(i))
#nを40まで大きくしたら、自己処理とループ処理で時間かかるので、方針転換

#代入の=を使い、a = b とb = a + bを利用

#実験   
#a = 0
#b = 1
#for i in range(4):
     #a = b
     #b = a + b
     #print(str(a) + " " + str(b))
#print(b)
#c = 0
#d = 1
#for i in range(4):
    #(c, d) = (d, c + d)
    #print(str(c) + " " + str(d))
#print(d)   

#これでいけそう
#e = 0
#f = 1
#for i in range(2018):
    #(e, f) = (f, e + f)
    #print(str(e) + " " + str(f))
#str(f)
#すぐ出てきた

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        (a, b) = (0, 1)
        for i in range(n - 1):
            (a, b) = (b, a + b)
        return b
    

print(fib(2018))
#答えは In [31]の出力値

    
    


