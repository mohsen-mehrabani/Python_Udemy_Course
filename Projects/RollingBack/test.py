# import sqlite3
#
# con = sqlite3.connect("test.db")
# cur = con.cursor()
# cur.executescript("""
#     create table if not exists samples(
#         id,
#         value
#     );
#     insert into samples(id, value)
#     values (
#         '123',
#         'abcdef'
#     );
#     """)
# cur.execute("SELECT * from samples")
#
# print(cur.fetchone())
import pytz
import datetime
utc_time = pytz.utc.localize(datetime.datetime.utcnow())
local_time = utc_time.astimezone()
zone = local_time.tzinfo  # this is so helpful https://docs.python.org/2.4/lib/datetime-tzinfo.html
print(zone)
