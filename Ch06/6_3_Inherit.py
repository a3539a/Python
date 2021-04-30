"""
날짜 : 2021/04/30
이름 : 김승용
내용 : 파이썬 클래스 상속 실습하기 교재 p163
"""

from Ch06.sub2.StockAccount import StockAccount

kb = StockAccount('KB증권', '111-111-111', '김유신', 10000,'삼성전자', 10, 80000)
kb.deposit(40000)
kb.withdraw(5000)
kb.buy(10, 80000)
kb.sell(10, 8000)
kb.show()