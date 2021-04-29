"""
날짜 : 2021/04/29
이름 : 김승용
내용 : 파이썬 함수 영역 (Scope) 실습하기 교재 p132

함수(Function)
    - 프로그래밍에서 일련의 로직 단위를 모듈로 만든것
    - 함수는 정의, 호출로 이루어진다
"""

def sum(x, y):
    tot = 0

    for k in range(x, y + 1):
        tot += k

    return tot

tot = 0
start = 1
end = 10

tot = sum(start, end)

print('tot : ', tot)

