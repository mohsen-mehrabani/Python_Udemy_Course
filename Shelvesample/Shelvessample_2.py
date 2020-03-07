import shelve
fruit = shelve.open('ShelfTest')
while True:
    dict_key = input("Please enter a fruit: ")
    if dict_key == "quit":
        break
    if dict_key in fruit:
        description = fruit[dict_key]
        print(description)
    else:
        print("We don't have a " + dict_key)
fruit.close()
