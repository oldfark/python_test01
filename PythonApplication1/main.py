
import sys
from panda_test_mod import *
from numpy_plot_mod import *

def hello_py():
    print('Hello python!!!!')

def main():
    #hello_py()
    #numpy_test()
    dat=loadtxt_test()
    panda_test()
    print('This project was uploaed to gitbub!!!')

if __name__ == "__main__":
    sys.exit(int(main() or 0))