"""
Python for .NET을 시험해 보기위한 파일임

다음 사이트에 설치 및 사용방법이 있음

http://pythonnet.github.io/

* 사용을 하기 위해서는 .NET 4.0+ 이상의 CLR을 이용하여야 한다.
* 위의 사이트에서 알려주는 파이썬 패키지 저장소로 가서
  현재 사용중인 파이썬의 버전에 적합한 whl파일을 다운로드한다. 

* 먼저 "Anaconda prompt"를 관리자 권한으로 실행시켜야한다.
* 실행된 관리자 CMD 창에서 다음 명령으로 설치한다.

* pip install pythonnet~~~~.whl

"""
import clr
import System

def pythonnet_test_str():
    print(System.Environment.Version)

def pythonnet_test_csharp_dll():
    path = '../CS_DLL/bin/Debug/'
    clr.AddReference(path+'CS_DLL')  #주의사항: 끝에 .dll 이라는 확장자를 뺀다
    from CS_DLL import Class1
    p = Class1()
    b = p.add(1. , 3.)
    print(b)
    a= p.Print(u'강정민')
    print(a)

