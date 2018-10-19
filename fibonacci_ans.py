# -*- coding: utf-8 -*-

def fib_simple(n):
    a, b = 0, 1
    for i in range(n-1):
        a, b = b, a + b
    return b


def fib_simple2(n, a0=0, a1=1):
    a, b = a0, a1
    for i in range(n-1):
        a, b = b, a + b
    return b


# ref https://p--q.blogspot.com/2014/06/python11.html
def fib_recursion(n):
    a, b = 0, 1
    if n>=2:
        return fib_recursion(n-1) + fib_recursion(n-2)
    elif n==0:
        return a
    elif n==1:
        return b
    else:
        return -1


def fib_list(n):
    result = [0, 1]
    for i in range(n-1):
        a = result[-1] + result[-2]
        result.append(a)
    return result


# ref wikipedia
def fib_generalterm(n):
    f = ((1 + 5**0.5) / 2)**n / 5**0.5 + 0.5
    return int(f)

# ref 
def fib_generator(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, b + a


if __name__ == '__main__':
    n = 5
    print('fib_simple(%d) ='%n, fib_simple(n))
    print('fib_list(%d) ='%n, fib_list(n))
    print('fib_simple2(%d) ='%n, fib_simple2(n, 1, 3))
    print('fib_generalterm(%d) ='%n, fib_generalterm(n))
    print('fib_recursion(%d) ='%n, fib_recursion(n))

    # fib_generator
    for i in fib_generator(n+1):
        print('fib_generator(%d) ='%i, i)