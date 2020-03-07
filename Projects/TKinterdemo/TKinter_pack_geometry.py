# try:
#     import tkinter
# except ImportError:
#     import Tkinter as tkinter
import tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)

# tkinter._test()

main_window = tkinter.Tk()
main_window.title('Hello world!')
main_window.geometry("500x400")

j_label = tkinter.Label(text="Oh My God")
j_label.pack(side='top')

right_frame = tkinter.Frame(main_window)
right_frame.pack(side='right', anchor='e', fill=tkinter.Y, expand=True)

j_canvas = tkinter.Canvas(right_frame, relief='raised', borderwidth=5)
j_canvas.pack(side='left', anchor="n", fill=tkinter.Y)

left_frame = tkinter.Frame(main_window)
left_frame.pack(side='left', anchor='n', fill=tkinter.Y, expand=True)

button1 = tkinter.Button(left_frame, text='Number 1', borderwidth=3)
button2 = tkinter.Button(left_frame, text='Number 2', borderwidth=3)
button3 = tkinter.Button(left_frame, text='Number 3', borderwidth=3)
button4 = tkinter.Button(left_frame, text='Number 4', borderwidth=3)

button1.pack(side='top')
button2.pack(side='top')
button3.pack(side='top')
button4.pack(side='top')

main_window.mainloop()
