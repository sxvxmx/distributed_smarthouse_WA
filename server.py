from fastapi import FastAPI, UploadFile, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import base, crud
from datetime import datetime

app = FastAPI()
app.mount("/static", StaticFiles(directory="resources"), name="static")

server_start_time = None

@app.on_event("startup")
async def startup_event():
    global server_start_time
    server_start_time = datetime.utcnow()

def get_start_time():
    return server_start_time

templates = Jinja2Templates(directory="templates")

@app.get("/ping")
def ping():
    return "pong"

@app.get("/",response_class=HTMLResponse)
def read_root(request: Request, start_time: datetime = Depends(get_start_time)):
    return templates.TemplateResponse("wlcm.html", {"request": request, "start_time": start_time})

@app.get("/get_base/{base_name}")
def get_base(base_name:str):
    return crud.get_all(base.SessionLocal(), base_name=base_name)

@app.post("/set_base_item/{base_name}")
async def set_base_item(file:UploadFile, base_name:str):
    file = await file.read()
    return crud.set_item(base.SessionLocal(), base_name=base_name, file=file)

@app.post("/del_base_item/{base_name}")
async def set_base_item(file:UploadFile, base_name:str):
    file = await file.read()
    return crud.del_item(base.SessionLocal(), base_name=base_name, file=file)