import sqlite3

try:
    import tkinter
except ImportError:  # python2
    import Tkinter as tkinter


class Scrollbar(tkinter.Listbox):
    def __init__(self, windows, **kwargs):
        # tkinter.Listbox.__init__(self, windows, **kwargs)     # for Python 2
        super().__init__(windows, **kwargs)
        self.scrollbar = tkinter.Scrollbar(windows, orient=tkinter.VERTICAL, command=self.yview)

    def grid(self, row, column, sticky='nsw', rowspan=1, columnspan=1, **kwargs):
        # tkinter.Listbox.grid(row=row, column=column, sticky=sticky, rowspan=rowspan,
        # columnspan=columnspan, **kwargs)  # for Python 2
        super().grid(row=row, column=column, sticky=sticky, rowspan=rowspan, columnspan=columnspan, **kwargs)
        self.scrollbar.grid(row=row, column=column, sticky='nse', rowspan=rowspan)
        self['yscrollcommand'] = self.scrollbar.set


class DataListBox(Scrollbar):
    def __init__(self, windows, connection, table, field, sort_order=(), **kwargs):
        # Scrollbar.__init__(self, windows, **kwargs) # for python 2
        super().__init__(windows, **kwargs)
        self.linked_box = None
        self.link_field = None
        self.cursor = connection.cursor()
        self.table = table
        self.field = field
        self.bind('<<ListboxSelect>>', self.on_select)
        self.sql_select = "SELECT " + self.field + ", _id" + " FROM " + self.table
        if sort_order:
            self.sql_sort = " ORDER BY " + ','.join(sort_order)
        else:
            self.sql_sort = " ORDER BY " + self.field

    def clear(self):
        self.delete(0, tkinter.END)

    def link(self, widget, link_field):
        self.linked_box = widget
        widget.link_field = link_field

    def requery(self, link_value=None):
        if link_value and self.link_field:
            sql = self.sql_select + " WHERE " + self.link_field + "=?" + self.sql_sort
            print(sql)          # TODO delete this line
            self.cursor.execute(sql, (link_value,))
        else:
            print(self.sql_select + self.sql_sort)      # TODO delete this line
            self.cursor.execute(self.sql_select + self.sql_sort)

        # clear the ListBox contents before reloading
        self.clear()
        for value in self.cursor:
            self.insert(tkinter.END, value[0])

        if self.linked_box:
            self.linked_box.clear()

    def on_select(self, event):
        if self.linked_box:
            print(self is event.widget)     # TODO Delete this message
            index = self.curselection()[0]
            value = self.get(index),

            # get the artist ID from the database row
            link_id = self.cursor.execute(self.sql_select + " WHERE " + self.field + "=?", value).fetchone()[1]
            self.linked_box.requery(link_id)


if __name__ == '__main__':
    conn = sqlite3.connect("music.sqlite")
    mainWindow = tkinter.Tk()
    mainWindow.title('Music DB Browser')
    mainWindow.geometry('1080x768')

    mainWindow.columnconfigure(0, weight=2)
    mainWindow.columnconfigure(1, weight=2)
    mainWindow.columnconfigure(2, weight=2)
    mainWindow.columnconfigure(3, weight=1)  # spacer column in right

    mainWindow.rowconfigure(0, weight=1)
    mainWindow.rowconfigure(1, weight=5)
    mainWindow.rowconfigure(2, weight=5)
    mainWindow.rowconfigure(3, weight=1)

    # =========Labels=================
    tkinter.Label(mainWindow, text='Artists').grid(row=0, column=0)
    tkinter.Label(mainWindow, text='Albums').grid(row=0, column=1)
    tkinter.Label(mainWindow, text='Songs').grid(row=0, column=2)

    # =========Artists ListBox========
    artistList = DataListBox(mainWindow, conn, "artists", "name")
    artistList.grid(row=1, column=0, sticky='nsew', rowspan=2, padx=(30, 0))
    artistList.config(border=2, relief='sunken')
    artistList.requery()

    # =========Albums ListBox========
    albumLV = tkinter.Variable(mainWindow)
    albumLV.set(('Choose an artist',))
    albumList = DataListBox(mainWindow, conn, "albums", "name", sort_order=("name",))
    albumList.grid(row=1, column=1, sticky='nsew', padx=(30, 0))
    albumList.config(border=2, relief='sunken')

    artistList.link(albumList, "artist")

    # ========Songs ListBox==========
    songLV = tkinter.Variable(mainWindow)
    songLV.set(('Choose an album',))
    songsList = DataListBox(mainWindow, conn, "songs", "title", ("track", "title"))
    songsList.grid(row=1, column=2, sticky='nsew', padx=(30, 0))
    songsList.config(border=2, relief='sunken')

    albumList.link(songsList, "album")

    # =======mainloop================
    print("Closing database connection")
    mainWindow.mainloop()

    conn.close()
