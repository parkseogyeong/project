#18list.py

dt=[5, 7, 33]
print(dt)

dt.append(9)
print(dt)

dt.insert(1, 45) #insert(위치, 데이터)
print(dt)
print('-' * 100)

ret1 = dt.index(7)
print('dt.index(7)위치 ', ret1, '번째')

#ret2 = dt.index(8) #데이터가 없으면 에러발생
#print('dt.index(8)위치 ', ret2, '번째')

dt.remove(33)
print(dt) #[5, 46, 7, 9]

dt.append(71)
dt.append(24)
dt.append(3)
dt.append(15)
print(dt) #[5, 45, 7, 9, 71, 24, 3, 15]

print(dt[1:4]) #해결1] 46 7 9 추출 슬라이싱 [시작:끝+1]
del dt[1:4] #해결2] 46 7 9 삭제가능
dt[1:4]=[] #해결 46 7 9 삭제가능
print(dt)

print()