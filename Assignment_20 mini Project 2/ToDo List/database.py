import sqlite3

connection = sqlite3.connect("todolistDB.db")
my_cursor = connection.cursor()

def addTask(id, title, description, time):
    my_cursor.execute(f'INSERT INTO Tasks(id, title, description, time, done) VALUES("{id}","{title}","{description}","{time}","{0}")')
    connection.commit()

def getAll():
    my_cursor.execute("SELECT * FROM Tasks")
    results = my_cursor.fetchall()
    return results 

def getDetails(id):
    my_cursor.execute(f'SELECT * FROM Tasks WHERE id={id}')
    result = my_cursor.fetchall()
    return result

def deleteTask(del_id):
    my_cursor.execute(f'DELETE FROM Tasks WHERE id={del_id}')
    connection.commit()

def update_done(id, state):
    my_cursor.execute(f'UPDATE Tasks SET done = {state} WHERE id={id}')
    connection.commit()