"""
날짜 : 2021/05/13
이름 : 김승용
내용 : 사전평가 문제)3
"""

def factorial(n):

    if n <= 1:
        return 1

    return n * factorial(n - 1)

if __name__ == '__main__':
    print('3! =', factorial(3))
    print('4! =', factorial(4))
    print('5! =', factorial(5))