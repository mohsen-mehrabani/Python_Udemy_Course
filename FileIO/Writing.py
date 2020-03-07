#
# cities = ["Adelaide", "Alice Spring", "Darwin", "Melbourne", "Sydney"]
# with open("Cities_name.txt", 'w') as cities_file:
#     for city in cities:
#         print(city, file=cities_file)
#
# cities = []
# with open("Cities_name.txt", 'r') as cities_file:
#     for city in cities_file:
#         cities.append(city.strip("\n"))
# print(cities)
# for city in cities:
#     print(city)
#
# imelda = "More Mayhem", "Imelda May", "2001", (
#     (1, "Pulling thr Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))
# with open("imelda.txt", 'w') as imelda_file:
#     print(imelda, file=imelda_file)
#
with open("imelda.txt", 'r') as imelda_file:
    contents = imelda_file.readline()

imelda = eval(contents)
print(imelda)
title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
