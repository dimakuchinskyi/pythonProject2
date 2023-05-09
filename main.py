#Симулятор навчального закладу (база даних)
class School:
    def __init__(self, name, students):
        self.name = name
        self.students = students #Список студентів
    def admit_student(self, student):
        self.students.append(student)
        print(f'{student.name} був доданий до школи {self.name}') #Дописати, коли створено клас студентыв
    def expel_student(self, student):
        expelled_student = next(filter(lambda s: s.name == student.name
                                                 and s.grade == student.grade, self.students), None)
        if expelled_student is not None:
            self.students_remove(expelled_student)
            print(f'{expelled_student.name} був видалений з {self.name}')
        else:
            print(f'{student.name} не був видалений {self.name}')


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
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(filtered_numbers)