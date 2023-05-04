#Класи

class Student:
    print('Hi!')
    count = 0
    def __init__(self, height = 150):
        self.height = height
        Student.count += 1
    def breathing(self):
        return self.height - 10
oleg = Student()#Об'єкт, екземпляр класу
print(oleg.height)
masha = Student(height = 200)
print(masha.height)
print(Student.count)
print(masha.breathing())
