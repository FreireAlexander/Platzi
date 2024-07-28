'''
Curso de FastAPI de Platzi
'''

from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse

app = FastAPI()

app.title = "Declaraciones de Renta"
app.version = "0.0.1-DEV"

names = [
    {
        "id":1140858993,
        "name": "Freire Alexander Palomino Palma",
        "amount": 2600.342
     },
      {
        "id":1140860262,
        "name": "Estefania Maldonado Cardenas",
        "amount": 10000500
     }
]
response = f'''
    <h1 
        style="
                color: navy; 
                font-size: 5rem; 
                background-color: cream;
                border: 2px navy solid; 
                border-radius: 4px; ">
        Hello {names[0]['id']}!!!
    </h1>'''
response = HTMLResponse(response)

@app.get('/', tags=['home'])
def message():
    global response
    return response


@app.get('/names/{id}', tags=['name'])
def get_Names(id: int):
    global names
    for name in names:
        if id == name['id']:
            return name
    return {}


@app.get('/names/', tags=['names'])
def search(name: str = None):
    global names
    for _name in names:
        if name in _name['name']:
            return _name
    return {}