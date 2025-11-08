from lib.album import Album

# Test album constructs

def test_album_constructs():
    album = Album(1, "Surfer Rosa", 1988, 1)
    assert album.id == 1
    assert album.title == "Surfer Rosa"
    assert album.release_year == 1988
    assert album.artist_id == 1

# Tests that albums with equal contents are equal

def test_albums_are_equal():
    album1 = Album(1, "Surfer Rosa", 1988, 1)
    album2 = Album(1, "Surfer Rosa", 1988, 1)
    assert album1 == album2

# Tests that albums can be represented as strings

def test_stringify():
    album = Album(1, "Surfer Rosa", 1988, 1)
    assert str(album) == "Album(1, Surfer Rosa, 1988, 1)"

# Test album's validity

def test_album_validity():
    assert Album(1, "", "", "").is_valid() == False
    assert Album(1, None, None, None).is_valid() == False
    assert Album(1, "Surfer Rosa", 1988, 1).is_valid() == True

# Test album's errors

def test_album_errors():
    assert Album(1, "", "", "").generate_errors() == "Title can't be blank, Release year can't be blank, Artist ID can't be blank"
    assert Album(1, "", "", 1).generate_errors() == "Title can't be blank, Release year can't be blank"
    assert Album(1, "", 1988, 1).generate_errors() == "Title can't be blank"
    assert Album(1, "Surfer Rosa", 1988, 1).generate_errors() == None