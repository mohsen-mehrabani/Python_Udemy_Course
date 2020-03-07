import shelve
fruit = shelve.open("ShelfTest")
# ordered_keys = list(fruit.keys())
# sorted(ordered_keys)
# for F in ordered_keys:
#     print(F + " :" + fruit[F])
for V in fruit.values():
    print(V)
print(fruit.values())

for f in fruit.items():
    print(f)

print(fruit.items())
