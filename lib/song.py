class Song:
    song_count = 0
    def __init__(self,name,artist,genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.song_count += 1
