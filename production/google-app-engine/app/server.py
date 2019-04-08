from starlette.applications import Starlette
from starlette.responses import HTMLResponse, JSONResponse
from starlette.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
import uvicorn, aiohttp, asyncio
from io import BytesIO

from fastai import *
from fastai.vision import *

model_file_url = 'https://doc-0g-b8-docs.googleusercontent.com/docs/securesc/dpu5qh538s0ikhgndk52d3ktb6c7433t/7h9ujimtphoerag3f51gtvobgrhhhuso/1554544800000/08844475752152095245/08844475752152095245/1mJO5kjeBGl30Ogryk5s1xFzP8dSuY2eK?e=download'
model_file_name = 'model'
classes = ['car', 'bike']
path = Path(__file__).parent

app = Starlette()
app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_headers=['X-Requested-With', 'Content-Type'])
app.mount('/static', StaticFiles(directory='app/static'))

async def download_file(url, dest):
    if dest.exists(): return
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.read()
            with open(dest, 'wb') as f: f.write(data)

async def setup_learner():
    await download_file(model_file_url, path/'models'/f'{model_file_name}.pth')
    
	# data_bunch = ImageDataBunch.single_from_classes(path, classes,
	 #    tfms=get_transforms(), size=224).normalize(imagenet_stats)
    # learn = cnn_learner(data_bunch, models.resnet34, pretrained=False)
    # learn.load(model_file_name)
	
    learn = load_learner(path/'models')
    return learn

loop = asyncio.get_event_loop()
tasks = [asyncio.ensure_future(setup_learner())]
learn = loop.run_until_complete(asyncio.gather(*tasks))[0]
loop.close()

@app.route('/')
def index(request):
    html = path/'view'/'index.html'
    return HTMLResponse(html.open().read())

@app.route('/analyze', methods=['POST'])
async def analyze(request):
    data = await request.form()
    img_bytes = await (data['file'].read())
    img = open_image(BytesIO(img_bytes))
    return JSONResponse({'result': learn.predict(img)[0].obj})

if __name__ == '__main__':
    if 'serve' in sys.argv: uvicorn.run(app, host='0.0.0.0', port=8080)

