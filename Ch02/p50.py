"""
날짜 : 2021/04/27
이름 : 김승용
내용 : 교재 실습 p50
"""

# 슬라이싱(Slicing)

oneLine = 'this is one line string'
multiLine = """this is
multi line
string"""
multiLine2 = 'this is\nmulti line\nstring'

# 1) 왼쪽 기준

print(oneLine)
print('문자열 길이 : ', len(oneLine))
print(oneLine[0:4])
print(oneLine[:4]) # 처음부터 5번째 전까지
print(oneLine[:]) # 전체원소
print(oneLine[::2]) # 2의 배수 index

# 2) 오른쪽 기준

print(oneLine[0:-1:2]) #  0번 부터 뒤에서 1번째 앞까지 2의 배수
print(oneLine[-6:-1]) # 뒤에서 6번째 부터 뒤에서 1번째 앞까지
print(oneLine[-6:]) # 뒤에서 6번째 부터 끝까지

# 3) 부분 문자열 생성

subString = oneLine[-11:] # 새로운 객체로 지정
print(subString)