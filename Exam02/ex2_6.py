"""
날짜 : 2021/05/13
이름 : 김승용
내용 : 사전평가 문제)6
"""

class Person:
    def __init__(self, name):
        self.name = name

    def work(self):
        print('{} working...'.format(self.name))

class Student(Person):
    def work(self):
        print('{} studing...'.format(self.name))

class Developer(Person):
    def work(self):
        print('{} programming...'.format(self.name))

if __name__ == '__main__':

    obj1 = Person('김유신')
    obj2 = Student('김춘추')
    obj3 = Developer('장보고')

    people = [obj1, obj2, obj3]

    for person in people:
        person.work()