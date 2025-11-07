from lib.database_connection import DatabaseConnection

# Run this file to reset your DB using the seeds e.g. python seed_dev_database.py

connection = DatabaseConnection(test_mode = False)
connection.connect()
connection.seed("seeds/music_library.sql")

