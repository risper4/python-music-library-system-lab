class Song:
    count = 0
    genres = set()
    artists = set()
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre 
        Song.count += 1
        Song.add_to_genres(genre)
        Song.add_to_artist(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls, name) :
        print(f'{name}')
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre) :
        cls.genres.add(genre)
        cls.add_to_genre_count(genre)
            

    @classmethod
    def add_to_artist(cls, artist) :
        cls.artists.add(artist)
        cls.add_to_artist_count(artist)
            

    @classmethod
    def add_to_genre_count(cls, genre) :
        if genre not in cls.genre_count :
            cls.genre_count[genre] = 1
        else :
            cls.genre_count[genre] += 1

    @classmethod
    def add_to_artist_count(cls, artist) :
        if artist not in cls.artist_count :
            cls.artist_count[artist] = 1
        else :
            cls.artist_count[artist] += 1
