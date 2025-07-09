class Song:
    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}

    def __init__(self,name,artist,genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.artists
        Song.genres
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls,genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls,artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls):
        pass

    @classmethod
    def add_to_artists_count(cls):
        pass