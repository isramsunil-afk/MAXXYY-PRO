from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()

@app.get("/manifest.json")
def manifest():
    return {"name":"MAXXYY PRO","short_name":"MAXXYY","start_url":"/","display":"standalone","background_color":"#000000","theme_color":"#00ff00","icons":[{"src":"https://cdn-icons-png.flaticon.com/512/3081/3081559.png","sizes":"512x512","type":"image/png"}]}

@app.get("/sw.js")
def sw():
    return HTMLResponse("self.addEventListener('install',e=>self.skipWaiting());self.addEventListener('fetch',e=>{});", media_type="application/javascript")

@app.get("/", response_class=HTMLResponse)
def home():
    return """<!DOCTYPE html>
<html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>MAXXYY PRO</title><link rel="manifest" href="/manifest.json">
<style>
body{background:#0a0a0a;color:#fff;font-family:Arial;margin:0;padding:0}
.header{background:#00ff88;color:#000;padding:15px;text-align:center;font-weight:bold;font-size:22px}
.card{background:#151515;border:1px solid #00ff88;border-radius:12px;padding:15px;margin:12px}
.btn{background:#00ff88;color:#000;border:none;padding:14px;border-radius:10px;font-weight:bold;width:100%;font-size:16px}
.market{color:#00ff88;font-size:28px;font-weight:bold}
.install-box{background:#111;border:2px dashed #00ff88;border-radius:12px;padding:15px;margin:12px;text-align:center}
</style></head><body>
<div class="header">MAXXYY PRO 🔥 LIVE</div>

<div id="installBox" class="install-box">
<p>📲 Install chey - Play Store la use chey!</p>
<button class="btn" id="installBtn">INSTALL APP</button>
</div>

<div class="card"><div>Market Status</div><div class="market">● LIVE</div><p>Nifty: 24,850 ▲ 120</p></div>
<div class="card"><button class="btn">💹 Start Trading</button></div>
<div class="card"><button class="btn" style="background:#222;color:#fff;border:1px solid #00ff88" onclick="location.reload()">🔄 Refresh Data</button></div>

<script>
if('serviceWorker' in navigator){navigator.serviceWorker.register('/sw.js')}
let deferredPrompt;
window.addEventListener('beforeinstallprompt',e=>{e.preventDefault();deferredPrompt=e;document.getElementById('installBox').style.display='block';});
document.getElementById('installBtn').onclick=()=>{if(deferredPrompt){deferredPrompt.prompt();}};
if(window.matchMedia('(display-mode: standalone)').matches || window.navigator.standalone){
  document.getElementById('installBox').style.display='none';
}
</script>
</body></html>"""
