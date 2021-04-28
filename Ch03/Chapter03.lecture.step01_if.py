"""
날짜 : 2021/04/28
이름 : 김승용
내용 : 교제 실습 p61
"""

# 단일 조건문 형식 1

var = 9 # if 블럭에서 사용 될 변수
if var >= 5 : # 조건식
    print('var = ', var)
    print('var는 5보다 크다.')
    print('조건이 참인 경우 실행')

print('항상 실행')

# 단일 조건문 형식 2

# 100 ~ 85 : '우수', 84 ~ 70 : '보통', 69 이하 : '사람이하'
score = int(input('점수 입력 : '))
if score >= 85 and score <= 100:
    print('우수')
else:
    if score >= 70:
        print('보통')
    else:
        print('사람이하')

# 중첩 조건문

score = int(input('점수입력 : '))
grade = '' # 등급

if score >= 85 and score <= 100:
    grade = '우수'
elif score >= 70:
    grade = '보통'
else:
    grade = '사람이하'

print('당신의 점수는 %d이고, 등급은 %s' % (score, grade))

# 삼항 조건문

# 1) 일반 조건문
num = int(input('숫자? ')) # 초기화
result = 0

if num >= 5:
    result = num * 2
else:
    result = num + 2
print('result : ', result)

# 2) 3항 연산자
# 형식) 변수 = 참일때 : if(조건문), else : 거짓일때
result2 = num * 2 if num >= 5 else num + 2
print('result2 : ', result2)