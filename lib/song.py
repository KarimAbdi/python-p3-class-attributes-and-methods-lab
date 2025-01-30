class Song:
    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        # Instance variables
        self.name = name
        self.artist = artist
        self.genre = genre

        # Increment the count of songs
        Song.add_song_to_count()

        # Add the artist and genre to the class attributes
        Song.add_to_artists(artist)
        Song.add_to_genres(genre)

        # Update the genre count and artist count
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

# Examples of usage:
ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
one_time = Song("One Time", "Drake", "Pop")
halo = Song("Halo", "Beyonce", "Pop")

# Checking the class attributes
print(Song.count)  # Total number of songs created
print(Song.artists)  # List of unique artists
print(Song.genres)  # List of unique genres
print(Song.genre_count)  # Genre count
print(Song.artist_count)  # Artist count
