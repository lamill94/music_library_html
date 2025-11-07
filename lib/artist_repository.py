from lib.artist import Artist

class ArtistRepository:

    # Initialise with DB connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all artists using list comprehension
    def all(self):
        rows = self._connection.execute_query('SELECT * from artists')
        return [Artist(row['id'], row['name'], row['genre']) for row in rows]
    
    # Create a new artist
    def create(self, artist):
        rows = self._connection.execute_query('INSERT INTO artists (name, genre) VALUES (%s, %s) RETURNING id', [artist.name, artist.genre])
        return rows[0]['id']
    
    # Can add a find or delete method (see databases-in-python-project-starter) or update method (see python-web-app-project-starter)
    # Would also need to add testing for these methods