import numpy as np
import matplotlib.pyplot as plt

def numpy_test():
    print(np.pi)
    x=np.linspace(0, 3.14, 100)
    y=np.tan(x)
    plt.plot(x,y)
    plt.title(r'$\alpha -\beta$')
    plt.show()
