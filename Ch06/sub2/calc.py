"""
모듈 파일 다른 언어에선 라이브러리 라고도 한다.
"""
def plus(x, y):
    return x + y

def minus(x, y):
    return  x - y

def multi(x, y):
    return  x * y

def div(x, y):
    return x / y


if __name__=='__main__':
    # 모듈 파일의 프로그램 시작점을 선언해서 의도치 않은 코드 실행을 차단
    print('plus : ', plus(1, 2))
    print('minus : ', minus(1, 2))
    print('multi:', multi(2, 3))
    print('div:', div(4, 2))
