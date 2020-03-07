import sys


def getint(prompt):
    while True:
        try:
            number = int(input("please enter a number: "))
            return number
        except ValueError:
            print("Invalid number entered, try again ")
        except EOFError:
            sys.exit(1)


first_number = getint("Please enter first number: ")
second_number = getint("Please enter second number: ")

try:
    print("{} divided by {} is {}".format(first_number, second_number, first_number / second_number))
except ZeroDivisionError:
    print("Divide by Zero Error")
sys.exit(2)