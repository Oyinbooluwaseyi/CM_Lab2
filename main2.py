import numpy as np
from scipy.optimize import minimize
# Функция
def f(X):
    return 1 - 2*x[0]  - 2*x[1]  - 4*x[0]*x[1] + 10*(x[0]**2)  + 2*(x[1]**2)
x = np.zeros(2, dtype = float)
def test():
    
    # Начальная точка поиска минимума функции
    x[0] = -150.0
    x[1] = 10
    xtol = 1.0e-5 # Точность поиска экстремума
    # Находим минимум функции
    #Нелдер-Мид
    minimize(f, x, method = 'Nelder-Mead', options = {'xtol': xtol, 'disp': True}) 

test()