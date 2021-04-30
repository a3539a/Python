from Ch06.sub1.Account import Account

# 클래스 정의

class StockAccount(Account):

    def __init__(self, bank, id, name, money, stock, amount, price):
        # 부모클래스 생성자 실행
        super().__init__(bank, id, name, money)
        self.__stock = stock
        self.__amount = amount
        self.__price = price

    def sell(self, amount, price):
        print('{}를 {}개 {}가격에 판매함'.format(self.__stock, amount, price))

    def buy(self, amount, price):
        print('{}를 {}개 {}가격에 구매함'.format(self.__stock, amount, price))

    def show(self):
        super().show() # Account (부모) 꺼
        print('주식종목 : ', self.__stock)
        print('주식수량 : ', self.__amount)
        print('주식가격 : ', self.__price)