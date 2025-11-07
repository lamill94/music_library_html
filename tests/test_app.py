from playwright.sync_api import Page, expect

# When I go to http://localhost:5001/albums
# I get a list of albums

def test_get_albums(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")

    li_tags = page.locator("li")
    expect(li_tags).to_have_text([
        "Surfer Rosa",
        "Waterloo",
        "Folklore",
        "I Put a Spell on You"
    ])

# The page returned by GET /albums should contain a link for each album listed
# It should link to '/albums/<id>', where each <id> is the corresponding album's id
# That page should then show information about the specific album

def test_visit_album_show_page(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Surfer Rosa'")

    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Album: Surfer Rosa")

    details_tag = page.locator(".details p")
    expect(details_tag).to_have_text([
        "Release year: 1988",
        "Artist: Pixies"
    ])

# Test go back button

def test_visit_album_show_page_and_go_back(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Surfer Rosa'")
    page.click("text='Go back to album list'")

    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Albums")

# When I go to http://localhost:5001/albums/1
# I get a single album

def test_get_album(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums/1")

    h1_tags = page.locator("h1")
    expect(h1_tags).to_have_text("Album: Surfer Rosa")

    details_tag = page.locator(".details p")
    expect(details_tag).to_have_text([
        "Release year: 1988",
        "Artist: Pixies"
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
"""
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
        "Album(2, Waterloo, 1974, 2)",
        "Album(3, Folklore, 2020, 3)",
        "Album(4, I Put a Spell on You, 1965, 4)",
        "Album(5, Baltimore, 1978, 4)"
    ])
"""

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
"""
def test_post_albums_no_data(db_connection, web_client):
    db_connection.seed("seeds/music_library.sql")
    post_response = web_client.post("/albums")
    assert post_response.status_code == 400
    assert post_response.data.decode('utf-8') == "You need to submit a title, release_year and artist_id"

    get_response = web_client.get("/albums")
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "\n".join([
        "Album(1, Surfer Rosa, 1988, 1)",
        "Album(2, Waterloo, 1974, 2)",
        "Album(3, Folklore, 2020, 3)",
        "Album(4, I Put a Spell on You, 1965, 4)"
    ])
"""

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

