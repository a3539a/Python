"""
날짜 : 2021/05/13
이름 : 김승용
내용 : 사전평가 문제)4
"""

import math, random

def lotto():

    lotto_set = set()

    while True:
        num = math.ceil(random.random() * 45)

        lotto_set.add(num)

        if len(lotto_set) == 6:
            break

    return list(lotto_set)

if __name__ == '__main__':

    for i in range(5):
        # 로또 번호 생성
        lotto_nums = lotto()

        # 번호 정렬
        lotto_nums.sort()

        # 번호 출력
        print(lotto_nums)