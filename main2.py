import methods as m
import numpy as np
from scipy.optimize import minimize

# Функция
def fx(X):
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
    vx = jx1-x*gx1
    vy = jx2-x*gx2
    return fx(np.array([vx, vy]))


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
    current = x
    i=1
    while True:
        
        last = current
        grad = gradient(current)
        lambd = GoldenSelection(0, 0.05, eps, grad, current)
        current = Calculate(current, grad, lambd)
        i=i+1
       
        if (abs(fx(current)-fx(last)) < eps):
            print("Iterations:"+str(i)+" f(x)=" +str(fx(current)))
            return current


# Тело главной функции



x = np.zeros(2, dtype=float)


def test(t, y, e):
    # Начальная точка поиска минимума функции
    x[0] = t
    x[1] = y
    xtol = e  # Точность поиска экстремума
    # Находим минимум функции
    # Нелдер-Мид
    minimize(fx, x, method='Nelder-Mead', options={'disp': True})


def main():
    # x1 = input("Введите x1: ")
    # x2 = input("Введите x2: ")
    # E = input("Введите E: ")
    x1 = -10
    x2 = 1
    E = 0.00001
    x[0]=x1
    x[1]=x2
    result = GradDown(x, E)
    print("Результат: x1 = " + str(result[0]) + " x2 = " + str(result[1])+"\n")
    test(x1, x2, E)


main()
