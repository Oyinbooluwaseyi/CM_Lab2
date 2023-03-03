import matplotlib.pyplot as plt
import numpy as np


def draw1(ymin, ymax, xmin, xmax):
    x = np.linspace(xmin, xmax, 500)

    y =  (np.log(x)/x)**3

    # setting the axes at the centre
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.grid(True)
    plt.xticks(np.arange(0,100,5)) 
    # plot the functions, with labels
    plt.plot(x, y, 'c-', label='y=(ln(x)/x)^3')
    plt.ylim([-ymax, ymax])
    plt.legend(loc='upper right')

    fig = plt.gcf()  # Взять текущую фигуру
    fig.set_size_inches(15, 15)  # Задать размеры графика
    fig.tight_layout(pad=5.0)
    fig.savefig('lab02_part01.png', dpi=1500)
    # show the plot
    plt.show()
def draw2(x1_p,x2_p,fx):
    # установим размер графика
    fig = plt.figure(figsize = (12,10))
    
    # создадим последовательность из 1000 точек в интервале от -5 до 5
    # для осей x1 и x2
    x1 = np.linspace(-5, 5, 1000)
    x2 = np.linspace(-5, 5, 1000)
    
    # создадим координатную плоскость из осей w1 и w2
    x1, x2 = np.meshgrid(x1, x2)
    
    # пропишем функцию
    f = 1 - 2*x1 - 2*x2 - 4*x1*x2 + 10*(x1**2) + 2*(x2**2)

    
    # создадим трехмерное пространство
    ax = fig.add_subplot(projection = '3d')
    
    # выведем график функции, alpha задает прозрачность
    ax.plot_surface(x1, x2, f, alpha = 0.4, cmap = 'Blues')
    
    # выведем точку A с координатами (3, 4, 25) и подпись к ней
    ax.scatter(x1_p, x2_p, fx, c = 'red', marker = '^', s = 100)
    ax.text(x1_p, x2_p, fx, 'A', size = 25)
    
    
    # укажем подписи к осям
    ax.set_xlabel('x1', fontsize = 15)
    ax.set_ylabel('x2', fontsize = 15)
    ax.set_zlabel('f(x1, x2)', fontsize = 15)
    
    # выведем результат
    plt.show()
#draw1(-100, 100, 0, 100)
# draw(-1, 1, 0, 5)
