def python_food():
    width = 80
    text = "spams and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


# def center_text(text):
#     text = str(text)
#     left_margin = (80 - len(text)) // 2
#     print(" " * left_margin, text)
def center_text(*args, sep=' ', end='\n', file=None, flush=False):
    text = ""
    for arg in args:
        text += str(arg) + sep
    # text = "".join(str(args))
    left_margin = (80 - len(text)) // 2
    return " " * left_margin + text


# with open("centered", mode="w") as centered_file:
print(center_text("spams and eggs"))
print(center_text("spam, spams and eggs"))
print(center_text(" spam , spam , spams and eggs "))
print("spam, spam, spams and eggs", 12, 5, sep=":::")
print(center_text(12))

print("=" + str(12 * 3))
print(sorted(["B", "C", "D", "A"]))