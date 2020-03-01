import sqlite3

try:
    import tkinter
except ImportError:  # python2
    import Tkinter as tkinter

conn = sqlite3.connect("music.sqlite")


class Scrollbar(tkinter.Listbox):
    def __init__(self, windows, **kwargs):
        # tkinter.Listbox.__init__(self, windows, **kwargs)     # for Python 2
        super().__init__(windows, **kwargs)
        self.scrollbar = tkinter.Scrollbar(windows, orient=tkinter.VERTICAL, command=self.yview)

    def grid(self, row, column, sticky='nse', rowspan=1, columnspan=1, **kwargs):
        # tkinter.Listbox.grid(row=row, column=column, sticky=sticky, rowspan=rowspan,
        # columnspan=columnspan, **kwargs)  # for Python 2
        super().grid(row=row, column=column, sticky=sticky, rowspan=rowspan, columnspan=columnspan, **kwargs)
        self.scrollbar.grid(row=row, column=column, sticky='nse', rowspan=rowspan)
        self['yscrollcommand'] = self.scrollbar.set


class DataListBox(Scrollbar):
    def __init__(self, windows, connection, table, field, sort_order=(), **kwargs):
        # Scrollbar.__init__(self, windows, **kwargs) # for python 2
        super().__init__(windows, **kwargs)
        self.cursor = connection.cursor()
        self.table = table
        self.field = field
        self.sql_select = "SELECT " + self.field + ", _id" + " FROM " + self.table
        if sort_order:
            self.sql_sort = " ORDER BY " + ','.join(sort_order)
        else:
            self.sql_sort = " ORDER BY " + self.field

    def clear(self):
        self.delete(0, tkinter.END)

    def requery(self):
        print(self.sql_select + self.sql_sort)      # TODO delete this line
        self.cursor.execute(self.sql_select + self.sql_sort)
        # clear the ListBox contents before reloading
        self.clear()
        for value in self.cursor:
            self.insert(tkinter.END, value[0])


def get_albums(event):
    lb = event.widget
    index = lb.curselection()[0]
    artist_name = lb.get(index),

    # get the artist ID from the database row
    artist_id = conn.execute("SELECT artists._id FROM artists WHERE artists.name = ?", artist_name).fetchone()
    alist = []
    for row in conn.execute("SELECT albums.name FROM albums WHERE albums.artist = ? ORDER BY albums.name", artist_id):
        alist.append(row[0])
    albumLV.set(tuple(alist))
    songLV.set(("Choose an album",))


def get_songs(event):
    lb = event.widget
    index = int(lb.curselection()[0])
    albums_name = lb.get(index),
    # get the artist ID from the database row
    albums_id = conn.execute("SELECT albums._id FROM albums WHERE albums.name=?", albums_name).fetchone()
    alist = []
    for x in conn.execute("SELECT songs.title FROM songs WHERE songs.album=? ORDER BY songs.track", albums_id):
        alist.append(x[0])
    songLV.set(tuple(alist))


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
# for artist in conn.execute("select artists.name from artists order by artists.name"):
#     artistList.insert(tkinter.END, artist[0])

artistList.bind('<<ListboxSelect>>', get_albums)

# =========Albums ListBox========
albumLV = tkinter.Variable(mainWindow)
albumLV.set(('Choose an artist',))
albumList = DataListBox(mainWindow, conn, "albums", "name", sort_order=("name",))
albumList.requery()
albumList.grid(row=1, column=1, sticky='nsew', padx=(30, 0))
albumList.config(border=2, relief='sunken')

albumList.bind('<<ListboxSelect>>', get_songs)

# ========Songs ListBox==========
songLV = tkinter.Variable(mainWindow)
songLV.set(('Choose an album',))
songsList = DataListBox(mainWindow, conn, "songs", "title", ("track", "title"))
songsList.requery()
songsList.grid(row=1, column=2, sticky='nsew', padx=(30, 0))
songsList.config(border=2, relief='sunken')

print("Closing database connection")
mainWindow.mainloop()

conn.close()
