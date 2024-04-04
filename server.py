from pytz import timezone
from datetime import datetime

from fastapi import FastAPI, UploadFile, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from crud import *


app = FastAPI()
app.mount("/static", StaticFiles(directory="resources"), name="static")
templates = Jinja2Templates(directory="templates")

server_start_time = None


def get_start_time():
    return server_start_time


@app.on_event("startup")
async def startup_event():
    global server_start_time
    server_start_time = datetime.now(tz=timezone('Europe/Moscow'))


@app.get("/ping")
def ping():
    return "pong"


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request, start_time: datetime = Depends(get_start_time)):
    return templates.TemplateResponse("wlcm.html", {"request": request, "start_time": start_time})


@app.get("/get_table/{table_name}")
def get_table(table_name: str):
    return get_table(table_name=table_name)


@app.get("/get_all/")
def get_join_base():
    return get_all()


@app.get("/get_var")
def get_join_base():
    return get_var()


@app.post("/set_device")
async def set_base_item(file: UploadFile):
    file = await file.read()
    return set_device(file=file)


@app.post("/set_table_item/{table_name}")
async def set_table_item(file: UploadFile, table_name: str):
    file = await file.read()
    return set_item(table_name=table_name, file=file)


@app.post("/del_table_item/{table_name}")
async def del_table_item(file: UploadFile, table_name: str):
    file = await file.read()
    return del_item(table_name=table_name, file=file)
