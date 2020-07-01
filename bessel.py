import math as m
import matplotlib.pyplot as plt
import numpy as np


def bessel(n):
    f = float(n)
    #s = n + x ** 2
    for i in range(1000):
        """ s = s + ((-1) * k)((x / 2) ** (n + (2 * k))) /
            ((m.factorial(k) * m.factorial(k + n)))
        """
        return s

    x = np.linspace(0, 5, 100)
    print(x)
    # print(bessel(2, 3))
    plt.plot(x, bessel(1))
