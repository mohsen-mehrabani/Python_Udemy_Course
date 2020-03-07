# write a program to append the times table to our jabberwocky poem in sample.txt
# We want the tables for 2 to 12 (similar to the output from the FOR LOOPS part 2 lecture
# in section 6)
with open("061 sample.txt", 'a') as tables:
    for i in range(2, 13):
        for j in range(1, 13):
            print("{1:>2} times {0} is {2}".format(j, i, i*j), file=tables)
        print("="*20, file=tables)

