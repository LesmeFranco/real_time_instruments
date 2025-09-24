from microdot import Microdot
from microdot import send_file
from mpu import get_mpu_data

app = Microdot()

@app.get('/api/mpu')
async def api_mpu(request):
    data = get_mpu_data()
    return data

@app.get('/')
async def index(request):
    return send_file('index.html')

@app.get('/styles/style.css')
async def style_css(request):
    return send_file('styles/style.css')

@app.get('/styles/flight-indicators.css')
async def flight_css(request):
    return send_file('styles/flight-indicators.css')

@app.get('/scripts/script.js')
async def script_js(request):
    return send_file('scripts/script.js')

@app.get('/scripts/flight-indicators.js')
async def flight_js(request):
    return send_file('scripts/flight-indicators.js')

@app.get('/esm/module-flight-indicators.mjs')
async def flight_js(request):
    return send_file('esm/module-flight-indicators.mjs', content_type='text/javascript')

@app.get('/img/horizon_circle.svg')
async def image(request):
    return send_file('img/horizon_circle.svg')

@app.get('/img/horizon_mechanics.svg')
async def image(request):
    return send_file('img/horizon_mechanics.svg')

@app.get('/img/horizon_ball.svg')
async def image(request):
    return send_file('img/horizon_ball.svg')

@app.get('/img/horizon_back.svg')
async def image(request):
    return send_file('img/horizon_back.svg')

@app.get('/img/speed_mechanics.svg')
async def image(request):
    return send_file('img/speed_mechanics.svg')

@app.get('/img/fi_needle.svg')
async def image(request):
    return send_file('img/fi_needle.svg')

@app.get('/img/fi_circle.svg')
async def image(request):
    return send_file('img/fi_circle.svg')

@app.get('/img/fi_box.svg')
async def image(request):
    return send_file('img/fi_box.svg')

@app.get('/img/fi_tc_airplane.svg')
async def image(request):
    return send_file('img/fi_tc_airplane.svg')

@app.get('/img/heading_mechanics.svg')
async def image(request):
    return send_file('img/heading_mechanics.svg')

@app.get('/img/heading_yaw.svg')
async def image(request):
    return send_file('img/heading_yaw.svg')


app.run()