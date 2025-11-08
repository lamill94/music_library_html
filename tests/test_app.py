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

# When I go to http://localhost:5001/artists
# I get a list of artists

def test_get_artists(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists")

    li_tags = page.locator("li")
    expect(li_tags).to_have_text([
        "Pixies",
        "ABBA",
        "Taylor Swift",
        "Nina Simone"
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

# The page returned by GET /artists should contain a link for each artist listed
# It should link to '/artists/<id>', where each <id> is the corresponding artist's id
# That page should then show information about the specific artist

def test_visit_artist_show_page(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click("text='Pixies'")

    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Artist: Pixies")

    details_tag = page.locator(".details p")
    expect(details_tag).to_have_text([
        "Genre: Rock",
        "Albums: Surfer Rosa (1988)"
    ])

# Test go back button for Album show page

def test_visit_album_show_page_and_go_back(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text='Surfer Rosa'")
    page.click("text='Go back to album list'")

    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Albums")

# Test go back button for Artist show page

def test_visit_artist_show_page_and_go_back(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/artists")
    page.click("text='Pixies'")
    page.click("text='Go back to artist list'")

    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Artists")

# When I create a new album
# We see it in the albums index

def test_create_album(db_connection, page, test_web_address):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    page.click("text=Add a new album")
    page.fill("input[name='title']", "Here Comes the Sun")
    page.fill("input[name='release_year']", "1971")
    page.fill("input[name='artist_id']", "4")
    page.click("text=Add album")

    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Album: Here Comes the Sun")

    details_tag = page.locator(".details p")
    expect(details_tag).to_have_text([
        "Release year: 1971",
        "Artist: Nina Simone"
    ])

# When I call POST /artists with artist info
# That artist is now in the list in GET /artists
"""
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
"""

# When I call POST /artists with no data
# I get error message
"""
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
"""
