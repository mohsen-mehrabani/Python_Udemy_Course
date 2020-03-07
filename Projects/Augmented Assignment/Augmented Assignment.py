# Augmented Assignment means additional exercise
number = "9,231,254,367,256,254,996,777"
CleanedNumber = ''
for i in range(0, len(number)):
    if number[i] in "0123456789":
        CleanedNumber = CleanedNumber + number[i]
NewNumber = int(CleanedNumber)
print("")
print("The number is {}".format(NewNumber))

# --------------------------------------------------------------

number = "9,231,254,367,256,254,996,777"
CleanedNumber = ''
for i in range(0, len(number)):
    if number[i] in "0123456789":
        CleanedNumber += number[i]
NewNumber = int(CleanedNumber)
print("")
print("The number is {}".format(NewNumber))
