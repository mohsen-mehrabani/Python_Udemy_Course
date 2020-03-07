import sqlite3

conn = sqlite3.connect("contacts.db")
# for row in conn.execute("SELECT * FROM contacts"):
for row in conn.execute("SELECT * FROM sqlite_master"):
    print(row)

conn.close()
