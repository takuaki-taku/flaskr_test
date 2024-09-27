from flaskr import app
# from flaskr import flask  # 不要なインポート
from flask import render_template, request, redirect, url_for
import sqlite3
DATABASE = "database.db"


@app.route('/')
def index():
    conn = sqlite3.connect(DATABASE, check_same_thread=False)
    db_books = conn.execute("SELECT * FROM books").fetchall()
    conn.close()

    books = []
    for row in db_books:
        books.append({
            'id': row[0],
            'title': row[1],
            'joint': row[2],
            'level': row[3]
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
    conn.execute("INSERT INTO books VALUES (NULL, ?, ?, ?)", (title, joint, level))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>', methods=['GET', 'POST'])  # int:id の型指定
def delete(id):
    if request.method == 'POST':
        conn = sqlite3.connect(DATABASE)
        conn.execute("DELETE FROM books WHERE id=?", (id,))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    else:
        # Display confirmation dialog (optional)
        # ...
        return render_template('delete_confirmation.html', id=id)  # Optional confirmation page

if __name__ == '__main__':
    app.run(debug=True)