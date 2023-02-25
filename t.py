import methods as m
import numpy as np
from scipy.optimize import minimize


class vector:
    x = 0.0
    y = 0.0

    def __init__(self, x, y):
        self.x = x
        self.y = y


def fx(x):
    return 1 - 2*x.x - 2*x.y - 4*x.x*x.y + 10*(x.x**2) + 2*(x.y**2)


def gradient(x):
    return vector(200*x.x, 200*x.y)


def Calculate(v, gradient, lambd):
    x = v.x-lambd * gradient.x
    y = v.y-lambd * gradient.y
    return vector(x, y)


def MakeSimplefx(x, grad, xj):
    vx = xj.x-x*grad.x
    vy = xj.y-x*grad.y
    return fx(vector(vx, vy))


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

    while True:

        last = current
        grad = gradient(current)
        lambd = GoldenSelection(0, 0.05, eps, grad, current)
        current = Calculate(current, grad, lambd)
        if (abs(fx(current)-fx(last)) > eps):
            return current


# Тело главной функции
# Функция
def f(X):
    return 1 - 2*x[0] - 2*x[1] - 4*x[0]*x[1] + 10*(x[0]**2) + 2*(x[1]**2)

x = np.zeros(2, dtype = float)
def test(t, y, e):
    # Начальная точка поиска минимума функции
    x[0] = t
    x[1] =y
    xtol = e # Точность поиска экстремума
    # Находим минимум функции
    #Нелдер-Мид
    minimize(f, x, method = 'Nelder-Mead', options = {'xtol': xtol, 'disp': True}) 


def main():
    # x = input("Введите x: ")
    # y = input("Введите y: ")
    # E = input("Введите E: ")
    t = 1
    y = 1
    E = 0.001
    v = vector(float(t), float(y))
    result = GradDown(v, E)
    print("\nРезультат: x = " + str(result.x) + " y = " + str(result.y))
    test(t, y, E)


main()
