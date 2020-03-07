import sqlite3
import pytz
import pickle

db = sqlite3.connect("contacts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)

# for row in db.execute("SELECT * FROM history"):
#     # print(row)
#     local_time = row[0]
#     print("{}\t{}".format(local_time, type(local_time)))
# for row in db.execute("SELECT strftime('%Y-%m-%d %H:%M:%f',history.time, 'localtime') as localtime,"
#                       " history.account, history.amount from history order by history.time"):
for row in db.execute("SELECT * from history"):
    utc_time = row[0]
    picked_zone = row[3]
    zone = pickle.loads(picked_zone)
    local_time = pytz.utc.localize(utc_time).astimezone(zone)
    print("{}\t{}\t{}".format(utc_time, local_time, local_time.tzinfo))

db.close()
