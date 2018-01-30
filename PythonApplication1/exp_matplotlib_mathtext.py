import matplotlib.pyplot as plt
import numpy as np


def exp_matplotlib_mathtext():
    x=np.linspace(-3.14,3.14,100)
    y=np.sin(x)

    plt.plot(x,y)
    plt.title(r"This is experimantal feasure - $\alpha \omega$")
    plt.show()