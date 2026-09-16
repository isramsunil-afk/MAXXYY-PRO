from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()

@app.get("/manifest.json")
def manifest():
    return {
        "name": "MAXXYY PRO",
        "short_name": "MAXXYY",
        "start_url": "/",
        "display": "standalone",
        "background_color": "#000000",
        "theme_color": "#00ff00",
        "icons": [{"src": "https://cdn-icons-png.flaticon.com/512/3081/3081559.png", "sizes": "512x512", "type": "image/png"}]
    }

@app.get("/sw.js")
def sw():
    return HTMLResponse("self.addEventListener('install',e=>self.skipWaiting());self.addEventListener('fetch',e=>{});", media_type="application/javascript")

@app.get("/", response_class=HTMLResponse)
@app.get("/dashboard", response_class=HTMLResponse)
def home():
    return """<!DOCTYPE html>
<html><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>MAXXYY PRO</title><link rel="manifest" href="/manifest.json">
<meta name="theme-color" content="#00ff00">
<style>body{background:#000;color:#fff;font-family:Arial;text-align:center;padding:20px;margin:0}h1{color:#00ff88;font-size:32px;margin-top:30px}.box{background:#111;border:2px solid #00ff88;border-radius:15px;padding:25px;margin:20px auto;max-width:380px}button{background:#00ff88;color:#000;border:none;padding:16px 30px;border-radius:12px;font-weight:bold;font-size:18px;width:100%;margin-top:10px}#install{background:#fff}</style>
</head><body>
<h1>MAXXYY PRO 🔥</h1><p>Trading Dashboard - LIVE</p>
<div class="box"><h2>✅ App Working 100%!</h2><p id="status">Checking PWA...</p><button id="install">📲 INSTALL APP</button><button onclick="location.reload()">Refresh</button></div>
<script>
if('serviceWorker' in navigator){navigator.serviceWorker.register('/sw.js').then(()=>{document.getElementById('status').innerHTML='✅ Ready To Install!'});}
let p;window.addEventListener('beforeinstallprompt',e=>{e.preventDefault();p=e;});
document.getElementById('install').onclick=()=>{if(p){p.prompt();}else{alert('Chrome 3 dots -> Add to Home Screen');}}
if(window.matchMedia('(display-mode: standalone)').matches){document.getElementById('status').innerHTML='🔥 APP INSTALLED - Welcome Nanna!';document.getElementById('install').style.display='none';}
</script></body></html>"""
