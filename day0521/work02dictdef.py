import random
import time
import math
import sys #프로그램종료 sys.exit()

menu = {'cake':230, 'tea':970} #메뉴이름을 key, 메뉴가격을 value
b1 = True
num = 0

def saveMenu():
        #menu['tea'] = 340
        name=input('key메뉴이름>>>')
        price=int(input('value가격입력>>>'))
        menu[name]=price
        print(name+'키값 등록 성공했습니다')

def selectAllMenu():
        for k in menu:
            print(k, ':', menu[k])
            print()

def editMenu():
        name=input('수정key메뉴이름>>>')
        if menu.get(name)==None:
            print(name, '수정키 데이터가 없습니다')
        else:
            price=int(input('value수정가격입력>>>'))
            menu[name]=price
            print(name+'키값 수정 성공했습니다')

def deleteMenu():
        name=input('삭제key메뉴이름>>>')
        if menu.get(name)==None:
            print(name, '키 데이터가 없습니다')
        else:
            menu.pop(name)
            print(name, '데이터삭제 성공했습니다')

def searchMenu():
        name=input('검색key메뉴이름>>>')
        if menu.get(name)==None:
            print(name, '검색데이터가 없습니다')
        else:
            print(name, ':', menu[name])

def exitMenu():
        print('프로그램을 종료합니다')
        sys.exit()

while b1:
    print()
    num=int(input('1.등록 2.출력 3.수정 4.삭제 5.조회 9.종료 >>>'))


    if num==9:
        print('프로그램을 종료합니다')
        b1=False
        sys.exit()
    elif num==1:
         saveMenu()
    elif num==2:
         selectAllMenu()
    elif num==3:
         editMenu()
    elif num==4:
         searchMenu()
    elif num==5:
         deleteMenu()
    else:
         exitMenu()