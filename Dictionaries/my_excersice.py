# This is just for my exercise
fruit = {"orange": "a sweet, orange, citrus fruit", "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit", "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit", "pear": "great with tequila"}
# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#     description = fruit.get(dict_key, "we don't have a " + dict_key)
#     print(description)
# -----------------------------------------------
# The first approach
# -----------------------------------------------

# ordered_keys = list(fruit.keys())
# ordered_keys.sort()
# for i in ordered_keys:
#     print(i + " : " + fruit[i])
# -----------------------------------------------
# The second one
# -----------------------------------------------
# ordered_keys = sorted(list(fruit.keys()))
# for j in range(11):
#     for i in ordered_keys:
#         print(i + " : " + fruit[i])
#     print("=" * 40)
# -----------------------------------------------
# The third one
# -----------------------------------------------
# for val in fruit:
#     print(val)
# -----------------------------------------------
# The fourth approach which is less efficient
# -----------------------------------------------
# for val in fruit.values():
#     print(val)

# print(fruit.keys())
# print(fruit.values())

# fruit_keys = fruit.keys()
# print(fruit_keys)
# fruit["tomato"] = "Not delicious with ice cream"
# print(fruit.keys())

# x = fruit.items()
# print(type(x))
# ------------------------------------------------------------


f_tuple = tuple(fruit.items())
print(type(f_tuple))
print(f_tuple)

# for snack in f_tuple:
#     item, description = snack
#     print(item + " is " + description)
# ------------------------------------------------------------
# for comparison
# ------------------------------------------------------------
# f_tuple = tuple(fruit.values())
# print(type(f_tuple))
# print(f_tuple)
#
# for snack in f_tuple:
#     item, description = snack
#     print(item + " is " + description)
# ------------------------------------------------------------
# f_tuple = tuple(fruit.keys())
# print(type(f_tuple))
# print(f_tuple)
#
# for snack in f_tuple:
#     item, description = snack
#     print(item + " is " + description)
# ------------------------------------------------------------
print(dict(f_tuple))



















