"""
날짜 : 2021/04/29
이름 : 김승용
내용 : 파이썬 Class 실습하기 교재 p148
"""

from Ch06.sub1.Account import Account
from Ch06.sub1.Computer import Computer

# Account 객체 생성
kb = Account('국민은행', '1111-11-1111', '김유신', 10000)
kb.deposit(40000) # 참조연산
kb.withdraw(7000)
kb.show()

wr = Account('우리은행', '2222-22-2222', '김춘추', 30000)
wr.deposit(10000)
wr.withdraw(5000)
wr.show()

# Computer 객체 생성
samsung = Computer('samsung', 'Intel i7', '16GB', '1TB')
imac = Computer('apple', 'Intel i7', '32GB', '1TB')

samsung.calc()
samsung.info()

imac.calc()
imac.info()










