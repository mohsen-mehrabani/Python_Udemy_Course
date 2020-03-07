# for i in range(17):
#     print("{0:<2} in Hex is {0:>02x}".format(i))
# print("=" * 40)
# a = 0x20
# b = 0x0a
# print(a)
# print(b)
# print(a * b)
#
# print(0b00101010)
# print(0b101010)
# print(0B00101010)
# print(0B101010)
# print(0x45)
# ----------------------------------------------------------------------
powers = []
for power in range(15, -1, -1):
    powers.append(2 ** power)
print(powers)
x = int(input("Please enter a number: "))
printing = False
for power in powers:
    bit = x // power
    if bit != 0 or power == 1:
        printing = True
    if printing:
        print(bit, end='')
    x %= power
