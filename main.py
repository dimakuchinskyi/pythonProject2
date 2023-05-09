#Симулятор навчального закладу (база даних)
class School:
    def __init__(self, name, students):
        self.name = name
        self.students = students #Список студентів
    def admit_student(self, student):
        self.students.append(student)
        print(f'{student.name} був доданий до школи {self.name}') #Дописати, коли створено клас студентыв
    def expel_student(self, student):
        pass


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def promote(self):
        self.grade += 1
        print(f'{self.name} був підвищенй {self.grade}')
    def demote(self):
        self.grade -= 1
        print(f'{self.name} був понижений {self.grade}')
    def __str__(self):
        return f'{self.name} - Ранг {self.grade}'


multiply = lambda x, y: x * y
print(multiply(2, 5))