from typing import Optional
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

lista_Integrantes = [{'item_id': 1, 'matricula': 918765432, 'nombre': 'Jose', 'edad': 21, 'APaterno': 'Astudillo','AMaterno': 'Girón', 'correo': 'jose@utselva.edu', 'telefono': 9191778245, 'carrera': 'Redes inteligentes'},
                    {'item_id': 2, 'matricula': 918765423, 'nombre': 'Josue', 'edad': 22, 'APaterno': 'Santiz','AMaterno': 'Luna', 'correo': 'josue@utselva.edu', 'telefono': 9191778457, 'carrera': 'ciberseguridad'},
                    {'item_id': 3, 'matricula': 918765445, 'nombre': 'Eduardo', 'edad': 23, 'APaterno': 'Nájera','AMaterno': 'Girón', 'correo': 'Eduard@utselva.edu', 'telefono': 9191771457, 'carrera': 'Seguridad privada'},
                    {'item_id': 4, 'matricula': 918765457, 'nombre': 'Francisco', 'edad': 24, 'APaterno': 'Sanchez','AMaterno': 'Guttierrez', 'correo': 'franc@utselva.edu', 'telefono': 919177457, 'carrera': 'Ingeniero'},
                    {'item_id': 5, 'matricula': 918761456, 'nombre': 'Enrique', 'edad': 28, 'APaterno': 'Carvajal','AMaterno': 'Vargas', 'correo': 'andres@utselva.edu', 'telefono': 919177789, 'carrera': 'Turismo'},
                    {'item_id': 6, 'matricula': 918765456, 'nombre': 'Jesus', 'edad': 26, 'APaterno': 'Acero','AMaterno': 'Monroy', 'correo': 'cristiano@utselva.edu', 'telefono': 919177478, 'carrera': 'contaduria'},
                    {'item_id': 7, 'matricula': 918765478, 'nombre': 'Gerard', 'edad': 35, 'APaterno': 'Perez','AMaterno': 'Garcia', 'correo': 'Gerard@utselva.edu', 'telefono': 919177546, 'carrera': 'Ad. Empresas'},
                    {'item_id': 8, 'matricula': 918764579, 'nombre': 'Rocio', 'edad': 20, 'APaterno': 'Rocha','AMaterno': 'Martinez', 'correo': 'Leo@utselva.edu', 'telefono': 9191774457, 'carrera': 'Relaciones Exteriores'},
                    {'item_id': 9, 'matricula': 918765479, 'nombre': 'Sofia', 'edad': 24, 'APaterno': 'Fernandez','AMaterno': 'Ruiz', 'correo': 'Ana@utselva.edu', 'telefono': 9191774564, 'carrera': 'ing. agricola'},
                    {'item_id': 10, 'matricula': 918764794, 'nombre': 'Lorena', 'edad': 25, 'APaterno': 'solorzano','AMaterno': 'Botero', 'correo': 'eva@utselva.edu', 'telefono': 9191774733, 'carrera': 'Ingeniero civil'}]

@app.get('/integrantes')
async def leer_integrantes(item_id: int):
    for diccionario in lista_Integrantes:
        if diccionario.get('item_id') == item_id:
            respuesta = f"""
            <html>
            <head>
                <title>{diccionario.get('nombre')}</title>
            </head>
            <body>
            <h3>Sitio personal {diccionario.get('nombre')}</h3>
            <ul>
                <li>Matricula: {diccionario.get('matricula')}</li>
                <li strong>APaterno: {diccionario.get('APaterno')}
                <li>AMaterno: {diccionario.get('AMaterno')}</li>
                <li>Nombre: {diccionario.get('nombre')}</li>
                <li>Edad: {diccionario.get('edad')} </li>
                <li>Correo: {diccionario.get('correo')}</li>
                <li>Telefono: {diccionario.get('telefono')}</li>
                <li>Carrera: {diccionario.get('carrera')}</li>
            </ul>
            </body>
            </html>
            """
            return HTMLResponse(content=respuesta, status_code=200)
    return "No se encontro el registro"