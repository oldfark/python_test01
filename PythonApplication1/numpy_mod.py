import numpy as np

def loadtxt_test():
    a=np.loadtxt('./data.txt')
    print(a)
    return a

""" 보통 데이터를 엑셀이나 텍스트 파일에서 카피한 후 
클립보드에 있는데이터를 붙여 넣어 그림을 그리는 경우가 많다.
대부분 숫자인데 이경우 사용하면 편리하다.
"""
def read_txt_strs_test():
    from io import StringIO
    a="""1	1
2	4
3	9
4	16
5	25
6	36
7	49
8	64
9	81
10	100"""
    data = np.loadtxt(StringIO(a))
    print(data)