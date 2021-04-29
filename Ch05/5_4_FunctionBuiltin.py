"""
날짜 : 2021/04/29
이름 : 김승용
내용 : 파이썬 내장 함수 실습하기 교재 p118

함수(Function)
    - 프로그래밍에서 일련의 로직 단위를 모듈로 만든것
    - 함수는 정의, 호출로 이루어진다
"""

import math
import random
import time

# 수학과련 내장 함수

r1 = abs(-5) # abs 절대값
print('r1 : ', r1)

r2 = math.ceil(1.2) # math.ceil 올림
r3 = math.ceil(1.8)
print('r2 : ', r2)
print('r3 : ', r3)

r4 = math.floor(1.2) # math.floor 내림
r5 = math.floor(1.8)
print('r4 : ', r4)
print('r5 : ', r5)

r6 = round(1.2) # round 반올림
r7 = round(1.8)
print('r6 : ', r6)
print('r7 : ', r7)

r8 = math.sqrt(4) # math.sqrt 제곱근
r9 = math.sqrt(9)
print('r8 : ', r8)
print('r9 : ', r9)

# random
num1 = random.random()
print('num1 : ', num1) # 0 ~ 1 사이의 실수

num2 = num1 * 48
print('num2 : ', num2) # 0 ~ 48 사이의 실수

num3 = math.ceil(num2)
print('num3 : ', num3) # 1 ~ 48 사이의 정수

num4 = math.ceil(random.random() * 10)
print('num4 : ', num4) # 1 ~ 10 사이의 정수

# 날짜, 시간
t1 = time.time()
print('t1 : ', t1) # Unix time

t2 = time.ctime()
print('t2 : ', t2) # 변환 된 Unix time

now = time.localtime(time.time())
year = time.strftime('%Y', now)
month = time.strftime('%m', now)
date = time.strftime('%d', now)
hour = time.strftime('%H', now)
minute = time.strftime('%M', now)
second = time.strftime('%S', now)

print('{}년 {}월 {}일'.format(year, month, date))
print('{}시 {}분 {}초'.format(hour, minute, second))

















