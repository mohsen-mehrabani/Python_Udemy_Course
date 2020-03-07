fruit = {"orange": "a sweet, orange, citrus fruit", "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit", "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit", "pear": "great with tequila"}
# print(fruit)
# print(fruit["lemon"])
# print(fruit["apple"])
# print(type(fruit))
# print(fruit)
# print([fruit])
# print(fruit)
# del(fruit["pear"])
# del fruit
# fruit.clear()
print(fruit)
# print(fruit["tomato"])
# while True:
#     dict_key = input("Please enter a fruit :")
#     if dict_key == "quit":
#         break
#     if dict_key in fruit:
#         description = fruit.get(dict_key)
#         print(description)
#     else:
#         print("we don't have a " + dict_key)
# ---------------------------------------------------------
while True:
    dict_key = input("Please enter a fruit :")
    if dict_key == "quit":
        break
    description = fruit.get(dict_key, "we don't have a " + dict_key)
    print(description)
