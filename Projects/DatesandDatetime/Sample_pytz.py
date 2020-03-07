import pytz
import datetime
# country = 'Europe/Moscow'
# tz_to_display = pytz.timezone(country)
# local_time = datetime.datetime.now(tz=tz_to_display)
# print("The UTC time is {}".format(datetime.datetime.utcnow()))
# print("The time in {} is {}".format(country, local_time))
# for x in sorted(pytz.all_timezones):
#     print(x, end="\t")
# for x in sorted(pytz.country_timezones):
#     # print("{}: {}".format(x, pytz.country_names[x]))
#     print( x + ": " + pytz.country_names[x])
for x in sorted(pytz.country_names):
    # print("{}: {}: {}".format(x, pytz.country_names[x], pytz.country_timezones(x)))
    print("{}: {}: {}".format(x, pytz.country_names[x], pytz.country_timezones.get(x)))

