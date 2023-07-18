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
            # print(f'Средняя оценка студента {self.name} = {arifm}')

    def get_all_marks(self):
        print("Теперь у студента следующие оценки: ")
        for i in self.grade:
            print(i)

    @property
    def student_name(self):
        return self.name.capitalize()
def student_calc():
    students = []

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
                if students:
                    flag = True
                    for chel in students:
                        if chel.student_name == name.capitalize():
                            flag = False
                            break
                    if flag:
                        students.append(new_student)
                    else:
                        print('- - Студент уже существует - -')
                else:
                    students.append(new_student)

            case 2:
                if students:
                    student_name = input('Имя студента, которому хотите добавить оценку - ')
                    grade = int(input('Оценка, которую хотите добавить - '))
                    found_student = None
                    for s in students:
                        if s.student_name == student_name.capitalize():
                            found_student = s
                    if found_student:
                        found_student.add_grade(grade)
                        found_student.get_all_marks()
                    else:
                        print('- - Студент не найден - -')
                else:
                    print("- - В классе еще нет учащихся - -")
            case 3:
                if students:
                    student_name = input('Имя студента, у которого хотите вычеслить среднюю оценку - ')
                    found_student = None
                    for s in students:
                        if s.student_name == student_name.capitalize():
                            found_student = s

                    if found_student:
                        found_student.get_average_grade()
                    else:
                        print('- - Студент не найден - -')
                else:
                    print("- - В классе еще нет учащихся - -")

            case 4:
                if students:
                    summ = count = 0
                    for s in students:
                        s.get_average_grade()
                        if s.arifm == 0:
                            pass
                        else:
                            print(f'Средняя оценка студента {s.name} = {s.arifm}')
                        summ += s.arifm
                        count += 1
                    if count == 0:
                        print("Нет данных о средней оценке класса")
                    else:
                        arifm_class = round(summ / count, 1)
                        print(f'Средняя оценка класса = {arifm_class}')
                else:
                    print("- - В классе еще нет учащихся - -")
            case 6:
                raise KeyboardInterrupt
            case 5:
                if students:
                    for s in students:
                        s.get_average_grade()
                        if s.arifm == 0:
                            pass
                        else:
                            print(f'{s.name} - {s.arifm}')
                else:
                    print("- - В классе еще нет учащихся - -")
            case _:
                print("- - Error - -")


if __name__ == "__main__":
    student_calc()