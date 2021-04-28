"""
날짜 : 2021/04/27
이름 : 김승용
내용 : 교재 실습 p38
"""

# 자료형 변환

# 실수 -> 정수
a = int(10.5)
b = int(20.42)
add = a + b
print('add = ', add)

# 정수 -> 실수
a = float(10)
b = float(20)
add2 = a + b
print('add2 = ', add2)

# 논리형 -> 정수
print(int(True)) # 1
print(int(False)) # 0

# 문자형 -> 정수
st = '10'
print(int(st) ** 2) # 문자 '10'을 정수 10 으로 전환하여 제곱