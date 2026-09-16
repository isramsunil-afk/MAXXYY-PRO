from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
import os

app = FastAPI()

# PWA FILES
@app.get("/manifest.json")
def manifest():
    return FileResponse("manifest.json") if os.path.exists("manifest.json") else FileResponse("templates/manifest.json") if os.path.exists("templates/manifest.json") else {"name":"MAXXYY PRO"}

@app.get("/sw.js")
def sw():
    return FileResponse("sw.js") if os.path.exists("sw.js") else FileResponse("templates/sw.js") if os.path.exists("templates/sw.js") else HTMLResponse("")

@app.get("/logo.png")
def logo():
    for p in ["logo.png","templates/logo.png","static/logo.png"]:
        if os.path.exists(p):
            return FileResponse(p)
    return FileResponse("manifest.json")

# MAIN SITE - DIRECT HTML - NO TEMPLATE ERROR
@app.get("/", response_class=HTMLResponse)
@app.get("/dashboard", response_class=HTMLResponse)
def home():
    return """
<!DOCTYPE html>
<html><head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>MAXXYY PRO</title>
<link rel="manifest" href="/manifest.json">
<meta name="theme-color" content="#00ff00">
<style>
body{background:#000;color:#fff;font-family:Arial;text-align:center;padding:20px;margin:0}
h1{color:#00ff88;font-size:32px;margin-top:30px}
.box{background:#111;border:2px solid #00ff88;border-radius:15px;padding:25px;margin:20px auto;max-width:380px}
button{background:#00ff88;color:#000;border:none;padding:16px 30px;border-radius:12px;font-weight:bold;font-size:18px;width:100%;margin-top:10px}
#install{background:#fff}
</style>
</head><body>
<h1>MAXXYY PRO 🔥</h1>
<p>Trading Dashboard - LIVE</p>
<div class="box">
<h2>✅ App Working 100%!</h2>
<p id="status">Checking PWA...</p>
<button id="install">📲 INSTALL APP</button>
<button onclick="location.reload()">Refresh</button>
</div>
<script>
if('serviceWorker' in navigator){navigator.serviceWorker.register('/sw.js').then(()=>{document.getElementById('status').innerHTML='✅ Ready To Install!'}).catch(()=>{document.getElementById('status').innerHTML='✅ Ready (Click 3 dots -> Install)'});}
let deferredPrompt;
window.addEventListener('beforeinstallprompt',(e)=>{e.preventDefault();deferredPrompt=e;document.getElementById('status').innerHTML='✅ Click INSTALL button below!';});
document.getElementById('install').addEventListener('click',()=>{
 if(deferredPrompt){deferredPrompt.prompt();deferredPrompt.userChoice.then(c=>{if(c.outcome==='accepted')alert('GETHU NANNA! Installed 🔥')});}
 else{alert('Chrome paine 3 dots (...) -> Add to Home Screen / Install App nokku nanna!');}
});
</script>
</body></html>
    """

@app.get("/health")
def health():
    return {"status":"LIVE","app":"MAXXYY PRO"}
