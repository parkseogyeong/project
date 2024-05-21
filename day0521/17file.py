#파일처리

path = 'C:/Mtest/aaa.txt'
file = open(path, 'w', encoding='utf-8')
name = input('이름>>>')
age = input('나이>>>')
juso = input('주소>>>')

file.write(name+'\n')
file.write(age+'\n')
file.write(juso+'\n')
file.close() #권장
print(path, '파일저장 성공했습니다')


'''
path = 'C:/Mtest/aaa.txt'
wfile = open(path, 'w', encoding='utf-8') #쓰기
rfile = open(path, 'r', encoding='utf-8') #읽기
afile = open(path, 'a', encoding='utf-8') #존재하면 뒤쪽추가

with open(path, 'w', encoding='utf-8') as myfile:
    pass
    #myfile.함수()
'''
