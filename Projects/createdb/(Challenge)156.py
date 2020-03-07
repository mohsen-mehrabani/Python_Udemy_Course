import sqlite3

conn = sqlite3.connect("contacts.db")
name = input("Please input the name which you want to update: ")
update_outcome = input(" update email to : ")

# My first approach
# update_base_on_name = "update contacts SET email= '{}' WHERE name = '{}' ".format(update_outcome, name)
# conn.execute(update_base_on_name)

# My second approach
update_base_on_name = "update contacts SET email= ? WHERE name LIKE ? "
conn.execute(update_base_on_name, (update_outcome, name))

conn.commit()
for row in conn.execute("SELECT * FROM contacts"):
    print(row)
conn.close()

