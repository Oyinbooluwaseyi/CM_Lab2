import numpy as np
from scipy.optimize import minimize
from graph import draw2
import grad_down as gd
import time
def print_res(text, x, y, i, t):
    print("----"+text+"----")
    print("x: "+str(x)+"\nf(x) = "+str(y)+"\nIterations: "+str(i)+"\nTime: " +str(t)+" seconds\n")
# Функция
def fx(x):
    x1, x2 = x
    return 1 - 2*x1 - 2*x2 - 4*x1*x2 + 10*(x1**2) + 2*(x2**2)

def fpx1(x):
    x1, x2 = x
    return -2-4*x2+20*x1

def fpx2(x):
    x1, x2 = x
    return-2-4*x1 + 4*x2


def main():
    # x1 = input("Введите x1: ")
    # x2 = input("Введите x2: ")
    # E = input("Введите E: ")
    x1 = 2
    x2 = 2
    E = 10e-7
    x=np.array([x1,x2])

    stime = time.time()
    res = gd.GradDown(fx, fpx1, fpx2, x, E)
    t = time.time() - stime
    print_res("Наискорейший градиентный спуск",res[0], res[1], res[2], t)

    s2time = time.time()
    res = minimize(fx, x, method='Nelder-Mead', options={'xatol':E})
    t2 = time.time() - s2time
    print_res("Нелдер-Мид",res.x, res.fun, res.nit, t2)
    #draw2(result[0], result[1], fx(result))

main()
