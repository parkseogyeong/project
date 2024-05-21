#02date.py

#import datetime
from datetime import datetime #dt = datetime.now()
import time

print('02date.py문서')
dt=datetime.now()
print(dt) #2024-05-17 12:30:43.067669
ob = time.localtime()
print(ob) #time.struct_time(tm_year=2024, tm_mon=5, tm_mday=17, tm_hour=12, tm_min=30, tm_sec=43, tm_wday=4, tm_yday=138, tm_isdst=0)

print(ob.tm_year, '년', ob.tm_mon, '월', ob.tm_mday, '일')

mydata =['park', 90, 85, 87.5, True, 'B', '축합격']
week = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
lotto = [23, 7, 19, 45, 31, 26] #int정수형구성 리스트