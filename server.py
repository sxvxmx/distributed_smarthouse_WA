from fastapi import FastAPI, UploadFile, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import base, crud, model
from datetime import datetime
from pytz import timezone

app = FastAPI()
app.mount("/static", StaticFiles(directory="resources"), name="static")

server_start_time = None

@app.on_event("startup")
async def startup_event():
    global server_start_time
    server_start_time = datetime.now(tz=timezone('Europe/Moscow'))

def get_start_time():
    return server_start_time

templates = Jinja2Templates(directory="templates")

@app.get("/ping")
def ping():
    return "pong"

@app.get("/",response_class=HTMLResponse)
def read_root(request: Request, start_time: datetime = Depends(get_start_time)):
    return templates.TemplateResponse("wlcm.html", {"request": request, "start_time": start_time})

@app.get("/get_table/{table_name}")
def get_table(table_name:str):
    return crud.get_table(base.SessionLocal(), table_name=table_name)

@app.get("/get_all/")
def get_join_base():
    return crud.get_all(base.SessionLocal())

@app.get("/get_var")
def get_join_base():
    return crud.get_var(base.SessionLocal())

@app.post("/set_device")
async def set_base_item(file:UploadFile):
    file = await file.read()
    return crud.set_device(base.SessionLocal(), file=file)

@app.post("/set_table_item/{table_name}")
async def set_table_item(file:UploadFile, table_name:str):
    file = await file.read()
    return crud.set_item(base.SessionLocal(), table_name=table_name, file=file)

@app.post("/del_table_item/{table_name}")
async def del_table_item(file:UploadFile, table_name:str):
    file = await file.read()
    return crud.del_item(base.SessionLocal(), table_name=table_name, file=file)