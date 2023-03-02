import methods as m
import numpy as np
from scipy.optimize import minimize
from graph import draw2
import time

# Функция
def fx(x):
    x1, x2 = x
    return 1 - 2*x1 - 2*x2 - 4*x1*x2 + 10*(x1**2) + 2*(x2**2)

def gradient(x):
    x1, x2 = x
    return np.array([-2-4*x2+20*x1, -2-4*x1 + 4*x2])


def Calculate(v, gradient, lambd):
    gx1, gx2 = gradient
    vx1, vx2 = v
    x = vx1-lambd * gx1
    y = vx2-lambd * gx2
    return np.array([x, y])


def MakeSimplefx(x, grad, xj):
    gx1, gx2 = grad
    jx1, jx2 =xj
    v1 = jx1-x*gx1
    v2 = jx2-x*gx2
    return fx(np.array([v1, v2]))


def GoldenSelection(a, b, eps, gradient, x):
    fi = 1.6180339887
    x1 = b-((b-a)/fi)
    x2 = a+((b-a)/fi)
    y1 = MakeSimplefx(x1, gradient, x)
    y2 = MakeSimplefx(x2, gradient, x)
    while (abs(b-a) > eps):

        if (y1 <= y2):

            b = x2
            x2 = x1
            x1 = b-((b-a)/fi)
            y2 = y1
            y1 = MakeSimplefx(x1, gradient, x)

        else:

            a = x1
            x1 = x2
            x2 = a+((b-a)/fi)
            y1 = y2
            y2 = MakeSimplefx(x2, gradient, x)

    return (a+b)/2


def GradDown(x, eps):
    current = np.copy(x)
    i=1
    while True:
        flast =  fx(current)
        grad = gradient(current)
        lambd = GoldenSelection(0, 1, eps, grad, current)
        current = Calculate(current, grad, lambd)
        fcur = fx(current)
        if (abs(fcur-flast) < eps):
            print("Iterations:"+str(i)+" f(x)=" +str(fcur))
            return current
        i=i+1

def main():
    # x1 = input("Введите x1: ")
    # x2 = input("Введите x2: ")
    # E = input("Введите E: ")
    x1 = 2
    x2 = 2
    E = 10e-7
    x=np.array([x1,x2])
    start_time = time.time()
    result = GradDown(x, E)
    print("--- %s seconds ---" % (time.time() - start_time))
    print("Результат: x1 = " + str(result[0]) + " x2 = " + str(result[1])+"\n")
    start_time = time.time()
    # x=np.array([-5,-5])
    res = minimize(fx, x, method='Nelder-Mead', options={'xatol':E})
    print(res)
    print("--- %s seconds ---" % (time.time() - start_time))
    draw2(result[0], result[1], fx(result))

main()
