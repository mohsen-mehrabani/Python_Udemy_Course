import datetime
import pytz


class Account:
    """The simple account with balance"""
    @staticmethod   
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        self._transaction_list = [(Account._current_time(), balance)]
        print("The account created for " + self._name)
        self.show_balance()

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            self._transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self._transaction_list.append((Account._current_time(), -amount))
            self.show_balance()
        else:
            print("The amount ({}) must be greater than zero and no more than your account balance".format(amount))
            self.show_balance()

    def show_balance(self):
        print("The balance is: {}".format(self.__balance))

    def show_transactions(self):
        for date, amount in self._transaction_list:
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
    mohsen.withdraw(2000)

    steph = Account("Steph", 800)
    steph.__balance = 200
    steph.deposit(100)
    steph.withdraw(200)
    steph.show_transactions()
    steph.show_balance()
    print(steph.__dict__)
    steph._Account__balance = 40
    steph.show_balance()
