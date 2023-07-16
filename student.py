class Student:
    def __init__(self, name: str, age: int):
        self.name = name.capitalize()
        self.age = age
        self.grade = []

    def add_grade(self, grade: int):
        self.grade.append(grade)
        print(f'Оценка {grade} добавлена в список оценок студента {self.name}')

    def get_average_grade(self):
        count = summ = 0
        for number in self.grade:
            summ += number
            count += 1
        arifm = round(summ / count, 1)
        print(f'Средняя оценка студента {self.name} = {arifm}')


def student_calc(name: str, age: int):
    student = Student(name, age)
    students = set()
    students.add(student)


if __name__ == "__main__":
    name = input('Имя студента - ')
    age = int(input('Возраст студента - '))
    student_calc(name, age)