class Dog:
    def __init__(self, name:str, breed: str, age: float):
        self.name = name
        self.breed = breed
        self.age = age

    def batk(self):
        return print("Гав-гав!")

    def get_human_age(self):
        if self.age < 0:
            print("Ошибка: введено отрицательное число")
            return
        elif self.age < 1:
            human_age = self.age * 14
        elif 1 <= self.age < 2:
            human_age = 14
        elif 2 <= self.age < 3:
            human_age = 22
        else:
            human_age = 22 + (self.age - 2) * 5
        print(f"Человеческий возраст: {human_age :.1f} лет")
        return human_age


if __name__ == "__main__":
    input_name = input("Имя собаки - ")
    input_breed = input("Порода собаки - ")
    input_age = float(input("Возраст - "))
    dog = Dog(input_name, input_breed, input_age)
    dog.batk()
    dog.get_human_age()