import pymssql
from fastapi import FastAPI

app = FastAPI()

def get_connection():
    return pymssql.connect(
        server="pbdb3073.database.windows.net",
        user="admrs",
        password="Gf3$Rn8!Qb12^KsW0tZ",
        database="PBDB3073"
    )

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
