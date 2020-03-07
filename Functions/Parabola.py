try:
    import tkinter
except ImportError:
    import Tkinter as tkinter


def parabola(x):
    y = x * x / 100
    return y


def draw_axes(page):
    page.update()
    x_origin = page.winfo_width() / 2
    y_origin = page.winfo_height() / 2
    page.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    page.create_line(-x_origin, 0, x_origin, 0, fill='black')
    page.create_line(0, y_origin, 0, -y_origin, fill='black')


def plot(canvas, x, y):
    canvas.create_line(x, y, x+1, y+1, fill="green")


main_window = tkinter.Tk()
main_window.title("Parabola")
main_window.geometry("640x480")

canvas = tkinter.Canvas(main_window, width=320, height=480)
canvas.grid(row=0, column=0)
canvas2 = tkinter.Canvas(main_window, width=320, height=480, background="red")
canvas2.grid(row=0, column=1)

draw_axes(canvas)
draw_axes(canvas2)

for x in range(-1000, 1000):
    y = parabola(x)
    plot(canvas, x, -y)
    plot(canvas2, x, -y)

main_window.mainloop()
