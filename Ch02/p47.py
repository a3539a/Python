"""
날짜 : 2021/04/27
이름 : 김승용
내용 : 교재 실습 p47
"""

# 외부상수 출력

name = '홍길동'
age = 35
price = 125.456

# 6) 외부상수 인수
print('이름 : {}, 나이 :  {}, data = {}'.format(name, age, price))
print('이름 : {1}, 나이 :  {0}, data = {2}'.format(age, name, price)) # {}안에 인덱스타입의 수를 넣어 순서를 정할 수 있다.

# 7) format 축약형(SQL문 작성)
uid = input('id input : ')
query = f"select * from member where uid = {uid}"
print(query) # member 테이블에서 uid가 (input) 인 레코드 검색