import shelve
recipes = shelve.open("Recipes", writeback=True)
recipes["scrambled_eggs"].append("salt")
recipes["scrambled_eggs"].remove("salt")
# recipes["scrambled_eggs"].remove("salt")
for snack in recipes:
    print(snack, recipes[snack])



