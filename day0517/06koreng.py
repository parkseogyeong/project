#06koreng.py
#kor=0; eng=0
kor, eng = 0,0 #권장
hap=0; avg=0.0
msg='안내문'
grade='F'

#파이썬 키보드입력 문자값 = input('안내문') 
#파이썬 형변환 str(), int(), float()
#순서4] 키보드입력 Scanner클래스X, <input type=text name=pay>
kor = input('국어입력 >>> ')
eng = input('영어입력 >>> ')

#순서1]  총점,평균
hap = int(kor) + int(eng) #파이썬 형변환 str(), int(), float()
avg = hap/2

#순서2]  if~else 평균점수 70점부터 축합격, 0~69 재시험
if avg >= 70:
    msg='축합격'
else:
    msg='재시험'

#순서3]  if~elif~else 평균점수 100~90 A, 89~80 B, 79~70 C 69~60 D, 59~0 F
if avg >= 90:
    grade='A'
elif avg >= 80:
    grade='B'
elif avg >= 70:
    grade='C'
elif avg >= 60:
    grade='D'
else:
    grade='F'


print('합계 = ', hap)
print('평균 = ', avg)
print('학점 = ', grade)
print('결과 = ', msg)
print('06koreng.py')
print()


