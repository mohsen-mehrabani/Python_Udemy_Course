import shelve
fruit = shelve.open("ShelfTest")
# for key in fruit:
#     print(key, ":", fruit[key])
while True:
    shelf_key = input("Please enter a fruit: ")
    if shelf_key == "quit":
        break
    description = fruit.get(shelf_key, "We don't have a " + shelf_key)
    print(description)
# dictionary.get(keyname, value)
# Parameter Values
# Parameter	Description
# keyname	Required. The keyname of the item you want to return the value from
# value	Optional. A value to return if the specified key *****does not exist*****.
# Default value None

fruit.close()
print(fruit)
