# # *args
# def average(*args):
#     print(type(args))
#     print(*args)
#     mean = 0
#     for arg in args:
#         mean += arg
#     return mean / len(args)
#
#
# print(average())


# def print_backwards(*args, file=None):
#     for word in args[::-1]:
#         print(word[::-1], end=' ', file=file)
#
#
# with open("backwards.text", 'w') as backwards:
#     print_backwards("hallo", "worlds", file=backwards)


# def print_backwards(*args, end='', **kwargs):     # First solution
def print_backwards(*args, **kwargs):
    end_character = kwargs.pop('end', '\n')
    sep_character = kwargs.pop('sep', ' ')

    kwargs.pop('end', None)                       # Second solution
    for word in args[::-1]:
        print(word[::-1], end=' ', **kwargs)

    print(end=end_character)


with open("backwards.text", 'w') as backwards:
    # print_backwards("hallo", "worlds", file=backwards, end='\n')
    print_backwards("hallo", "worlds", end='\n')
