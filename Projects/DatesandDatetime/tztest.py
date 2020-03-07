import pytz
import datetime
# country = 'Europe/Moscow'
# tz_to_display = pytz.timezone(country)
# local_time = datetime.datetime.now(tz_to_display)
# print("The zone time in {} is {}".format(country, local_time))
# print("The UTC zone time is {}".format(datetime.datetime.utcnow()))
# for x in pytz.all_timezones:
#     print(x)
# for x in sorted(pytz.country_names):
#     print(x + " :" + pytz.country_names[x])
# for x in sorted(pytz.country_names):
#     print("{} :{} is : {}".format(x, pytz.country_names[x], pytz.country_timezones.get(x)))
# for x in sorted(pytz.country_names):
#     print("{}: {}".format(x, pytz.country_names[x]), end=": ")
#     if x in pytz.country_timezones:
#         print(pytz.country_timezones[x])
#     else:
#         print("No time zone defined!")
# for x in sorted(pytz.country_names):
#     print("{}: {}".format(x, pytz.country_names[x]), end=": ")
#     if x in pytz.country_timezones:
#         for zone in sorted(pytz.country_timezones[x]):
#             tz_to_display = pytz.timezone(zone)
#             local_time = datetime.datetime.now(tz=tz_to_display)
#             print("\t\t{}: {}".format(zone, local_time))
#     else:
#         print("\t\tNo time zone defined!")
for x in sorted(pytz.country_names):
    print("{}: {}".format(x, pytz.country_names[x]), end=": ")
    if x in pytz.country_timezones:
        for zone in sorted(pytz.country_timezones[x]):
            tz_to_display = pytz.timezone(zone)
            local_time = datetime.datetime.now(tz=tz_to_display)
            print("\t\t{}: {}".format(zone, local_time))
    else:
        print("\t\tNo time zone defined!")
