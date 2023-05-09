#Симулятор навчального закладу (база даних)
class School:
    def __init__(self, name, students):
        self.name = name
        self.students = students #Список студентів
    def admit_student(self, student):
        self.students.append(student)
        print(f'{}') #Дописати, коли створено клас студентыв
