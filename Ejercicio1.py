from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def inicio():
    contenido_html = """
    <html>
    <head>
        <title>Eduardo Nájera</title>
    </head>
    <body>
        <h3>BIENVENIDOS</h3>
        <p>Este sitio pertenece a José Eduardo y mostrara algunos datos</p>
        <a href="Eduardo.html">Eduardo </a>
    </body>
    </html>
    """
    return HTMLResponse(content= contenido_html, status_code=200)