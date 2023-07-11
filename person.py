class Person:
    def __init__(self, name: str, age: str):
        self.name = name
        self.age = age
    def print_info(self):
        print("Привет, меня зовут", self.name, "и меня зовут ", self.age)

def person_func(input_info):
    name, age = input_info.split()
    person = Person(name, age)
    person.print_info()

if __name__ == "__main__":
    input_info = input("Введите имя и возраст через пробел - ")
    person_func(input_info)