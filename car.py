class Car:
    def __init__(self, make: str, model: str, year: int, speed: int):
        self.make = make
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate(self, amount: int):
        self.speed += amount
        # print(f'Скорость после ускорения машины = {self.speed}')

    def brake(self, amount: int):
        if self.speed >= amount:
            self.speed -= amount
        else:
            self.speed = 0

        # print(f'Скорость после снижения = {self.speed}')


    @property
    def get_speed(self) -> int:
        return self.speed

def car_calc(make: str, model: str, year: int, speed: int):
    car = Car(make, model, year, speed)
    while True:
        print("Выбрите число:")
        print("1 - Увеличить скорость; 2 - Уменьшить скорость; 3 - Посмотреть текущую скорость; 4 - Выход")
        option = int(input())
        match option:
            case 1:
                amount = int(input('Величина, на которую скорость повышается = '))
                car.accelerate(amount)
            case 2:
                amount = int(input('Величина, на которую скорость снижается = '))
                car.brake(amount)
            case 3:
                print(f'Текущая скорость = {car.get_speed}')
            case 4:
                raise KeyboardInterrupt


if __name__ == "__main__":
    input_data = input("Введите марку, модель и год машины через запятую - ")
    input_speed = int(input("Введите начальную скорость в км\ч - "))
    make, model, str_year = input_data.split(",")
    if make.startswith(" "):
        make = make.lstrip()
    if model.startswith(" "):
        model = model.lstrip()
    if str_year.startswith(" "):
        year = int(str_year.lstrip())
    else:
        year = int(str_year)
    car_calc(make, model, year, input_speed)