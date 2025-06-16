import sqlite3

DB_PATH = "stundenplan.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS lehrer (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )""")

    cur.execute("""
    CREATE TABLE IF NOT EXISTS fach (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )""")

    cur.execute("""
    CREATE TABLE IF NOT EXISTS klasse (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )""")

    cur.execute("""
    CREATE TABLE IF NOT EXISTS schueler (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        klasse_id INTEGER,
        FOREIGN KEY (klasse_id) REFERENCES klasse(id)                
    )""")

    cur.execute("""
    CREATE TABLE IF NOT EXISTS stunde (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tag TEXT NOT NULL,
        stunde INTEGER NOT NULL,
        fach_id INTEGER,
        lehrer_id INTEGER,
        klasse_id INTEGER,
        schueler_id INTEGER,
        FOREIGN KEY (fach_id) REFERENCES fach(id),
        FOREIGN KEY (lehrer_id) REFERENCES lehrer(id),
        FOREIGN KEY (klasse_id) REFERENCES klasse(id),
        FOREIGN KEY (schueler_id) REFERENCES schueler(id)
    )""")

    conn.commit()
    conn.close()
