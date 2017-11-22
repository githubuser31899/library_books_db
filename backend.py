#Section #2 == back_end coding (database_conn/command_functions/etc.)
import sqlite3

def connect():
    conn = sqlite3.connect("Library_Books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, ISBN INTEGER)")
    conn.commit()
    conn.close()

def insert(title, author, year, ISBN):
    conn = sqlite3.connect("Library_Books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO Books VALUES (NULL, ?,?,?,?)", (title, author, year, ISBN))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("Library_Books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Books")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(title="", author="", year="", ISBN=""):
    conn = sqlite3.connect("Library_Books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Books WHERE title=? OR author=? OR year=? OR ISBN=?", (title, author, year, ISBN))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect("Library_Books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM Books WHERE id=?", (id,))
    conn.commit()
    conn.close()


def update(id, title, author, year, ISBN):
    conn = sqlite3.connect("Library_Books.db")
    cur = conn.cursor()
    cur.execute("UPDATE Books SET title=?, author=?, year=?, ISBN=? WHERE id=?", (title, author, year, ISBN, id))
    conn.commit()
    conn.close()

connect()
