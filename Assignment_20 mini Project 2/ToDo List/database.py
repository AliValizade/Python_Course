import sqlite3

connection = sqlite3.connect("todolistDB.db")
my_cursor = connection.cursor()

def addTask(title, description):
    my_cursor.execute(f'INSERT INTO Tasks(title, description) VALUES("{title}","{description}")')
    # my_cursor.execute('UPDATE Tasks SET time="14:30" WHERE title="Lunch"')
    # my_cursor.execute('DELETE FROM Tasks WHERE title="Wake up"')
    connection.commit()

def getAll():
    my_cursor.execute("SELECT * FROM Tasks")
    results = my_cursor.fetchall()
    return results 

def deleteTask(args):
    pass

def updateDatabase(args):
    pass

def getDetails(id):
    pass