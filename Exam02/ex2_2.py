"""
날짜 : 2021/05/13
이름 : 김승용
내용 : 사전평가 문제)2
"""

def gcd(a, b):
    temp = 0

    if a < b:
        temp = a
    else:
        temp = b

    while True:
        if a % temp == 0 and b % temp == 0:
            break

        temp -= 1

    return temp

if __name__ == '__main__':
    print('1 과 5 의 최대공약수 : ', gcd(1, 5))
    print('2 과 6 의 최대공약수 : ', gcd(2, 6))
    print('3 과 9 의 최대공약수 : ', gcd(3, 9))
    print('18 과 12 의 최대공약수 : ', gcd(18, 12))
    print('60 과 24 의 최대공약수 : ', gcd(60, 24))