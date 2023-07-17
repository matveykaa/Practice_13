class Employee:
    def __init__(self, name: str, position: str, salary: float):
        self.name = name
        self.position = position
        self.salary = salary

    def get_salary(self):
        print(f'Зарплата работника {self.name.capitalize()} - {self.salary:.1f} р')

    def get_tax(self):
        tax = 0.2 * self.salary
        print(f'Налог - {tax:.1f} р, а доход работника - {(self.salary - tax):.1f} р')

def employee_func(input_info):
    name, position, inp_salary = input_info.split()
    employee = Employee(name, position, float(inp_salary))
    employee.get_salary()
    employee.get_tax()

if __name__ == "__main__":
    input_info = input("Введите имя, должность и зарплату сотрудника через пробел - ")
    employee_func(input_info)