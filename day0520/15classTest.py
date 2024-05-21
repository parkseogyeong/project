print()
import time

class MyClass:
    var = '안녕하세요 둘리' #클래스영역에서 전역변수 접근키워드 self사용

    def __init__(self, name):
        print('\n생성자')
        print(name, '님 환영합니다')
        print(self.var)

    def __del__(self):
        print("My class 소멸자 호출확인")

    def sayHello(self):
        print('sayHello함수')
        print(self.var)

obj =  MyClass('park')
print(obj.var)
print()

time.sleep(0.5)
obj.sayHello( )
del obj
#111페이지 class = 전역변수 + 생성자(self)  + 일반함수(self) 
#자바접근 MyClass  obj = new MyClass();
#파이썬  obj =  MyClass();
#print(obj) #<__main__.MyClass object at 0x000002AEDEF98F50>





print()