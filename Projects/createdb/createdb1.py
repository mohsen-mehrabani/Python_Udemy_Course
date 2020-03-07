import sqlite3

db = sqlite3.connect("contacts.db")
# new_email = "anotherupdate@email.com"
new_email = "newemail@email.com"
# phone = 1234
phone = input("Please enter a phone number: ")

# update_sql = "UPDATE contacts SET email= '{}' WHERE phone={}".format(new_email, phone)
update_sql = "UPDATE contacts SET email= ? WHERE phone=?"
print(update_sql)

update_cursor = db.cursor()
# update_cursor.execute(update_sql)
update_cursor.execute(update_sql, (new_email, phone))
# update_cursor.executescript(update_sql)
print("{} rows updated".format(update_cursor.rowcount))

print()
print("Are connections the same: {}".format(update_cursor.connection == db))
print()

update_cursor.connection.commit()
update_cursor.close()

for name, phone, email in db.execute("SELECT * FROM contacts"):
    print(name)
    print(phone)
    print(email)
    print("*" * 20)

db.close()


