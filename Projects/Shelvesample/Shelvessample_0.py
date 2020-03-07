import shelve
with shelve.open('ShelfTest')as fruit:
    fruit['orange'] = "a sweet, orange, citrus fruit"
    fruit['apple'] = "good for making cider"
    fruit['lemon'] = "a sour, yellow citrus fruit "
    fruit['grape'] = "a small, sweet fruit growing in bunt"
    fruit['lime'] = "a sour, green citrus fruit"

    print(fruit["lime"])
    print(fruit["apple"])
    print(fruit["grape"])
print(fruit)

#     fruit = {"orange": "a sweet , orange, citrus fruit",
#              "apple": "good for making cider",
#              "lemon": "a sour, yellow citrus fruit",
#              "grape": "a small, sweet fruit growing in bunches",
#              "lime": "a sour, green citrus fruit"}
#     print(fruit["lime"])
#     print(fruit["apple"])
#
# print(fruit["apple"])
# print(fruit)
#
# fruit = shelve.open('ShelfTest')
# fruit['orange'] = "a sweet, orange, citrus fruit"
# fruit['apple'] = "good for making cider"
# fruit['lemon'] = "a sour, yellow citrus fruit "
# fruit['grape'] = "a small, sweet fruit growing in bunt"
# fruit['lime'] = "a sour, green citrus fruit"
#
# print(fruit["lime"])
# print(fruit["apple"])
# print(fruit["grape"])
# fruit.close()
# print(fruit)

