from fastapi import FastAPI, Query
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os
from database import get_connection

app = FastAPI()

# Absolute oder relative Pfade korrekt setzen
frontend_path = os.path.abspath("../frontend")

# Static-Dateien (JS, CSS usw.) verfügbar machen
app.mount("/static", StaticFiles(directory=frontend_path), name="static")

# index.html aus frontend liefern
@app.get("/")
def root():
    return FileResponse(os.path.join(frontend_path, "index.html"))

@app.get("/klassen")
def get_klassen():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM klasse")
    rows = cur.fetchall()
    conn.close()
    return [{"id": row[0], "name": row[1]} for row in rows]


@app.get("/schueler")
def get_schueler():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM schueler")
    result = [{"id": row[0], "name": row[1]} for row in cur.fetchall()]
    conn.close()
    return result


@app.get("/stundenplan")
def get_stundenplan(klasse: str = Query(..., description="z. B. '11A'")):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT stunde.id, tag, stunde, fach.name, lehrer.name
        FROM stunde
        JOIN fach ON fach.id = stunde.fach_id
        JOIN lehrer ON lehrer.id = stunde.lehrer_id
        JOIN klasse ON klasse.id = stunde.klasse_id
        WHERE klasse.name = ?
    """, (klasse,))

    rows = cur.fetchall()
    conn.close()

    return [
        {
            "id": row[0],
            "tag": row[1],
            "stunde": row[2],
            "fach": row[3],
            "lehrer": row[4]
        }
        for row in rows
    ]
