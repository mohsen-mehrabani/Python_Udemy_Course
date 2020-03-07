from tkinter import *

root = Tk()
root.title("Alphabet Street")
root.Geometry = '11352×700'
root.configure(background='white')
# https://www.tutorialspoint.com/python/tk_cursors.htm
# for cursors {arrow" "circle""clock""cross""dotbox""exchange""fleur""heart""heart""man""mouse""pirate""plus""shuttle"
# "sizing""spider""spraycan""star""target""tcross""trek""watch"
# https://www.tutorialspoint.com/python/tk_relief.htm
# for relief use ( FLAT RAISED  SUNKEN  GROOVE  RIDGE )
# https://htmlcolorcodes.com/
ABC = Frame(root, bg="red", bd=15, relief=RIDGE, cursor="watch")
ABC.grid()
ABC1 = Frame(ABC, bg='blue', bd=10, relief=RIDGE, cursor="arrow")
ABC1.grid(row=0, column=0, sticky='w')
ABC2 = Frame(ABC, bg="#33ff90", bd=10, relief=RIDGE)
ABC2.grid(row=1, column=0, sticky='w')
pad = StringVar()
z = StringVar()

lb1Title = Label(ABC1, text=" \t\tAlphabet Street\t\t", font=('aria1', 30, 'bold'), padx=9, pady=9, bd=8,
                 bg="Cadet Blue", fg="Cornsilk", justify=CENTER).grid(row=0, column=1, columnspan=5)

for q in range(40):
    pad = (z, chr(q))
alphabet_pad = str(pad)

# alphabet_pad = "ABCDEFGHIJKLMNOPQRSTUVWXYZ\t\t\t\t\t"

i = 0
btn = []
for j in range(1, 7):
    for k in range(5):
        btn.append(Button(ABC2, width=9, height=1, font=('aria1', 22, 'bold'), bd=4, text=alphabet_pad[i]))
        btn[i].grid(row=j, column=k, pady=8, padx=8)
        i += 1

root.mainloop()
