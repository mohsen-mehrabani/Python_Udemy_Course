import time
# help(time)
print("The epoch on this system started at " + time.strftime('%c', time.gmtime(0)))
print("the current timezone is {0} with no offset of {1}".format(time.tzname[0], time.timezone))
if time.daylight != 0:
    print("\t Day Light Saving time is in effect for this region ")
    print("\t The DST timezone is " + time.tzname[1])

print("The Local time is " + time.strftime('%Y_%m_%d %H:%M:%S', time.localtime()))
print("The UTC time is " + time.strftime('%Y_%m_%d %H:%M:%S', time.gmtime()))



