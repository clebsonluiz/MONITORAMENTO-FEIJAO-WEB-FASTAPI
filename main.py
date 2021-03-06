__author__ = 'Clébson Luiz'
__version__ = "1.0-alpha"
__description__ = "Projeto para aprendizado de micro-serviços e api's"


import uvicorn 

from fastapi import FastAPI

from app.routers import create_routes
from app.config import *


def create_app() -> FastAPI:    
    """
    Create the main App

    :return: FastApi app
    """
    _app = FastAPI()
    create_routes(app=_app)
    return _app


app = create_app()


if __name__ == "__main__":
    """
    To run in localhost:
    """
    uvicorn.run("main:app", host=HOST, port=PORT, reload=RELOAD_APP)
