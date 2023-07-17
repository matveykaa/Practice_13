class BankAccount:
    def __init__(self, balance: float):
        self.balance = balance

    def deposit(self, amount: float):
        self.balance += amount
        print("Итого = ", self.balance)

    def withdraw(self, amount: float):
        self.balance -= amount
        print("Итого = ", self.balance)

    def is_negative(self):
        if self.balance < 0:
            print("Баланс отрицательный")

    def add_interest(self, interest_rate: float):
        interest = abs(self.balance * interest_rate * 0.01)
        self.balance += interest
        print("Баланс после добавления процента к общей сумме = ", self.balance)


def bank_calc(balance):
    bank = BankAccount(balance)
    while True:
        print("Выбрите число:")
        print("1 - Положить сумму на счет; 2 - Снять сумму со счета; 3 - Добавить процент на счет; 4 - Выход")
        option = int(input())
        match option:
            case 1:
                amount = float(input('Сумма, которую хотите положить на счет = '))
                bank.deposit(amount)
            case 2:
                amount = float(input('Сумма, которую хотите снять со счета = '))
                bank.withdraw(amount)
                bank.is_negative()
            case 3:
                amount = float(input('Процент добавления на счет = '))
                bank.add_interest(amount)
            case 4:
                raise KeyboardInterrupt



if __name__ == "__main__":
    input_balance = float(input("Введите свой начальный баланс - "))
    bank_calc(input_balance)