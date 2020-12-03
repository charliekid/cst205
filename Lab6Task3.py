# CST 205
# Charlie Nguyen
# Oct 8, 2020
# This program demonstrates how classes work.

class Song:
    def __init__ (self, artist, genre, seconds, album):
        self.artist = artist
        self.genre = genre
        self.seconds = seconds
        self.album = album


discoYeahSong = Song("Tom Misch", "Jazz", 232, "Geography")
valerieSong = Song("Amy Winehouse", "Pop", 323, "Back to Black")
justInTimeSong = Song("Frank Sintra", "Jazz", 432, "Just in Time")


print(discoYeahSong.artist)
print(valerieSong.seconds)
print(justInTimeSong.album)
