fruit = {"orange": "a sweet , orange, citrus fruit",
         "apple ": "good for making cider",
         "lemon":  "a sour, yellow citrus fruit",
         "grape":  "a small, sweet fruit growing in bunches",
         "lime":   "a sour, green citrus fruit"}


veg = {"cabbage": "every child's favorite",
       "sprouts": "mmmmmm, lovely",
       "spinach": "can I have some more fruit, please"}

# print(" the veg is :", veg)
# veg.update(fruit)
# print("the veg.update(fruit) is :", veg)
# print("the fruit is :", fruit)
# fruit.update(veg)
# print("the fruit.update(veg) is :", fruit)
print(fruit)
nice_and_nasty = fruit.copy()
print(nice_and_nasty)
print("=" * 50)
nice_and_nasty.update(veg)
print(nice_and_nasty)

