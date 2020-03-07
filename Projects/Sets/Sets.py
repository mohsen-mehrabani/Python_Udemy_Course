# print("=" * 100)
# farm_animals = {"sheep", "cow", "hen"}
# print(farm_animals)
# print(type(farm_animals))
# print()
# for animal in farm_animals:
#     print(animal)
# print("=" * 50)
# wild_animals = set(["lion", "tiger", "panther", "elephant", "hare"])
# print(wild_animals)
# farm_animals.add("horse")
# wild_animals.add("horse")
# print(wild_animals)
# print(farm_animals)
# -------------------------
# empty_set = set()
# empty_set2 = {}
# empty_set.add("a")
# # empty_set2.add("a")
# even = set(range(0, 40, 2))
# print(even)
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print(squares)
# -------------------------------
# even = set(range(0, 40, 2))
# print(even)
# print(len(even))
# square_tuple = (4, 6, 9, 16, 25)
# square = set(square_tuple)
# print(square)
# print(len(square))
# print(even.union(square))
# print(len(even.union(square)))
# print(square.union(even))
# print(len(square.union(even)))
# print(even)
# print(square)
# print(even.intersection(square))
# print((even & square))
# print(square.intersection(even))
# print(square & even)
# -----------------------------------
# even = set(range(0, 40, 2))
# square_tuple = (4, 6, 9, 16, 25)
# print(sorted(even))
# print(sorted(square_tuple))
# squares = set(square_tuple)
# print(sorted(squares))

print("=" * 40)
# print("The even is: ", sorted(even))
# print("The squares is: ", sorted(squares))
# print(" even minus squares ")
# print(sorted(even.difference(squares)))
# print(sorted(even - squares))
#
# print("squares minus even")
# print(squares.difference(even))
# print(squares - even)
# print(even)
# print(squares)
# even.difference_update(squares)
# print(sorted(even))
# even = set(range(0, 40, 2))
# print(sorted(even))
#
# square_tuple = (4, 6, 9, 16, 25)
# squares = set(square_tuple)
# print(sorted(square_tuple))

# print("Symmetric even minus square")
# print(sorted(even.symmetric_difference(squares)))
# print("Symmetric square minus even")
# print(squares.symmetric_difference(even))
# squares.discard(4)
# print(sorted(squares))
# if 4 in squares:
#     squares.remove(4)
# try:
#     squares.remove(4)
# except KeyError:
#     print("There is no iem 4!")
# print(sorted(squares))

# even = set(range(0, 40, 2))
# print(even)
#
# square_tuple = (4, 6, 16)
# squares = set(square_tuple)
# print(squares)
#
# if squares.issubset(even):
#     print("squares is subset of even")
#
# if even.issuperset(squares):
#     print("even is a superset of squares")

even = frozenset(range(0, 100, 2))
print(even)
even.add(3)


























