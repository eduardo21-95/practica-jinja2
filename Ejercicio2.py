from fastapi import FastAPI
from typing import Optional
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def inicio():

@app.get("/integrantes/(item_id)")
def integrantes(item_id: int, matricula: int, nombre: str, edad: Optional[int] = None):
    respuesta = f"""
    <html>
    <head>
        <title>'Eduardo'</title>
    </head>
    <body>
        <h3>Sitio Personal de Nájera</h3>
        <ul>
            <li>Matricula: 091810334</li>
            <li>Nombre: 'Eduardo'</li>
            <li>Edad: 25</li>
    </body>
    </html>
    """
    return HTMLResponse(content= respuesta, status_code=200)