# ------------------------------------------------------------
IpAddress = input("Please enter an IP address: ")

# print("You have entered {}".format(IpAddress))
# print("You have entered %s " % IpAddress)

segment = 1
segment_length = 0
character = '' 

for character in IpAddress:
    if character == ".":
        print("Segment {} contains {} length".format(segment, segment_length))
        segment += 1
        segment_length = 0

    else:
        segment_length += 1


if character != ".":
    print("Segment {} contains {} length".format(segment, segment_length))







