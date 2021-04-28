"""
날짜 : 2021/04/27
이름 : 김승용
내용 : 교재 실습 p41
"""

# 대입 연산자

# 변수에 값 할당(=)
i = tot = 10 # i = 10; tot = 10
i += 1 # i = i + 1
tot += i # tot = tot + i
print(i, tot)

# 같은 줄에 중복 출력
print('출력1', end = '~~~~,') # end = '구분자'
print('출력2')

v1, v2 = 100, 200

# 변수 교체

v2, v1 = v1, v2
print(v1, v2) # 200 100 으로 서로 바뀜

# 패킹(Packing) 할당
lst = [1, 2, 3, 4, 5]
v1, *v2 = lst # *가 패킹연산자 이다 *가 붙은 변수에만 원소가 묶여서 할당 된다.
print(v1, v2)

*v1, v2 = lst
print(v1)
print(v2)