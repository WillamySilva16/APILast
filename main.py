from fastapi import FastAPI
import pyodbc

app = FastAPI()

def get_connection():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=pbdb3073.database.windows.net;"
        "DATABASE=PBDB3073;"
        "UID=admrs;"
        "PWD=Gf3$Rn8!Qb12^KsW0tZ;"
    )

@app.get("/")
def root():
    return {"status": "API ONLINE"}

@app.get("/visitas")
def get_visitas():
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT TOP 10 *
    FROM TAB_REGISTRO_VISITA_SUPERVISAO_CABECALHO
    """

    cursor.execute(query)
    columns = [col[0] for col in cursor.description]
    rows = cursor.fetchall()

    result = [dict(zip(columns, row)) for row in rows]

    cursor.close()
    conn.close()

    return result
