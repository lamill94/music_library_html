# When I seed the DB
# I get some records back

def test_database_connection(db_connection):
    db_connection.seed("seeds/database_connection.sql")

    db_connection.execute_query('INSERT INTO test_table (name) VALUES (%s)', ["second_record"])

    result = db_connection.execute_query('SELECT * from test_table')

    assert result == [
        {'id': 1, 'name': 'first_record'},
        {'id': 2, 'name': 'second_record'}
    ]