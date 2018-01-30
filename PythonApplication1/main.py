
import sys
from pythonnet_mod import pythonnet_test_str
from pythonnet_mod import pythonnet_test_csharp_dll
from exp_matplotlib_mathtext import exp_matplotlib_mathtext
from exp_matplotlib_cpem2018_fig3 import exp_matplotlib_cpem2018_fig3_run
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
    #pythonnet_test_str()
    #pythonnet_test_csharp_dll()
    #print('여기는 저의 회사 사무실입니다.!!!')
    
    #exp_matplotlib_mathtext()
    exp_matplotlib_cpem2018_fig3_run()
if __name__ == "__main__":
    sys.exit(int(main() or 0))
