import matplotlib.pyplot as plt
import numpy as np


def plot(functions, arg_min, arg_max, show_grid=False, *args, **kwargs):
    for fn in functions:
        X = np.linspace(arg_min, arg_max, 200)
        y = [fn.eval(x) for x in X]
        plt.plot(X, y, label=str(fn), *args, **kwargs)
    if show_grid:
        plt.grid()
    plt.legend()
    # plt.savefig('plot_adv.png', transparent=True)
    plt.show()
