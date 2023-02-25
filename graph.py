import matplotlib.pyplot as plt
import numpy as np


def draw(ymin, ymax, xmin, xmax):
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

    # plot the functions, with labels
    plt.plot(x, y, 'c-', label='y=(ln(x)/x)^3')
    plt.ylim([-ymax, ymax])
    plt.legend(loc='upper right')

    fig = plt.gcf()  # Взять текущую фигуру
    fig.set_size_inches(15, 15)  # Задать размеры графика
    fig.tight_layout(pad=5.0)
    fig.savefig('lab02_part01.png', dpi=500)
    # show the plot
    plt.show()


#draw(-0.4, 0.075, 0, 10)
draw(-1, 1, 0, 5)