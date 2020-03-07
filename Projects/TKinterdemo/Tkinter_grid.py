# try:
#     import tkinter
# except ImportError:
#     import Tkinter as tkinter
import tkinter

main_window = tkinter.Tk()
main_window.title('Hello world!')
main_window.geometry("700x500")

j_label = tkinter.Label(text="Oh My God")
j_label.grid(row=0, column=1)

right_frame = tkinter.Frame(main_window)
right_frame.grid(row=1, column=3)

j_canvas = tkinter.Canvas(right_frame, relief='raised', borderwidth=5)
j_canvas.grid(row=1, column=3)

left_frame = tkinter.Frame(main_window)
left_frame.grid(row=1, column=1, sticky='n')

button1 = tkinter.Button(left_frame, text='Number 1', borderwidth=3)
button2 = tkinter.Button(left_frame, text='Number 2', borderwidth=3)
button3 = tkinter.Button(left_frame, text='Number 3', borderwidth=3)
button4 = tkinter.Button(left_frame, text='Number 4', borderwidth=3)

button1.grid(row=0, column=0)
button2.grid(row=1, column=0)
button3.grid(row=2, column=0)
button4.grid(row=3, column=0)

main_window.columnconfigure(0, weight=1)
main_window.columnconfigure(1, weight=1)
main_window.grid_columnconfigure(2, weight=1)

left_frame.config(relief='sunken', borderwidth=2)
right_frame.config(relief='sunken', borderwidth=2)
left_frame.grid(sticky='nw')
right_frame.grid(sticky='wn')

button1.grid(sticky='s')

main_window.mainloop()
