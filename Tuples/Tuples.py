# Today lesson is about Tuple
# from typing import List, Union
#
# t = "a", "b", "c"
# print(type(t))
#
# Metallica = "Ride the Lightening", "Metallica", 1984
# print(Metallica)
# print(Metallica[0])
# print(Metallica[1])
# print(Metallica[2])
# # noinspection SpellCheckingInspection
# Metallica = Metallica[0], "Imelda", Metallica[2]
# print(Metallica)
# print("=" * 50)
# title, artist, year = Metallica
# print(title)
# print(artist)
# print(year)
# ----------------------------------------------------------------------
# Metallica2 = ["Ride the Lightening", "Metallica", 1984]
# print(type(Metallica2))
# Metallica2.append("Rock")
#
# print(Metallica2)
# title, artist, year = Metallica2
# -----------------------------------------------------------------------
imelda = "More Mayhem", "Imelda May", 2011, (
    (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")
)
# My solution which is wrong
# for i in range(0, len(imelda) - 1):
#     print(imelda[i])
#
# for j in range(0, len(imelda)):
#     print(j)
# -----------------------------------------
# Tim's Solution
title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
for song in tracks:
    # print("\t", song)
    track, title = song
    print("\tTrack number {}, Title: {}".format(track, title))
