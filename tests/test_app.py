# When I call GET /albums
# I get a list of albums back

def test_get_albums(db_connection, web_client):
    db_connection.seed("seeds/music_library.sql")
    response = web_client.get("/albums")
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "\n".join([
        "Album(1, Surfer Rosa, 1988, 1)",
        "Album(2, Doolittle, 1989, 1)",
        "Album(3, Ring Ring, 1973, 2)",
        "Album(4, Waterloo, 1974, 2)",
        "Album(5, Lover, 2019, 3)",
        "Album(6, Folklore, 2020, 3)",
        "Album(7, I Put a Spell on You, 1965, 4)",
        "Album(8, Here Comes the Sun, 1971, 4)"
    ])

# When I call GET /artists
# I get a list of artists back

def test_get_artists(db_connection, web_client):
    db_connection.seed("seeds/music_library.sql")
    response = web_client.get("/artists")
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "\n".join([
        "Artist(1, Pixies, Rock)",
        "Artist(2, ABBA, Pop)",
        "Artist(3, Taylor Swift, Pop)",
        "Artist(4, Nina Simone, Jazz)"
    ])

# When I call POST /albums with album info
# That album is now in the list in GET /albums

def test_post_albums(db_connection, web_client):
    db_connection.seed("seeds/music_library.sql")
    post_response = web_client.post("/albums", data = {
        'title': 'Baltimore',
        'release_year': '1978',
        'artist_id': '4'
    })
    assert post_response.status_code == 200
    assert post_response.data.decode('utf-8') == ""

    get_response = web_client.get("/albums")
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "\n".join([
        "Album(1, Surfer Rosa, 1988, 1)",
        "Album(2, Doolittle, 1989, 1)",
        "Album(3, Ring Ring, 1973, 2)",
        "Album(4, Waterloo, 1974, 2)",
        "Album(5, Lover, 2019, 3)",
        "Album(6, Folklore, 2020, 3)",
        "Album(7, I Put a Spell on You, 1965, 4)",
        "Album(8, Here Comes the Sun, 1971, 4)",
        "Album(9, Baltimore, 1978, 4)"
    ])

# When I call POST /artists with artist info
# That artist is now in the list in GET /artists

def test_post_artists(db_connection, web_client):
    db_connection.seed("seeds/music_library.sql")
    post_response = web_client.post("/artists", data = {'name': 'Wild Nothing', 'genre': 'Indie'})
    assert post_response.status_code == 200
    assert post_response.data.decode('utf-8') == ""

    get_response = web_client.get("/artists")
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "\n".join([
        "Artist(1, Pixies, Rock)",
        "Artist(2, ABBA, Pop)",
        "Artist(3, Taylor Swift, Pop)",
        "Artist(4, Nina Simone, Jazz)",
        "Artist(5, Wild Nothing, Indie)"
    ])

# When I call POST /albums with no data
# I get error message

def test_post_albums_no_data(db_connection, web_client):
    db_connection.seed("seeds/music_library.sql")
    post_response = web_client.post("/albums")
    assert post_response.status_code == 400
    assert post_response.data.decode('utf-8') == "You need to submit a title, release_year and artist_id"

    get_response = web_client.get("/albums")
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "\n".join([
        "Album(1, Surfer Rosa, 1988, 1)",
        "Album(2, Doolittle, 1989, 1)",
        "Album(3, Ring Ring, 1973, 2)",
        "Album(4, Waterloo, 1974, 2)",
        "Album(5, Lover, 2019, 3)",
        "Album(6, Folklore, 2020, 3)",
        "Album(7, I Put a Spell on You, 1965, 4)",
        "Album(8, Here Comes the Sun, 1971, 4)"
    ])

# When I call POST /artists with no data
# I get error message

def test_post_artists_no_data(db_connection, web_client):
    db_connection.seed("seeds/music_library.sql")
    post_response = web_client.post("/artists")
    assert post_response.status_code == 400
    assert post_response.data.decode('utf-8') == "You need to submit a name and genre"

    get_response = web_client.get("/artists")
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "\n".join([
        "Artist(1, Pixies, Rock)",
        "Artist(2, ABBA, Pop)",
        "Artist(3, Taylor Swift, Pop)",
        "Artist(4, Nina Simone, Jazz)"
    ])

