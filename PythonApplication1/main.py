
import sys
#from panda_test_mod import *
from numpy_mod import *
from pythonnet_mod import *

def hello_py():
    print('Hello python!!!!')

def main():
    #hello_py()
    print('This project was uploaed to gitbub!!!')
    #numpy_test()
    #dat=loadtxt_test()
    #panda_test()
    #loadtxt_test()
    pythonnet_test_str()

if __name__ == "__main__":
    sys.exit(int(main() or 0))