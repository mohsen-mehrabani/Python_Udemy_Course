with open("check_file.text", 'r') as check_list:
    for line in check_list:
        checklist_1 = tuple(check_list)

with open("albums.txt",'r') as album:
    for line_1 in album:
        cheklist_2 = tuple(album)

if checklist_1 == cheklist_2:
    print("yes")
else:
    print("No")