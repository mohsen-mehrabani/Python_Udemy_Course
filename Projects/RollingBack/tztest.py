import sqlite3
import datetime
import pytz
import pickle

db = sqlite3.connect("contacts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)
db.execute("CREATE TABLE IF NOT EXISTS accounts (name TEXT PRIMARY KEY NOT NULL, balance INTEGER NOT NULL)")
db.execute("CREATE TABLE IF NOT EXISTS history (time TIMESTAMP NOT NULL ,"
           " account TEXT NOT NULL, amount INTEGER NOT NULL,"
           " zone INTEGER NOT NULL, PRIMARY KEY (time, account))")
db.execute("CREATE VIEW IF NOT EXISTS localhistory as SELECT strftime('%Y-%m-%d %H:%M:%f', history.time, 'localtime')"
           " as localtime, history.account, history.amount from history order by history.time")


class Account(object):

    @staticmethod
    def _current_time():
        # local_time = pytz.utc.localize(datetime.datetime.utcnow())
        # return local_time.astimezone()
        utc_time = pytz.utc.localize(datetime.datetime.utcnow())
        local_time = utc_time.astimezone()
        zone = local_time.tzinfo    # this is so helpful https://docs.python.org/2.4/lib/datetime-tzinfo.html
        return utc_time, zone

    def __init__(self, name: str, opening_balance: int = 0):
        cursor = db.execute("SELECT name, balance FROM accounts WHERE (name=?)", (name, ))
        row = cursor.fetchone()

        if row:
            self.name, self._balance = row
            print("Retrieved record for {}.".format(self.name), end=" ")
        else:
            self.name = name
            self._balance = opening_balance
            cursor.execute("INSERT INTO accounts VALUES (?,?)", (name, opening_balance))
            cursor.connection.commit()

            print("Account created for {}.".format(self.name), end=" ")
        self.show_balance()

    def _save_update(self, amount):
        new_balance = self._balance + amount
        deposit_time, zone = Account._current_time()  # <----- unpack the returned tuple
        picked_zone = pickle.dumps(zone)
        db.execute("UPDATE accounts SET balance = ? WHERE (name = ?)", (new_balance, self.name))
        db.execute("INSERT INTO history VALUES (?,?,?,?)", (deposit_time, self.name, amount, picked_zone))
        db.commit()
        self._balance = new_balance

    def deposit(self, amount: int) -> float:
        if amount > 0:
            self._save_update(amount)
            print("{:.2f} deposited.".format(amount / 100))
        return self._balance / 100

    def withdraw(self, amount: int) -> float:
        if 0 < amount < self._balance:
            self._save_update(-amount)
            print("{:.2f} withdrawn.".format(amount / 100))
            return amount / 100
        else:
            print("The amount must be grater than zero and no more than your balance")
            return 0

    def show_balance(self):
        print("Balance on account {} is {:.2f}.".format(self.name, self._balance / 100))


if __name__ == "__main__":
    john = Account("John")
    john.deposit(1010)
    john.deposit(10)
    john.deposit(10)
    john.withdraw(30)
    john.withdraw(0)
    john.show_balance()
    terry = Account("TerryJ")
    graham = Account("Graham", 9000)
    erick = Account("Erick", 7000)
    micheal = Account("Micheal")
    terryG = Account("TerryG")

    db.close()
