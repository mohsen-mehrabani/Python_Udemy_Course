import shelve
# with shelve.open("bike") as bike:
#     bike["make"] = "Honda"
#     bike["model"] = "250 dream"
#     bike["colour"] = "red"
#     bike["engine_size"] = 250
#
#     print(bike["make"])
#     print(bike["model"])
# --------------------------------------------
# we do that for the reason that the Python is persistent in file and it never check for correcting it
# with shelve.open("bike_2") as bike:
#     bike["make"] = "Honda"
#     bike["model"] = "250 dream"
#     bike["colour"] = "red"
#     bike["engin_size"] = 250
#
#     print(bike["make"])
#     print(bike["engine_size"])
#  for checking it I correct the engin to engine and run it again
# with shelve.open("bike_2") as bike:
#     bike["make"] = "Honda"
#     bike["model"] = "250 dream"
#     bike["colour"] = "red"
#     bike["engine_size"] = 250
#
#     for key in bike:
#         print(key)
#     print("=" * 40)
#     print(bike["make"])
#     print(bike["engine_size"])
#     print(bike["engin_size"])
# ----------------------------------------------------
#  for correcting it we can delete the engin_size entry
with shelve.open("bike_2") as bike:
    bike["make"] = "Honda"
    bike["model"] = "250 dream"
    bike["colour"] = "red"
    bike["engine_size"] = 250

    del bike["engin_size"]

    for key in bike:
        print(key)
    print("=" * 40)
    print(bike["make"])
    print(bike["engine_size"])
# I know you get an error and it's because of that when you run this code you have deleted it so it is not exist know ;-)
