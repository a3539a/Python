"""
날짜 : 2021/04/29
이름 : 김승용
내용 : 파이썬 리스트 함수 실습하기 교재 p88

함수(Function)
    - 프로그래밍에서 일련의 로직 단위를 모듈로 만든것
    - 함수는 정의, 호출로 이루어진다
"""

dataset = [1, 4, 3]
print('1.dataset : ', dataset)

# List 원소 추가
dataset.append(2)
dataset.append(5)
print('2.dataset : ', dataset)

# List 정렬
dataset.sort()
print('3.dataset : ', dataset) # 오름 차순

dataset.sort(reverse=True)
print('4.dataset : ', dataset) # 내림 차순

# List 원소 삽입
dataset.insert(2, 6)
dataset.insert(1, 7)
print('6.dataset : ', dataset) # 3번째 자리에 6을 삽입

# List 원소 삭제
dataset.remove(6)
print('7.dataset : ', dataset) # 해당 원소 삭제

# map 함수
# - 리스트 원소를 지정된 함수로 일괄 처리 해주는 함수
# - 여러개의 데이터를 한번에 다른 형태로 변환할 때 많이 사용
def plus10(n):
    return n + 10

list1 = [1, 2, 3, 4, 5]
list1_map_list = list(map(plus10, list1))

print('list1_map_list :', list1_map_list)

list2 = [1.1, 2.2, 3.3, 4.4, 5.5]
list2_map_list = list(map(int, list2))

print('list2_map_list : ', list2_map_list)

list3 = [1, 2, 3, 4, 5]
list3_map_list = list(map(lambda x:x * 2, list3))

print('list3_map_list : ', list3_map_list)

list4 = ['1', '2', '3', '4', '5']
list4_map_list = list(map(int, list4))

print('list4 : ', list4)
print('list4_map_list : ', list4_map_list)

# input 함수 확장
a = input('입력 : ')
print('a : ', a)

var1, var2, var3 = input('3개 숫자 입력(띄어쓰기 구분) : ').split()
print('var1 : {}, var2 : {}, var3: {}'.format(var1, var2, var3))
print('var1 + var2 + var3 : ', var1 + var2 + var3)

num1, num2, num3 = map(int, input('3개 숫자 입력(띄어쓰기 구분) : ').split())
print('num1 : {}, num2 : {}, num3: {}'.format(num1, num2, num3))
print('num1 + num2 + num3 : ', num1 + num2 + num3)








