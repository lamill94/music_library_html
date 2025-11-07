import pytest
from lib.database_connection import DatabaseConnection
from app import app

# Pytest fixtures are reusable functions that provide setup logic for tests and they create an object that can be used in tests

# We will use below to create a DB connection

@pytest.fixture

def db_connection():
    connection = DatabaseConnection(test_mode = True)
    connection.connect()
    return connection

# Below creates a fixture for the client that we'll use to make test requests

@pytest.fixture

def web_client():
    app.config['TESTING'] = True # This gets us better errors
    with app.test_client() as client:
        yield client

# When we create a test, if we allow it to accept parameters called 'db_connection' or 'web_client', Pytest will
# automatically pass in the objects we created above. For example:

# def test_something(db_connection, web_client):
#   db_connection is now available to us in this test
#   web_client is now available to us in this test