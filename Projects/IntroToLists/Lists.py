# The usage of lists in python
# parrot_list = ["non pinin", "no more", "a stiff", "bereft of life"]
# parrot_list.append("a Norwegian Blue")
#
# for state in parrot_list:
#     print("This parrot is {}".format(state))
# print("")
# for state in parrot_list:
#     print("This parrot is a " + state)
# ------------------------------------------------------------
# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7]
# numbers = odd + even
# print(numbers)
# sort_numbers = sorted(numbers)
# print(sort_numbers)
# if numbers == sort_numbers:
#     print("The lists are equal!")
# else:
#     print("The lists aren't equal!")
#
# if sort_numbers == sorted(numbers):
#     print("The lists are equal!")
# else:
#     print("The lists aren't equal!")
# -----------------------------------------------------------------------
# list_1 = []
# list_2 = list()
#
# print("list_1 is {}".format(list_1))
# print("list_2 is {}".format(list_2))
#
# if list_1 == list_2:
#     print("The lists are equal!")
# else:
#     print("The lists aren't equal!")
# print(list("The lists are equal!"))
# --------------------------------------------------------------------------
# even = [2, 4, 6, 8]
# r_even = even
# r_even.sort(reverse=True)
# print(r_even)
# print(even)
# --------------------------------------------------------------------------
# even = [2, 4, 6, 8]
# r_even = list(even)
# print(even is r_even)
# r_even.sort(reverse=True)
# print(r_even)
# --------------------------------------------------------------------------
# even = [2, 4, 6, 8]
# r_even = sorted(even, reverse=True)
# print(r_even)
# print(even)
# --------------------------------------------------------------------------
# even = [2, 4, 6, 8]
# r_even = sorted(even, reverse=True)
# print(r_even)
# print(even)
# print(r_even is even)
# print(r_even == even)
# --------------------------------------------------------------------------
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7]
numbers = [even, odd]
print(numbers)
for number_set in numbers:
    print(number_set)

    for value in number_set:
        print(value)

        # for second_value in value:
        #     print(second_value)




















