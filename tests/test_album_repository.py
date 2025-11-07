from lib.album_repository import AlbumRepository
from lib.album import Album

# When we call AlbumRepository all method
# We get a list of Album objects reflecting the seed data

def test_all(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    albums = repository.all()

    assert albums == [
        Album(1, "Surfer Rosa", 1988, 1),
        Album(2, "Waterloo", 1974, 2),
        Album(3, "Folklore", 2020, 3),
        Album(4, "I Put a Spell on You", 1965, 4)
    ]

# When we call AlbumRepository create method
# I create an album in the DB
# And I can see it back in the all method

def test_create(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    repository.create(Album(None, "Baltimore", 1978, 4))
    albums = repository.all()

    assert albums == [
        Album(1, "Surfer Rosa", 1988, 1),
        Album(2, "Waterloo", 1974, 2),
        Album(3, "Folklore", 2020, 3),
        Album(4, "I Put a Spell on You", 1965, 4),
        Album(5, "Baltimore", 1978, 4)
    ]