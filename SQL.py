import sqlite3
db = sqlite3.connect('sqltest.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS  rep (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Product TEXT,
    color_code TEXT
    )"""
    )
db.commit()

sql.execute("""CREATE TABLE IF NOT EXISTS rep2 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    price FLOAT
    )"""
    )
db.commit()
sql.execute("""CREATE TABLE IF NOT EXISTS rep3 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    col1 TEXT,
    col2 TEXT,
    col3 TEXT,
    col4 TEXT,
    col5 TEXT,
    quantity_col1 TEXT,
    quantity_col2 TEXT,
    quantity_col3 TEXT,
    quantity_col4 TEXT,
    quantity_col5 TEXT

    )"""
    )
db.commit()
