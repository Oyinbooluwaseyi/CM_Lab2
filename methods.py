import math as m
import numpy as np

def gold(f, a, b, E):
    a = float(a)
    b = float(b)
    E = float(E)
    r = 0.618
    t = 0.382  # t=(1-r)
    i = 1

    alfa = a+t*(b-a)
    mu = a+r*(b-a)
    fa = f(alfa)
    fm = f(mu)
    res_f = 1.0
    res_x = -1.0
    while (abs(b-a) > E):

        if (fa <= fm):
            a = alfa
            alfa = mu
            mu = a+r*(b-a)
            fm = f(mu)
            res_f = fm
            res_x = mu
        else:
            b = mu
            mu = alfa
            alfa = a+t*(b-a)
            fa = f(alfa)
            res_f = fa
            res_x = alfa
        i = i+1
    return [res_f, res_x, i]


def newton(f,fp, fp2, a, b, E):
    a = float(a)
    b = float(b)
    E = float(E)
    if (f(a)*fp2(a) >= 0):
        x = a
    else:
        x = b
    i = 1
    x_res = x
    while (abs(fp(x)) < E):
        x_res = x
        x = x - fp(x)/fp2(x)
        i = i+1

    return [f(x_res), x_res, i]





