from flaskr import app
from flask import render_template, request, redirect, url_for
import sqlite3
DATABASE = "database.db"


@app.route('/')
def index():
    conn = sqlite3.connect(DATABASE)
    db_books = conn.execute("SELECT * FROM books").fetchall()
    conn.close()

    books = []
    for row in db_books:
        books.append({
            'title': row[0],
            'joint': row[1],
            'level': row[2]
        })

    return render_template('index.html', books=books)

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/register', methods=['POST'])
def register():
    title = request.form['title']
    joint = request.form['joint']
    level = request.form['level']

    conn = sqlite3.connect(DATABASE)
    conn.execute("INSERT INTO books VALUES (?, ?, ?)", (title, joint, level))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

