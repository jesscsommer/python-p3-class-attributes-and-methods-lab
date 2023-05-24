class Song:

    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):

        self.name = name
        self.artist = artist 
        self.genre = genre

        Song.add_song_to_count()
        if genre not in Song.genres:
            Song.add_to_genres(genre)
        if artist not in Song.artists:
            Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)
    
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1
    
    @classmethod
    def add_to_genres(cls, genre):
        cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        cls.artists.append(artist)
    
    @classmethod
    def add_to_genre_count(cls, genre):
        current_count = cls.genre_count.get(genre, 0)
        cls.genre_count.update({genre: current_count + 1})

    @classmethod
    def add_to_artist_count(cls, artist):
        current_count = cls.artist_count.get(artist, 0)
        cls.artist_count.update({artist: current_count + 1})