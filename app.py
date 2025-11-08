import os
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist_repository import ArtistRepository
from lib.artist import Artist
from flask import Flask, request, render_template, redirect, url_for

# Create a new Flask app
app = Flask(__name__)

# Routes go here:

# GET /albums
# Returns a list of albums
@app.route('/albums', methods = ['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    db_albums = repository.all()
    return render_template('albums/index.html', albums = db_albums)

# GET /artists
# Returns a list of artists
@app.route('/artists', methods = ['GET'])
def get_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    db_artists = repository.all()
    return render_template('artists/index.html', artists = db_artists)

# GET /albums/<id>
# Returns a single album
@app.route('/albums/<int:id>', methods = ['GET'])
def get_album(id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    db_album = repository.find_with_artist(id)
    return render_template('albums/show.html', album = db_album)

# GET /artists/<id>
# Returns a single artist
@app.route('/artists/<int:id>', methods = ['GET'])
def get_artist(id):
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    db_artist = repository.find_with_albums(id)
    return render_template('artists/show.html', artist = db_artist)

# GET /albums/new
# Returns a form to create a new book
@app.route('/albums/new', methods = ['GET'])
def get_new_book():
    return render_template('albums/new.html')

# POST /albums
# Creates a new album
@app.route('/albums', methods = ['POST'])
def create_album():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)

    # Get the fields from the request form
    title = request.form['title']
    release_year = request.form['release_year']
    artist_id = request.form['artist_id']

    # Create a new album object
    album = Album(None, title, release_year, artist_id)

    # Check for validity and if not valid, show the form again with errors
    if not album.is_valid():
        return render_template('albums/new.html', album = album, errors = album.generate_errors()), 400
    
    # Save the album to the database
    album = repository.create(album)

    # Redirect to the new album's show route so the user can see it
    return redirect(f"/albums/{album.id}")

## For the routes above - do same for artists

# Can add DELETE routes for albums and artists - also need to add tests for these (see python-html-web-app-project-starter)

# These lines start the server if you run this file directly
# They also start the server configured to use the test DB if started in test mode
if __name__ == '__main__':
    app.run(debug = True, port = int(os.environ.get('PORT', 5001)))