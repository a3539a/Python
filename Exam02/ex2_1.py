"""
날짜 : 2021/05/13
이름 : 김승용
내용 : 사전평가
"""

scores = []

while True:
    print('0 : 종료', '1 : 입력')
    result = input('입력 : ')

    if result == '0':
        break

    score = int(input('점수입력 : '))

    scores.append(score)

print('입력한 점수 확인')
print(scores)

sum = 0

for score in scores:
    sum += score

print('리스트 총합 : ', sum)