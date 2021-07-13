from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def inicio():
    contenido_html = """
    <html>
    <head>
        <title>EduardoN</title>
    </head>
    <body>
        <h3>Bienvenidos</h3>
        <p>Este sitio pertenece a Eduardo y mostrará datos</p>
        <a href="Eduardo.html"> Eduardo </a>
    </body>
    </html>
    """
    return HTMLResponse(content= respuesta, status_code=200)