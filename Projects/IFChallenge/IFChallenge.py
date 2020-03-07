# Write a small program to ask for a name and an age.
# When both values have been entered, check if the person
# is the right age to go on an 18-30 holiday (they must be
# over 18 and under 31).
# If they are, welcome them to thw holiday, otherwise print
# a (polite) message refusing them entry.

name = input("Enter your name: ")
age = int(input("Enter your age: "))
if 18 <= age <= 31:
    print("Dear %s, you are qualified to go on an 18-30 days holiday" % name)
    print("Dear {}, you are qualified to go on an 18-30 days holiday".format(name))
else:
    print("We are sorry, {},you are not qualified for going to an 18-30 days holiday".format(name))


