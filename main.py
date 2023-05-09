#Симулятор навчального закладу (база даних)
class School:
    def __init__(self, name, students):
        self.name = name
        self.students = students #Список студентів
    def admit_student(self, student):
        self.students.append(student)
        print(f'{student.name} був доданий до школи {self.name}') #Дописати, коли створено клас студентыв
class Student:.
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade