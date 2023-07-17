from itertools import cycle
class Student:
    def __init__(self, name: str, age: int):
        self.name = name.capitalize()
        self.age = age
        self.grade = []
        self.arifm = 0

    def add_grade(self, grade: int):
        self.grade.append(grade)
        print(f'Оценка {grade} добавлена в список оценок студента {self.name}')

    def get_average_grade(self):
        count = summ = 0
        for number in self.grade:
            summ += number
            count += 1
        try:
            arifm = round(summ / count, 1)
        except ZeroDivisionError:
            print(f'У {self.name} нет еще оценок')
        else:
            self.arifm = arifm
            print(f'Средняя оценка студента {self.name} = {arifm}')

    def get_all_marks(self):
        print("Теперь у студента следующие оценки: ")
        for i in self.grade:
            print(i)

    @property
    def student_name(self):
        return self.name
def student_calc(name: str, age: int):
    students = []
    students_names = []
    student = None

    while True:
        print("Выберите число:")
        print("1 - Добавить нового студента в класс;")
        print("2 - Добавить оценку студенту;")
        print("3 - Вычислить среднюю арифметическую оценку студента;")
        print("4 - Вычислить среднюю арифметическую оценку класса;")
        print("5 - Вывести всех студентов класса и их средние оценки;")
        print("6 - Выход")
        option = int(input())
        match option:
            case 1:
                name = input('Имя студента - ')
                age = int(input('Возраст студента - '))
                new_student = Student(name, age)
                if new_student.student_name in students_names:
                    print('Студент уже существует')
                else:
                    students.append(new_student)
                    students_names.append(new_student.student_name)
                    # students_names[new_student.student_name] = age
            case 2:
                student_name = input('Имя студента, которому хотите добавить оценку - ')
                grade = int(input('Оценка, которую хотите добавить - '))
                found_student = None
                # student_iter = cycle(students)
                i = 0
                while i < len(students):
                    if students[i].student_name == student_name.capitalize():
                        found_student = students[i]
                    i += 1
                # for s in students:
                #     if s.student_name == student_name.capitalize():
                #         found_student = s
                if found_student:
                    found_student.add_grade(grade)
                    found_student.get_all_marks()
                    student = found_student
                else:
                    print('Студент не найден')
            case 3:
                student_name = input('Имя студента, у которого хотите вычеслить среднюю оценку - ')
                found_student = None
                i = 0
                while i < len(students):
                    if students[i].student_name == student_name.capitalize():
                        found_student = students[i]
                    i += 1
                # for s in students:
                #     if s.student_name == student_name.capitalize():
                #         found_student = s
                if found_student:
                    found_student.get_average_grade()
                else:
                    print('Студент не найден')

            case 4:
                summ = count = 0
                for s in students:
                    summ += s.arifm
                    count += 1
                if count == 0:
                    print("Нет данных о средней оценке класса")
                else:
                    arifm_class = round(summ / count, 1)
                    print(f'Средняя оценка класса = {arifm_class}')
            case 6:
                raise KeyboardInterrupt
            case 5:
                for s in students:
                    print(f'{s.name} - {s.arifm}')
            case _:
                print("- - Error - -")


if __name__ == "__main__":
    name = input('Имя студента - ')
    age = int(input('Возраст студента - '))
    student_calc(name, age)