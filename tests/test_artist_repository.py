from lib.artist_repository import ArtistRepository
from lib.artist import Artist

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
