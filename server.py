from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

from fastapi.staticfiles import StaticFiles
import os

# Ee line app = FastAPI() ki kinda pettu
app.mount("/", StaticFiles(directory=".", html=False), name="static_root")

# Tarvata kindha ee routes unchu - rendu
@app.get("/manifest.json")
def manifest_file():
    return FileResponse("manifest.json")

@app.get("/sw.js")
def sw_file():
    return FileResponse("sw.js")

@app.get("/manifest.json")
def manifest_file():
    return FileResponse("manifest.json")

@app.get("/sw.js")
def sw_file():
    return FileResponse("sw.js")
