import shelve
# blt = ["bacon", "lettuce", "tomato", "bread"]
# beans_on_toast = ["beans", "bread"]
# scrambled_eggs = ["eggs", "butter", "bread"]
# pasta = ["pasta", "cheese"]
soup = ["tin of soup"]
with shelve.open("Recipes") as recipes:
    # recipes["blt"] = blt
    # recipes["beans_on_toast"] = beans_on_toast
    # recipes["scrambled_eggs"] = scrambled_eggs
    # recipes["pasta"] = pasta
    # recipes["soup"] = soup
    # ______________________________________________________
    # recipes["blt"].append("butter")
    # recipes["pasta"].append("tomato")
    # --------------------------------------------------------
    #                      It doesn't work because python write it on ram  not disk.
    #                      you have to append it to a temp file and then append it like this

    # Temp_list = recipes["blt"]
    # Temp_list.append("butter")
    # recipes["blt"] = Temp_list
    # Temp_list = recipes["pasta"]
    # Temp_list.append("tomato")
    # recipes["soup"] = Temp_list
    #               we run it and it appended to the DB so we don't need it again
    #               so I commented it :-)
    for snack in recipes:
        print(snack, recipes[snack])
