#파이썬 def 타입X  함수이름(매개인자): 라인개행후 내용기술 
#복합데이터 액면그대로 출력가능
def mydata():
    pass
    listdata=['blue', 23, 'F', 78.9, True, '월요일오전']
    print(listdata)

    tupledata= ( 27.43591, 136.9234, 78)
    print(tupledata)

    setdata= { 'ab', 'blue', 'ab', 12, 'ab', 12} #순서X,중복X
    print(setdata)

    dictdata= { 1:'bc', 2:'kb'}
    print(dictdata)



print('main이름명시 testing 10:19 10:21')
#파이썬 함수를 호출하면 기본적으로 main연결되어있음
if __name__ == '__main__':
    mydata()








print()