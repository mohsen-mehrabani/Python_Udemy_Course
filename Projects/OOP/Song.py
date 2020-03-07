
class Song:
    """Class to represent a song
    Attributes:
        title(str): the title of the song
        artist(artist): An artist object to represent the song creator
        duration(int): The duration of the song in seconds. May be zero

        """
    def __init__(self, title, artist, duration=0):
        self.title = title
        self.artist = artist
        self.duration = duration

# help(Song)
# help(Song.__init__)
# print(Song.__doc__)
# print(Song.__init__.__doc__)
# Song.__init__.__doc__ = """ Song list method:
#
#         Args:
#             title(str): Initialise the 'title' attribute
#             artist(str):At artist object representing the song's creator
#             duration(optional[int]: Initial the value for the 'duration' attribute.
#                                     will default to zero if not specified
#         """
# help(Song)


class Album:
    """ Class to represent an Album, using it's track list
    Attributes:
        name(str): The name of the album.
        year(int): The year was album released.
        artist(Artist): The artist responsible for the album. If not specified,
        the artist will default to an artist with the name "Various Artist".
        track (list[song]): A list of the songs on the album.
    Methods:
          add_song: Used to add a new song to the album's track list.
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artist")
        else:
            self.artist = artist

        self.track = []

    def add_song(self, song, position=None):
        """ Adds a song to the track list

        Args:
            song(song): A song to add.
            position(optional[int]): If specified the song will be added to that position.
            in the track list - Inserting it between other song if necessary.
            Otherwise the song will be added to the end of the list.
        """
        if position is None:
            self.track.append(song)
        else:
            self.track.append(position, song)


class Artist:
    """Basic class to store artist details.
    Attributes:
        name(str): The name of the artist.
        albums(list[Album]): A list of the albums by this artist.
        The list includes only those albums in this collection, it is
        not an exhaustive list of the artist's published albums.
    Methods:
        add_album: Use to add a new album to the artist's albums list
    """
    def __init__(self, name):
        self.name = name
        self.album = []

    def add_album(self, album):
        """Add a new album to the list

        Args:
            album(Album): Album object to add to list.
                If the album is already present, it will not added again (although this is yet to implemented).
        """
        self.album.append(album)


def load_data():
    new_album = None
    new_artist = None
    artist_list = []

    with open("albums.txt", 'r') as albums:
        for line in albums:
            # data rwo should consist of (artist, album, year, song)
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            # print(artist_field, album_field, year_field, song_field)
            print("{}:{}:{}:{}".format(artist_field, album_field, year_field, song_field))

            if new_artist is None:
                new_artist = Artist(artist_field)
            elif new_artist.name != artist_field:
                # We've just read details for a new artist
                # store the current album in the currents artists collection then create a new artist object
                new_artist.add_album(new_album)
                artist_list.append(new_artist)
                new_artist = Artist(artist_field)
                new_album = None

            if new_album is None:
                new_album = Album(album_field, year_field, new_artist)
            elif new_album.name != album_field:
                # We've just read a new album for the current artist
                # Store the current album in the artist's collection the create a new album object
                new_artist.add_album(new_album)
                new_album = Album(album_field, year_field, new_artist)

            # Create a new song object and add it to the current album's collection
            new_song = Song(song_field, new_artist)
            new_album.add_song(new_song)

        # After we read the last line of the text file, we will have an artist and album that have
        # not been store - process them now
        if new_artist is not None:
            if new_album is not None:
                new_artist.add_album(new_album)
            artist_list.append(new_artist)

    return artist_list


def create_check_file(artist_list):
    """ Create a check list file form the object data for comparison with the original file """
    with open("check_file.text", 'w') as check_file:
        for new_artist in artist_list:
            for new_album in new_artist.album:
                for new_song in new_album.track:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(new_artist, new_album, new_song),
                          file=check_file)


if __name__ == '__main__':
    artists = load_data()
    print("There are {} artists".format(len(artists)))

    create_check_file(artists)
