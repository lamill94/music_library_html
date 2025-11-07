from lib.artist import Artist
from lib.album import Album

class ArtistRepository:

    # Initialise with DB connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all artists using list comprehension
    def all(self):
        rows = self._connection.execute_query('SELECT * from artists')
        return [Artist(row['id'], row['name'], row['genre']) for row in rows]

    # Find a single artist by its id
    def find(self, artist_id):
        rows = self._connection.execute_query('SELECT * from artists where id = %s', [artist_id])
        row = rows[0]
        return Artist(row['id'], row['name'], row['genre'])
    
    # Find a single artist by its id alongside it's albums

    def find_with_albums(self, artist_id):
        rows = self._connection.execute_query(
            'SELECT artists.id as artist_id, artists.name, artists.genre, albums.id as album_id, albums.title, albums.release_year ' \
            'FROM artists JOIN albums ON artists.id = albums.artist_id ' \
            'WHERE artists.id = %s', [artist_id])
        
        albums = []
        for row in rows:
            album = Album(row["album_id"], row["title"], row["release_year"], row["artist_id"])
            albums.append(album)

        return Artist(rows[0]["artist_id"], rows[0]["name"], rows[0]["genre"], albums)
    
    # Create a new artist
    def create(self, artist):
        rows = self._connection.execute_query('INSERT INTO artists (name, genre) VALUES (%s, %s) RETURNING id', [artist.name, artist.genre])
        return rows[0]['id']
    
    # Can add a find or delete method (see databases-in-python-project-starter) or update method (see python-web-app-project-starter)
    # Would also need to add testing for these methods