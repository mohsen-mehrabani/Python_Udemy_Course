# import time
# print(time.gmtime())
# # print(time.localtime())
# # print(time.time())
# print("=" * 60)
# time_here = time.localtime()
# print(time_here)
# print("=" * 60)
# print("year: ", time_here[0], time_here.tm_year)
# print("month: ", time_here[1], time_here.tm_mon)
# print("day :", time_here[2], time_here.tm_mday)

import time
from time import time as my_timer
import random

input("Press enter to start")

wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = my_timer()
input("Press enter to stop")

end_time = my_timer()

print("Started at " + time.strftime("%X", time.localtime(start_time)))
print("Stopped at " + time.strftime("%X", time.localtime(end_time)))

print("Your react time was {} second ".format(end_time - start_time))

