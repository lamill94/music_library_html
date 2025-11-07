from lib.artist_repository import ArtistRepository
from lib.artist import Artist
from lib.album import Album

# When we call all method
# We get a list of Artist objects reflecting the seed data

def test_all(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = ArtistRepository(db_connection)
    artists = repository.all()

    assert artists == [
        Artist(1, 'Pixies', 'Rock'),
        Artist(2, 'ABBA', 'Pop'),
        Artist(3, 'Taylor Swift', 'Pop'),
        Artist(4, 'Nina Simone', 'Jazz')
    ]

# When we call ArtistRepository find method
# We get an Artist object

def test_find(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = ArtistRepository(db_connection)
    artist = repository.find(1)
    assert artist == Artist(1, "Pixies", "Rock")

# When we call ArtistRepository find_with_albums method
# We get an Artist object with albums

def test_find_with_artist(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = ArtistRepository(db_connection)
    artist = repository.find_with_albums(1)
    assert artist == Artist(1, "Pixies", "Rock", [Album(1, "Surfer Rosa", 1988, 1)])

# When we call create method
# I create an artist in the DB
# And I can see it back in the all method

def test_create(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = ArtistRepository(db_connection)
    repository.create(Artist(None, "Wild Nothing", "Indie"))
    artists = repository.all()

    assert artists == [
        Artist(1, 'Pixies', 'Rock'),
        Artist(2, 'ABBA', 'Pop'),
        Artist(3, 'Taylor Swift', 'Pop'),
        Artist(4, 'Nina Simone', 'Jazz'),
        Artist(5, 'Wild Nothing', 'Indie')
    ]
