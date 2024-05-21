mysite = {1: '네이버', 2:'카카오', 3:'파이썬', 4:'아마존'}
print(mysite)

#print(mysite[5]) #없는 항목은 실행중 에러가 발생
print(mysite.get(5)) #없는 항목인데 실행중에 다르게 표시 (None로 출력됨)
print()

print(mysite[2]) #정상
print(mysite.get(2)) #정상