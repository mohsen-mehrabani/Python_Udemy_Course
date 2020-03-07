# create a program that takes some text and returns a list of
# all the characters in the text that are not vowels, sorted in
# alphabetical order.
# you can either enter the text for keyboard or
# initialise a string variable with the string
sample_test = "Python is a very powerful language"

vowels = frozenset("aeiou")
final_set = set(sample_test).difference(vowels)
print(final_set)
final_list = sorted(final_set)
print(final_list)

