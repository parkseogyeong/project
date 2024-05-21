#zoom.py

#import LG #import LG 물리적인파일명
from LG import user_id, user_pwd, note, game
import time
from datetime import datetime

#zoom.py에서 LG.py문서 전역변수 및 함수접근 from~import구문

print('-' * 100)
print('zomm.py')

time.sleep(1) #Thread.sleep(1000), setTimeout(1, 2000=2초)
print(user_id)
print(user_pwd)
time.sleep(1)
print()
note()
time.sleep(1)
game()

print('-' * 100)
print()