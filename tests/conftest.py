import pytest, sys, random, py, os
from xprocess import ProcessStarter
from lib.database_connection import DatabaseConnection
from app import app

# Pytest fixtures are reusable functions that provide setup logic for tests and they create an object that can be used in tests

# This fixture creates a DB connection

@pytest.fixture
def db_connection():
    connection = DatabaseConnection(test_mode = True)
    connection.connect()
    return connection

# This fixture starts the test server and makes it available to the tests

@pytest.fixture
def test_web_address(xprocess):
    python_executable = sys.executable
    app_file = py.path.local(__file__).dirpath("../app.py")
    port = str(random.randint(4100, 4199))

    class Starter(ProcessStarter):
        env = {"PORT": port, "APP_ENV": "test", **os.environ}
        pattern = "Debugger PIN"
        args = [python_executable, app_file]

    xprocess.ensure("flask_test_server", Starter)

    yield f"localhost:{port}"

    xprocess.getinfo("flask_test_server").terminate()

# This creates a fixture for the client that we'll use to make test requests

@pytest.fixture
def web_client():
    app.config['TESTING'] = True # This gets us better errors
    with app.test_client() as client:
        yield client

# When we create a test, if we allow it to accept parameters called 'db_connection' or 'test_web_address', Pytest will
# automatically pass in the objects we created above. For example:

# def test_something(db_connection, test_web_address):
#   db_connection is now available to us in this test
#   test_web_address is now available to us in this test