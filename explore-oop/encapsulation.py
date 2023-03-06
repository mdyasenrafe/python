class Account:
    def __init__(self,  holder, intial_bal):
        self.holder = holder
        self.__balance = intial_bal

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def get_balance(self):
        return self.__balance


class StudentAceount(Account):

    def __init__(self, holder, school, intial_bal):
        self.school = school
        super().__init__(holder, intial_bal)


Rahim = StudentAceount("Rahim", "CU", 50000)
Rahim.withdraw(10000)
Rahim.deposit(20000)
print(Rahim._Account__balance)
