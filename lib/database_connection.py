import os, psycopg
from flask import g
from psycopg.rows import dict_row

class DatabaseConnection:

    DEV_DATABASE_NAME = "music_library"
    TEST_DATABASE_NAME = "music_library_test"

    def __init__(self, test_mode = False):
        self.test_mode = test_mode

    # This private method returns the name of the DB we should use
    def _database_name(self):
        if self.test_mode:
            return self.TEST_DATABASE_NAME
        else:
            return self.DEV_DATABASE_NAME

    # This method connects to PostgreSQL using the psycopg library
    # We connect to localhost & select the DB name given in argument

    def connect(self):
        try:
            self.connection = psycopg.connect(f"postgresql://localhost/{self._database_name()}", row_factory = dict_row)
        except psycopg.OperationalError:
            raise Exception(f"Couldn't connect to the DB {self._database_name()}")
        
    # This private method checks that we're connected to the DB

    CONNECTION_MESSAGE = "Can't run a SQL query as the connection to the DB was never opened. Did you call first the method DatabaseConnection.connect in your app.py file or in your tests?"

    def _check_connection(self):
        if self.connection is None:
            raise Exception(self.CONNECTION_MESSAGE)
        
    # This methods seeds the DB with the given SQL file
    # We use it to set up our DB ready for our tests or application

    def seed(self, sql_filename):
        self._check_connection()

        if not os.path.exists(sql_filename):
            raise Exception(f"File {sql_filename} does NOT exist")
        
        with self.connection.cursor() as cursor:
            cursor.execute(open(sql_filename, "r").read())
            self.connection.commit()

    # This method executes a SQL query on the DB (usually after it's been seeded)
    # It allows you to set some parameters too

    def execute_query(self, query, params = []):
        self._check_connection()

        with self.connection.cursor() as cursor:
            cursor.execute(query, params)

            if cursor.description is not None:
                result = cursor.fetchall() # Select returns rows
            else:
                result = None # Insert, update & delete DON'T return rows

            self.connection.commit()
            return result
        
# This function integrates with Flask to create one DB connection that Flask request can use (see app.py for its use)
def get_flask_database_connection(app):
    if not hasattr(g, 'flask_database_connection'):
        g.flask_database_connection = DatabaseConnection(test_mode = ((os.getenv('APP_ENV') == 'test') or (app.config['TESTING'] == True)))
        g.flask_database_connection.connect()
    return g.flask_database_connection