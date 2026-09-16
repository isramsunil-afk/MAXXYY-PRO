from fastapi import FastAPI, Request, Form, UploadFile, File
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
import os, json, shutil

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# --- LOGO FIX ---
@app.get("/logo.png")
def get_logo():
    if os.path.exists("logo.png"):
        return FileResponse("logo.png")
    return {"error": "no logo"}

# --- DATA SETUP ---
if not os.path.exists("data.json"):
    with open("data.json","w") as f:
        json.dump({"chats":[],"confessions":[],"lost":[],"files":[]}, f)
if not os.path.exists("uploads"):
    os.makedirs("uploads")

def get_data():
    with open("data.json") as f:
        return json.load(f)
def save_data(d):
    with open("data.json","w") as f:
        json.dump(d,f)

# --- PAGES ---
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

# --- APIS ---
@app.get("/api/chats")
def chats():
    return get_data().get("chats",[])[-50:]

@app.post("/api/chats")
async def post_chat(txt: str = Form(...)):
    d=get_data(); d.setdefault("chats",[]).append(txt); save_data(d)
    return {"ok":True}

@app.get("/api/confessions")
def confs():
    return get_data().get("confessions",[])[-50:]

@app.post("/api/confessions")
async def post_conf(txt: str = Form(...)):
    d=get_data(); d.setdefault("confessions",[]).append(txt); save_data(d)
    return {"ok":True}

@app.get("/api/lost")
def lost():
    return get_data().get("lost",[])[-50:]

@app.post("/api/lost")
async def post_lost(item: str = Form(...)):
    d=get_data(); d.setdefault("lost",[]).append(item); save_data(d)
    return {"ok":True}

@app.get("/api/files")
def files():
    return os.listdir("uploads")

@app.post("/api/upload")
async def upload(file: UploadFile = File(...)):
    path=f"uploads/{file.filename}"
    with open(path,"wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"ok":True}

@app.get("/files/{name}")
def get_file(name: str):
    return FileResponse(f"uploads/{name}")
