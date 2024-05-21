#work03lotto.py

import random

lotto = [0, 0, 0, 0, 0, 0]
#에러 lotto = list()
#6회발생 for반복문
for i in range(6):
    lotto[i] = random.randint(1, 45) #1~45

print(lotto)
lotto.sort()
print(lotto)
print()