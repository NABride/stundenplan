from fastapi import FastAPI, Query
from database import get_connection

app = FastAPI()

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
