#12list.py

su = [23, 7, 19, 45, 31, 26] #int정수형구성 리스트
print('소트전: ', end = ' ')
print(su)

su.sort() #숫자타입대상
print('소트후: ', end = ' ')
print(su)

print('샘플링 ', su[-1]) #맨끝에 위치

print('분  리: ', end = ' ') #1,2,3
print(su[1:4])