from database import get_connection, init_db

init_db()
conn = get_connection()
cur = conn.cursor()

cur.execute("DELETE FROM stunde")
cur.execute("DELETE FROM lehrer")
cur.execute("DELETE FROM fach")
cur.execute("DELETE FROM klasse")

# Beispiel-Daten
cur.execute("INSERT INTO lehrer (name) VALUES (?)", ("Herr Müller",))
cur.execute("INSERT INTO fach (name) VALUES (?)", ("Mathe",))
cur.execute("INSERT INTO klasse (name) VALUES (?)", ("11A",))

cur.execute("INSERT INTO schueler (name, klasse_id) VALUES (?, ?)", ("Bernd Brot", "11A"))
cur.execute("INSERT INTO schueler (name, klasse_id) VALUES (?, ?)", ("Alfred Schwarzenegger", "11B"))


# Mathe-Stunde für Klasse 11A
cur.execute("""
INSERT INTO stunde (tag, stunde, fach_id, lehrer_id, klasse_id, schueler_id)
VALUES (?, ?, ?, ?, ?, ?)
""", ("Montag", 1, 1, 1, 1, 1))

conn.commit()
conn.close()
