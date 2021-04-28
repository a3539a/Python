"""
날짜 : 2021/04/27
이름 : 김승용
내용 : 교재 실습 p40
"""

# 관계 연산자

num1 = 100 # 피연산자1
num2 = 20 # 피연산자2

# 동등비교
bool_result = num1 == num2 # 두변수의 값이 같은지 비교
print(bool_result)
bool_result = num1 != num2 # 두 변수의 값이 다른지 비교
print(bool_result)

# 크기비교
bool_result = num1 > num2 # num1값이 큰지 비교
print(bool_result)
bool_result = num1 >= num2 # num1값이 크거나 같은지 비교
print(bool_result)
bool_result = num1 < num2 # num2값이 작은지 비교
print(bool_result)
bool_result = num1 <= num2 # num2값이 작거나 같은지 비교
print(bool_result)

# 논리 연산자

# 두 관계식이 같은지 판단
log_result = num1 >= 50 and num2 <= 10
print(log_result)

# 두 관계식 중 하나라도 같은지 판단
log_result = num1 >= 50 or num2 <= 10
print(log_result)

log_result = num1 >=50 # 얘가 참이므로
print(log_result)

# 괄호 안의 관계식 판단 결과에 대한 부정
log_result = not(num1 >= 50)
print(log_result)