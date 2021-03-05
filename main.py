import uvicorn 

from fastapi import FastAPI

from app.routers import create_routes
from app.config import *

def create_app() -> FastAPI:    

    _app = FastAPI()
    create_routes(app=_app)
    return _app


app = create_app()


if __name__ == "__main__":
    uvicorn.run("main:app", host=HOST, port=PORT, reload=RELOAD_APP)
