from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

if os.path.exists("templates"):
    app.mount("/templates", StaticFiles(directory="templates"), name="templates_static")

@app.get("/manifest.json")
def manifest_file():
    if os.path.exists("manifest.json"):
        return FileResponse("manifest.json")
    return {"error": "manifest not found"}

@app.get("/sw.js")
def sw_file():
    if os.path.exists("sw.js"):
        return FileResponse("sw.js")
    return {"error": "sw not found"}

@app.get("/logo.png")
def logo_file():
    
    if os.path.exists("logo.png"):
        return FileResponse("logo.png")
    if os.path.exists("templates/logo.png"):
        return FileResponse("templates/logo.png")
    if os.path.exists("static/logo.png"):
        return FileResponse("static/logo.png")
    return FileResponse("manifest.json")  
    
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    try:
        return templates.TemplateResponse("dashboard.html", {"request": request})
    except:
        return HTMLResponse("<h1>MAXXYY PRO LIVE 🔥</h1><p>Dashboard loading...</p><a href='/dashboard'>Go to Dashboard</a>")

@app.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request):
    try:
        return templates.TemplateResponse("dashboard.html", {"request": request})
    except:
        return HTMLResponse("<h1>MAXXYY PRO Dashboard</h1><p>Working!</p>")

@app.get("/health")
def health():
    return {"status": "MAXXYY PRO is Live 🔥", "pwa": "ready"}
