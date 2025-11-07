class Artist:

    def __init__(self, id, name, genre):
        self.id = id
        self.name = name
        self.genre = genre

    # This method allows our tests to assert that the object it expects are the objects we made based on the DB records
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    # This method allows Artist object to be printed as a string (in the chosen format)
    def __repr__(self):
        return f"Artist({self.id}, {self.name}, {self.genre})"