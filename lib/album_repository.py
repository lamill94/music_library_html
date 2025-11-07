from lib.album import Album

class AlbumRepository:

    # Initialise with DB connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all albums using list comprehension
    def all(self):
        rows = self._connection.execute_query('SELECT * from albums')    
        return [Album(row['id'], row['title'], row['release_year'], row['artist_id']) for row in rows]
    
    # Create a new album
    def create(self, album):
        rows = self._connection.execute_query('INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s) RETURNING id', [album.title, album.release_year, album.artist_id])
        return rows[0]['id']
    
    # Can add a find or delete method (see databases-in-python-project-starter) or update method (see python-web-app-project-starter)
    # Would also need to add testing for these methods
    
