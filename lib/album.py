class Album:

    def __init__(self, id, title, release_year, artist_id):
        self.id = id
        self.title = title
        self.release_year = release_year
        self.artist_id = artist_id

    # This method allows our tests to assert that the object it expects are the objects we made based on the DB records
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    # This method allows album to be printed as a string (in the chosen format)
    def __repr__(self):
        return f"Album({self.id}, {self.title}, {self.release_year}, {self.artist_id})"