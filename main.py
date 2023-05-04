#1
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f'Імя : {self.name}, Вік: {self.age}')
student = Student('Vasia', 23)
student.info()