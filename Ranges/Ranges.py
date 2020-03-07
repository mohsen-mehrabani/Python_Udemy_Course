# my_list = list(range(10))
# print(my_list)
# even = list(range(0, 20, 2))
# odd = list(range(1, 20, 2))
# print(even)
# print(odd)
# ------------------------------------------------------------
# my_string = "abcdefghigklmnopqrstuvwxyz"
# print(my_string.index("e"))
# print(my_string[4])

# small_decimals = range(0, 10)
# print(small_decimals)
# print(small_decimals.index(3))
# ------------------------------------------------------------
# odd = range(1, 10000, 2)
# print(odd)
# a = odd[985]
# print(a)
# ------------------------------------------------------------
# sevens = range(7, 1000000, 7)
# x = int(input("Please enter a number less than one million: "))
# if x in sevens:
#     print("{} is divisible into seven!".format(x))
# else:
#     print("{} is not divisible to seven.".format(x))
# ------------------------------------------------------------
small_decimals = range(0, 10)
print(small_decimals)

my_range = small_decimals[::2]
print(my_range)
print(my_range.index(8))
print("=" * 20)
for number in my_range:
    print(number)


# 0123456789
# 02468




