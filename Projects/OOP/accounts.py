import datetime
import pytz


class Account:
    """The simple account with balance"""
    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction_list = []
        print("The account created for " + self.name)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()
            self.transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_list.append((Account._current_time(), amount))
            self.show_balance()
        else:
            print("The amount must be greater than zero and no more than your account balance")
            self.show_balance()

    def show_balance(self):
        print("The balance is: {}".format(self.balance))

    def show_transactions(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                tran_type = "Deposited"
            else:
                tran_type = "Withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))


if __name__ == '__main__':
    mohsen = Account("Mohsen", 0)
    mohsen.show_balance()
    mohsen.deposit(1000)
    mohsen.withdraw(50)
    mohsen.show_transactions()
