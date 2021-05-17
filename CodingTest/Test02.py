"""
날짜 : 2021/05/13
이름 : 김승용
내용 : 코딩 테스트 - 숫자 카드 게임
"""

# n, m 을 공백으로 구분하여 입력 받기
n, m = map(int, input('입력 :').split())

nums = []
result = 0

for i in range(n):
    data = list(map(int, input('입력 :').split()))

# data에서 가장 작은 수 구하기
data.sort()
num = data[0]
nums.append(num)

# nums 에서 가장 큰 값 구하기
nums.sort()
result = nums[-1]

print(result)