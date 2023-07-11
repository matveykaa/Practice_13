class BankAccount:
    def __init__(self, balance: float, interest_rate: float):
        self.balance = balance
        self.interest_rate = interest_rate

    def deposit(self, amount: float):
        self.balance += amount
        print("Итого = ", self.balance)

    def withdraw(self, amount: float):
        if amount <= self.balance:
            self.balance -= amount
            print("Итого = ", self.balance)
        else:
            print("Ошибка! Недостаточно средств на счете")

    def add_interest(self):
        interest = self.balance * self.interest_rate * 0.01
        self.balance += interest
        print("Баланс после добавления процента к общей сумме = ", self.balance)


def bank_calc(balance, rate):
    bank = BankAccount(balance, rate)
    input_deposit = float(input("Сумма для вклада - "))
    bank.deposit(input_deposit)
    input_data = float(input("Сумма для снятия - "))
    bank.withdraw(input_data)
    bank.add_interest()




if __name__ == "__main__":
    input_balance = float(input("Введите свой начальный баланс - "))
    input_rate = float(input("Введите желаемый процент для вклада - "))
    bank_calc(input_balance, input_rate)