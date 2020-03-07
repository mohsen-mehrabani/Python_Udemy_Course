# While loop
print("hi there")

# for i in range(0, 11):
#     print("i is now {}".format(i))
#
# i= 0
# while i < 11:
#     print(" i is now {}".format(i))
#     i += 1

available_exits = ["south", "north", "east"]
print("Chose a direction form %s, please" % available_exits)
for state in available_exits:
    print("the list is " + state)
print("Input q for exit!")
chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = input("Please input a direction: ")
    if chosen_exit == "q":
        print("Game Over!")
        break
else:
    print("aren't you glad you got out of there!")
