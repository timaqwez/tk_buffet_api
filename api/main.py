from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

app = FastAPI(debug=True)
app.mount('/static', StaticFiles(directory='api/static'), name='static')


