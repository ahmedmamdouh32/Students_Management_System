import sqlite3 as sql

def get_data(command):
    connection = sql.connect('Database.db')
    cursor = connection.cursor()  # we use it as a gate to write in database tables
    cursor.execute(command)
    rows = cursor.fetchall()
    connection.commit()  # to assure execution of query
    connection.close()
    return rows

def add_user(user_data):
    connection = sql.connect('Database.db')
    cursor = connection.cursor()  # we use it as a gate to write in database tables
    command =f"INSERT INTO Students(ID,Name,Phone_Number,Email,Major,Intake_No,Academic_Year,Payment_Status) Values ({user_data[0]},'{user_data[1]}','{user_data[2]}','{user_data[3]}','{user_data[4]}',{user_data[5]},{user_data[6]},'{user_data[7]}')"
    cursor.execute(command)
    connection.commit()  # to assure execution of query
    connection.close()
#

def delete_by_id(user_id):
    connection = sql.connect('Database.db')
    cursor = connection.cursor()  # we use it as a gate to write in database tables
    command =f"DELETE FROM Students WHERE id = {user_id}"
    cursor.execute(command)
    connection.commit()  # to assure execution of query
    connection.close()

def get_by_id(user_id):
    connection = sql.connect('Database.db')
    cursor = connection.cursor()  # we use it as a gate to write in database tables
    command =f"SELECT * FROM Students WHERE id = {user_id}"
    cursor.execute(command)
    row = cursor.fetchone()
    connection.commit()  # to assure execution of query
    connection.close()
    return row


def update_user(user_data):
    connection = sql.connect('Database.db')
    cursor = connection.cursor()  # we use it as a gate to write in database tables
    command =f"UPDATE Students SET Name = '{user_data[1]}', Email = '{user_data[3]}', Phone_Number = '{user_data[2]}', Major = '{user_data[4]}', Intake_NO = '{user_data[5]}', Academic_Year ='{user_data[6]}', Payment_Status = '{user_data[7]}' WHERE id = '{user_data[0]}'"
    cursor.execute(command)
    connection.commit()  # to assure execution of query
    connection.close()

def is_id_valid(user_id):
    connection = sql.connect('Database.db')
    cursor = connection.cursor()  # we use it as a gate to write in database tables
    command = f"SELECT EXISTS(SELECT 1 FROM students WHERE id = {user_id})"
    cursor.execute(command)
    connection.commit()  # to assure execution of query
    result = cursor.fetchone()[0]
    connection.close()
    return result