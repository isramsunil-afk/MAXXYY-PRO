from fastapi import FastAPI, Request, UploadFile, File, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse, RedirectResponse
import os, json
app = FastAPI()
templates = Jinja2Templates(directory="templates")
os.makedirs("uploads", exist_ok=True)
os.makedirs("data", exist_ok=True)
def load_db(n):
    try: return json.load(open(f"data/{n}.json"))
    except: return []
def save_db(n,d):
    json.dump(d, open(f"data/{n}.json","w"))
@app.get("/")
def root(): return RedirectResponse("/login")
@app.get("/login")
async def page(request: Request):
    # FIXED FOR NEW VERSION
    return templates.TemplateResponse(request, "login.html", {})
@app.post("/login")
async def login(username: str = Form(...)):
    u=load_db("users")
    if username not in [x["name"] for x in u]:
        u.append({"name": username}); save_db("users",u)
    return RedirectResponse(f"/dashboard?user={username}", status_code=302)
@app.get("/dashboard")
async def dash(request: Request, user: str="Anon"):
    return templates.TemplateResponse(request, "dashboard.html", {"user": user})
@app.get("/api/chats")
def gc(): return load_db("chats")
@app.post("/api/chats")
async def pc(request: Request):
    data=await request.json(); c=load_db("chats"); c.append(data); save_db("chats",c); return {"ok": True}
@app.get("/api/confessions")
def gcf(): return load_db("confessions")
@app.post("/api/confessions")
async def pcf(request: Request):
    data=await request.json(); c=load_db("confessions"); c.append(data); save_db("confessions",c); return {"ok": True}
@app.get("/api/files")
def gf(): return os.listdir("uploads")
@app.post("/upload")
async def up(file: UploadFile = File(...)):
    open(os.path.join("uploads", file.filename), "wb").write(await file.read()); return {"ok": True}
@app.get("/download/{name}")
async def dl(name: str):
    return FileResponse(os.path.join("uploads", name), filename=name)
