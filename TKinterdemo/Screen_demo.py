try:
    import tkinter
except ImportError:
    import Tkinter as tkinter
import os

mainWindow = tkinter.Tk()
mainWindow.title("Grid Demo")
mainWindow.geometry("640x480-8-200")
mainWindow['padx'] = 5
label = tkinter.Label(mainWindow, text="Tkinter Grid Demo")
label.grid(row=0, column=0, sticky='w', columnspan=3)

mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=3)
mainWindow.columnconfigure(3, weight=3)
mainWindow.columnconfigure(4, weight=3)
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=10)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=3)
mainWindow.rowconfigure(4, weight=3)

fileList = tkinter.Listbox(mainWindow)
fileList.grid(row=1, column=0, sticky='nsew')
fileList.config(border=2, relief='sunken')

for zone in os.listdir('/usr/bin'):
    fileList.insert(tkinter.END, zone)

listScroll_V = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=fileList.yview)
listScroll_V.grid(row=1, column=1, sticky='nsw', rowspan=1)
fileList['yscrollcommand'] = listScroll_V.set
listScroll_H = tkinter.Scrollbar(mainWindow, orient=tkinter.HORIZONTAL, command=fileList.xview)
listScroll_H.grid(row=2, column=0, sticky='enw', columnspan=1)
fileList['xscrollcommand'] = listScroll_H.set

# frame for the radio buttons
optionFrame = tkinter.LabelFrame(mainWindow, text="File Details")
optionFrame.grid(row=1, column=2, sticky='wn')

rbValue = tkinter.IntVar()
rbValue.set(3)
# Radio buttons
radio1 = tkinter.Radiobutton(optionFrame, text="FileName", value=1, variable=rbValue)
radio2 = tkinter.Radiobutton(optionFrame, text="Path", value=2, variable=rbValue)
radio3 = tkinter.Radiobutton(optionFrame, text="TimeStamp", value=3, variable=rbValue)
radio1.grid(row=0, column=0, sticky='w')
radio2.grid(row=1, column=0, sticky='w')
radio3.grid(row=2, column=0, sticky='w')

# widget to display the result
resultLabel = tkinter.Label(mainWindow, text="Result")
resultLabel.grid(row=1, column=2, sticky='sw')
result = tkinter.Entry(mainWindow)
result.grid(row=2, column=2, sticky='sw')

# Frame for the time spinner
timeFrame = tkinter.Label(mainWindow, text="time")
timeFrame.grid(row=3, column=0, sticky='new')

# time spinner
hourSpinner = tkinter.Spinbox(timeFrame, width=2, values=tuple(range(0, 24)))
minuteSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)
secondSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)
hourSpinner.grid(row=0, column=0)
tkinter.Label(timeFrame, text=":").grid(row=0, column=1)
minuteSpinner.grid(row=0, column=2)
tkinter.Label(timeFrame, text=":").grid(row=0, column=3)
secondSpinner.grid(row=0, column=4)
timeFrame['padx'] = 36

# Frame for the date spinners
dateFrame = tkinter.Frame(mainWindow)
dateFrame.grid(row=4, column=0, sticky='new')

# Date label
dayLabel = tkinter.Label(dateFrame, text='Day')
monthLabel = tkinter.Label(dateFrame, text='Month')
yearLabel = tkinter.Label(dateFrame, text='Year')
dayLabel.grid(row=0, column=0, sticky='w')
monthLabel.grid(row=0, column=1, sticky='w')
yearLabel.grid(row=0, column=2, sticky='w')

# Date spinner
day_spin = tkinter.Spinbox(dateFrame, width=5, from_=1, to=31)
month_spin = tkinter.Spinbox(dateFrame, width=5, values=('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug'
                                                         'Sep', 'Oct', 'Nov', 'Dec'))
year_spin = tkinter.Spinbox(dateFrame, width=5, from_=2000, to=2099)
day_spin.grid(row=1, column=0)
month_spin.grid(row=1, column=1)
year_spin.grid(row=1, column=2)

# Buttons
okButton = tkinter.Button(mainWindow, text='OK')
cancelButton = tkinter.Button(mainWindow, text='Cancel', command=mainWindow.quit)
okButton.grid(row=4, column=3, sticky='e')
cancelButton.grid(row=4, column=4, sticky='w')

mainWindow.mainloop()
print(rbValue.get())
