import sqlite3

db = sqlite3.connect("contacts.db")
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts (name, phone, email) VALUES ('Tim', 1234, 'Tim@my-email.com')")
db.execute("INSERT INTO contacts VALUES ('Ali', 1234, 'Ali@email.com')")
db.execute("INSERT INTO contacts VALUES ('Eli', 1234, 'Eli@email.com')")

cursor = db.cursor()
cursor.execute("select * from contacts")

for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)
    print("_" * 20)

cursor.close()
db.commit()
db.close()
