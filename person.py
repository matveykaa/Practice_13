class Person:
    def __init__(self, name: str, age: str):
        self.name = name
        self.age = age
    def print_info(self):
        print("Привет, меня зовут", self.name.capitalize(), "и мне ",self.age, "лет")

    def can_vote(self):
        if self.age >= '18':
            print("Совершеннолетний")

def person_func(input_info):
    name, age = input_info.split()
    person = Person(name, age)
    person.print_info()
    person.can_vote()

if __name__ == "__main__":
    input_info = input("Введите имя и возраст через пробел - ")
    person_func(input_info)