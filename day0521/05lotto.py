#set 복합데이터로 난수

import random
lotto = set() #셋set인식 {}표시하면 기본인 dict인식함
result = True

while result:
    num = random.randint(1, 45)
    if len(lotto) >= 6 :
        result = False
    else:
        #리스트 lotto.append(num)
        lotto.add(num)

print()
print(lotto)
mylotto = list(lotto)
mylotto.sort()


print(mylotto)