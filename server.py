from fastapi import FastAPI, Request, Form, UploadFile
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
import os, json, shutil

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# LOGO ROUTE - IMPORTANT
@app.get("/logo.png")
def get_logo():
    return FileResponse("logo.png")

# DATA
if not os.path.exists("data.json"):
    with open("data.json","w") as f:
        json.dump({"chats":[],"confessions":[],"lost":[]}, f)

def get_data():
    with open("data.json") as f:
        return json.load(f)

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

@app.get("/api/chats")
def chats():
    return get_data()["chats"][-50:]

@app.post("/api/chats")
async def post_chat(txt: str = Form(...)):
    data = get_data()
    data["chats"].append(txt)
    with open("data.json","w") as f:
        json.dump(data,f)
    return {"ok":True}

@app.get("/api/confessions")
def confs():
    return get_data()["confessions"][-50:]

@app.post("/api/confessions")
async def post_conf(txt: str = Form(...)):
    data = get_data()
    data["confessions"].append(txt)
    with open("data.json","w") as f:
        json.dump(data,f)
    return {"ok":True}

# NEW - LOST & FOUND
@app.get("/api/lost")
def lost():
    return get_data()["lost"]

@app.post("/api/lost")
async def post_lost(item: str = Form(...)):
    data = get_data()
    data["lost"].append(item)
    with open("data.json","w") as f:
        json.dump(data,f)
    return {"ok":True}
