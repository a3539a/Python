"""
날짜 : 2021/05/03
이름 : 김승용
내용 : 파이썬 파일 입출력 실습하기 교재 p217
"""

# 파일 읽기(File Input)
file1 = open('C:/Users/Bigdata/Desktop/Sample.txt', 'r') # open('경로(Path)', '모드(mode)')
line = file1.readline()

print('line :', line)
file1.close()

# 여러줄 파일 읽기
file2 = open('C:/Users/Bigdata/Desktop/Sample.txt', 'r') # open('경로(Path)', '모드(mode)')

while True:
    line = file2.read()

    if not line:
        # 읽을 라인이 없을 경우
        break

    print(line)

file2.close()

# 파일 쓰기(File Output)
file3 = open('C:/Users/Bigdata/Desktop/Test.txt', 'w') # open('경로(Path)', '모드(mode)')
file3.write('안녕하세요\n')
file3.write('반갑습니다\n')
file3.write('감사합니다\n')
file3.close()

# 구구단 쓰기
file4 = open('C:/Users/Bigdata/Desktop/GuguDan.txt', 'w') # open('경로(Path)', '모드(mode)')

for i in range(2, 10):
    file4.write(str(i))
    file4.write("단\n")
    for j in range(1, 10):
        k = i * j
        file4.write('{} X {} = {}\n'.format(i, j, k))

file4.close()












