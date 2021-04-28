"""
날짜 : 2021/04/28
이름 : 김승용
내용 : Chap03 연습문제 풀이 p77
"""

# 문제 1)a형 p 77 참조
jim = int(input('짐의 무게는 얼마입니까? : '))
if jim < 10:
    print('수수료는 없습니다.')
else:
    print('수수료는 10000원 입니다.')

# 문제 1)b형 p77 참조
jim = int(input('짐의 무게는 얼마입니까? : '))
if jim >= 10:
    price = (jim // 10) * 10000
    print('수수료는 {}원 입니다.'.format(price))
else:
    print('수수료는 없습니다.')

# 문제 2) p78 참조
import random

print('>>>숫자 맞추기 게임<<<')
com = random.randint(1, 10) # 1 ~ 10 사이 난수 발생

while True:
    my = int(input('1 ~ 10 사이 예상 숫자를 입력하세요 : '))
    if my == com:
        print('~~~ 성공 ~~~')
        break
    elif my > com:
        print('더 작은 숫자를 입력하세요')
    else:
        print('더 큰 숫자를 입력하세요')

# 문제 3) p79 참조

sum = 0
print('수열 : ', end='')
for i in range(1, 101):
    if i % 3 == 0 and not(i % 2 == 0):
        print(i, end=' ')
        sum += i

print()
print('총합 : ', sum)

# 문제 4) p79 참조
multiline = """안녕하세요. 파이썬 세계로 오신걸
환영합니다.
파이썬은 비단뱀 처럼 매력적인 언어입니다."""

words = []

for word in multiline.split():
    print(word)
    words.append(word)

print('단어 개수 : ', len(words))

# 문제 4) 해설집 풀이
# 공백 문자를 기준으로 단어 수 카운트
cnt = 0
doc = [] # 빈 list : 줄 단위 저장
word2 = [] # 단어 저장

for line in multiline.split('\n'):
    doc.append(line) # 줄단위 리스트에 저장
    for w in line.split():
        word2.append(w) # 단어 단위 리스트에 저장
        print(w)
        cnt += 1

# 결고 출력
print('단어 수 : ', cnt)
print(doc)
print(word2)