from typing import Union

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/")
def index(request: Request):
    # return {"Heloo": "world"}
    body_start = "CV"
    head_start = "Sergey Poleshchuk"
    # brief_description = "Graphic Artist - Web Designer - Illustrator"
    brief_description = "Python developer, C++ developer"
    return templates.TemplateResponse("index.html", {"request": request, "body_start": body_start,
                                                     "head_start": head_start, "brief_description": brief_description})

@app.get("/items/{id}")
def read_item(request: Request, id: str):
    return templates.TemplateResponse("item.html", {"request": request, "id": id})
