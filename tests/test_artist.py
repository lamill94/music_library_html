from lib.artist import Artist

# Test artist constructs

def test_artist_constructs():
    artist = Artist(1, "Pixies", "Rock")
    assert artist.id == 1
    assert artist.name == "Pixies"
    assert artist.genre == "Rock"

# Test that albums with equal contents are equal

def test_artists_are_equal():
    artist1 = Artist(1, "Pixies", "Rock")
    artist2 = Artist(1, "Pixies", "Rock")
    assert artist1 == artist2

# Test that arists can be represented as strings

def test_stringify():
    artist = Artist(1, "Pixies", "Rock")
    assert str(artist) == "Artist(1, Pixies, Rock)"