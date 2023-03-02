import numpy as np


def gradient(x, fpx1, fpx2):
    return np.array([fpx1(x), fpx2(x)])


def Calculate(v, gradient, lambd):
    gx1, gx2 = gradient
    vx1, vx2 = v
    x = vx1-lambd * gx1
    y = vx2-lambd * gx2
    return np.array([x, y])


def MakeSimplefx(fx, x, grad, xj):
    gx1, gx2 = grad
    jx1, jx2 = xj
    v1 = jx1-x*gx1
    v2 = jx2-x*gx2
    return fx(np.array([v1, v2]))


def GoldenSelection(fx, a, b, eps, gradient, x):
    fi = 1.6180339887
    x1 = b-((b-a)/fi)
    x2 = a+((b-a)/fi)
    y1 = MakeSimplefx(fx, x1, gradient, x)
    y2 = MakeSimplefx(fx, x2, gradient, x)
    while (abs(b-a) > eps):

        if (y1 <= y2):

            b = x2
            x2 = x1
            x1 = b-((b-a)/fi)
            y2 = y1
            y1 = MakeSimplefx(fx, x1, gradient, x)

        else:

            a = x1
            x1 = x2
            x2 = a+((b-a)/fi)
            y1 = y2
            y2 = MakeSimplefx(fx, x2, gradient, x)

    return (a+b)/2


def GradDown(fx, fpx1, fpx2, x, eps):
    current = np.copy(x)
    i = 1
    while True:
        flast = fx(current)
        grad = gradient(current, fpx1, fpx2)
        lambd = GoldenSelection(fx, 0, 1, eps, grad, current)
        current = Calculate(current, grad, lambd)
        fcur = fx(current)
        if (abs(fcur-flast) < eps):
            return [current, fcur, i]
        i = i+1
