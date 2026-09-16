from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/logo.png")
def logo():
    if os.path.exists("logo.png"):
        return FileResponse("logo.png")
    if os.path.exists("templates/logo.png"):
        return FileResponse("templates/logo.png")
    return {"error": "logo not found"}

@app.get("/manifest.json")
def manifest_file():
    return FileResponse("manifest.json")

@app.get("/sw.js")
def sw_file():
    return FileResponse("sw.js")
