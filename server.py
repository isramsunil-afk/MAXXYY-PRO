from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/logo.png")
def logo():
    # logo ekkada unna chusi ivvu
    if os.path.exists("logo.png"):
        return FileResponse("logo.png")
    if os.path.exists("templates/logo.png"):
        return FileResponse("templates/logo.png")
    return {"error": "logo not found"}

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

@app.get("/api/ping")
def ping():
    return {"ok": True}
