# jabber = open("/home/mohsen/IdeaProjects/Code/061 sample.txt", 'r')
#
# for line in jabber:
#     if "jabberwock" in line.lower():
#         print(line, end="")
#
# jabber.close()
#
# with open("061 sample.txt", 'r') as jabber:
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end='')
#
# with open("061 sample.txt", 'r') as jabber:
#     line = jabber.readline()
#     for line in jabber:
#         print(line)
# with open("061 sample.txt", 'r') as jabber:
#     line = jabber.readline()
#     while line:
#         line = jabber.readline()
#         print(line, end='')
#
# with open("061 sample.txt", 'r') as jabber:
#     lines = jabber.readlines()
# print(lines)
# for line in lines:
#     print(line, end='')
#
# with open("061 sample.txt", 'r') as jabber:
#     lines = jabber.read()
# for line in lines:
#     print(line, end="")
#
with open("061 sample.txt", 'r')as jabber:
    lines = jabber.read()
for line in lines[::-1]:
    print(line, end="")
