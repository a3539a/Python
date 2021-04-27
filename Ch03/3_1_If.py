"""
날짜 : 2021/04/27
이름 : 김승용
내용 : 파이썬 조건문 If 실습 교재 p68
"""

# if
num1, num2 = 1, 2

if num1 > 0:
    print('num1은 0보다 크다.')

if num1 > num2:
    print('num1은 num2보다 크다.')
# A 경우
if num1 > 0:
    if num2 > 1:
        print('num1은 0보다 크고 num2는 1보다 크다.')
# B 경우
if num1 > 0 and num2 > 1:
    print('num1은 0보다 크고 num2는 1보다 크다.')
# A와 B 경우는 논리적으로 같은 말이다.

# if ~ else
num3, num4 = 3, 4

if num3 > num4:
    # 조건이 '참' 일때
    print('num3가 num4 보다 크다.')
else:
    # 조건이 '거짓' 일때
    print('num3가 num4 보다 작다.')

# if ~ elif ~ else
if num1 > num2:
    print('num1은 num2 보다 크다')
elif num2 > num3:
    print('num2은 num3 보다 크다')
elif num3 > num4:
    print('num3은 num4 보다 크다')
else:
    print('num4가 가장 크다')

# 삼항 조건문
num = 5
        # if문을 중심으로 참일땐 앞으로 거짓일땐 else문으로
result = num * 2 if num >= 5 else num + 2

print('result : ', result)

# 확인문제
score = int(input('점수 입력 : '))

print('점수확인 : ', score)

# if score가 90점 이상 100점 이하이면:
#     print('A 입니다')
# elif score가 80점 이상 89점 이하이면:
#     print('B 입니다')
# elif score가 70점 이상 79점 이하이면:
#     print('C 입니다')
# elif score가 60점 이상 69점 이하이면:
#     print('D 입니다')
# elif score가 60점 미만이면:
#     print('F 입니다.')

if 90 <= score <= 100:
    print('A 입니다')
elif 80 <= score <=89:
    print('B 입니다')
elif 70 <= score <80:
    print('C 입니다')
elif 60 <= score and score <70:
    print('D 입니다')
else:
    print('F 입니다')