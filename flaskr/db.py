import sqlite3

DATABASE= "database.db"

def create_books_table():
    con = sqlite3.connect(DATABASE)
    con.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY AUTOINCREMENT,title,joint,level)")
    con.close()



def get_connection():
    return sqlite3.connect('azutre.db')

def get_all_data():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM azutre')
    data = cursor.fetchall()
    
