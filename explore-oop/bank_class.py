class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.max_withdrawal = 80
        self.min_withdrawal = 10

    def get_balance(self):
        return self.balance

    def widhdraw_balance(self, amount):
        if amount < self.min_withdrawal:
            return "Minimum withdrawal amount is 10"
        elif amount > self.max_withdrawal:
            return "Maximum withdrawal amount is 80"
        elif amount > self.balance:
            return "Insufficient balance"
        else:
            self.balance = self.balance - amount
            return "Withdrawal successful"

    def deposit_money(self, amount):
        self.balance = self.balance + amount
        return "Deposit successful"


my_bank = Bank("SBI", 100)
balance = my_bank.get_balance()
print(f'Balance: {balance}')
reply = my_bank.widhdraw_balance(10)
deposit = my_bank.deposit_money(20)
balance = my_bank.get_balance()
print(reply, balance, deposit)
