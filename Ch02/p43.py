"""
날짜 : 2021/04/27
이름 : 김승용
내용 : 교재 실습 p43
"""

# 표준 입력장치

# 1) 문자형 숫자 입력
num = input('num숫자 입력 : ')
print('num type : ', type(num)) # class 'str'
print('num : ', num)
print('num : ', num * 2)

# 2) 문자형 숫자를 정수형으로 변환
num1 = int(input('num1숫자 입력 : ')) # str -> int 로 바꾼다 (형 변환)
print('num1 type : ', type(num)) # class 'int'
print('num1 : ', num1)
print('num1 : ', num1 * 2)

# 3) 문자형 숫자를 실수형으로 변환
num2 = float(input('num2숫자입력 : ')) # str -> float 으로 바꾼다 (형 변환)
result = num1 + num2 # 정수 + 실수
print('result : ', result)