import math as m


def gold(a, b, E):
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


def newton(a, b, E):
    a = float(a)
    b = float(b)
    E = float(E)
    if (f(a)*fp2(a) >= 0):
        x = a
    else:
        x = b
    i = 1
    x_res = x
    while True:
        if (abs(fp(x)) < E):
            break
        x_res = x
        x = x - fp(x)/fp2(x)
        i = i+1

    return [f(x_res), x_res, i]


def f(x):
    """Функция возвращающая значение выражения от x

    Parameters
    ----------
    x: аргумент функции\n
    mod: модификатор функции (если ищем максимум -1, иначе 1)\n
    ----------
    """

    if (x <= 0):
        print("Для x="+str(x) +
              "невозможно вычислить значение функции. Знаменатель равен нулю!")
        exit(1)
    res = (m.log(x)/x)**3
    return res


def fp(x):
    """Функция возвращающая значение первой производной выражения от x

    Parameters
    ----------
    x: аргумент функции\n
    ----------
    """
    if (x <= 0):
        print("Для x="+str(x) +
              "невозможно вычислить значение функции. Знаменатель равен нулю!")
        exit(1)
    res = (3*(m.log(x)**2)-3*(m.log(x)**3))/(x**4)
    return res


def fp2(x):
    """Функция возвращающая значение второй производной выражения от x

    Parameters
    ----------
    x: аргумент функции\n
    ----------
    """
    if (x <= 0):
        print("Для x="+str(x) +
              "невозможно вычислить значение функции. Знаменатель равен нулю!")
        exit(1)
    res = (6*(m.log(x))-21*(m.log(x))**2+12*(m.log(x))**3)/(x**5)
    return res

newton(2, 3, 0.0001)
