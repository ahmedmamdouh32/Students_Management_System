import sqlite3 as sql

def get_data(command):
    connection = sql.connect('Database.db')
    cursor = connection.cursor()  # we use it as a gate to write in database tables
    cursor.execute(command)
    rows = cursor.fetchall()
    connection.commit()  # to assure execution of query
    connection.close()
    return rows