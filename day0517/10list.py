#10list.py

mydata =['park', 90, 85, 87.5, True, 'B', '축합격'] #혼합리스트
week = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일'] #문자열구성 리스트
lotto = [23, 7, 19, 45, 31, 26] #int정수형구성 리스트
grade = ['A', 'B', 'C', 'D', 'F'] #문자형
rate = [78.1, 34.2, 65.9, 80.5, 25.6] #실수형

print('혼합형타입 리스트', end = ' ')
for a in mydata:
    print(a, end= ' ')

print()
for b in lotto:
    print(b, end= ' ')

print()
for c in week:
    print(c, end= ' ')

print()
for d in grade:
    print(d, end= ' ')

print()
for e in rate:
    print(e, end= ' ')