from fastapi import APIRouter, FastAPI

from .test import router as test_router
from .apirest import router as api_router
from .template import router as templates_router


def create_routes(app: FastAPI):
    """
    Includes the routers to FastApi app endpoint
    """
    app.include_router(test_router)
    app.include_router(templates_router)
    app.include_router(
        api_router, 
        prefix="/api/sensores",
        tags=["API de Test"],
        responses={
            #200: {"description": "Sucesso"},
            #201: {"description": "Criado"},
            #203: {"description": "Atualizado"},
            #404: {"description": "Não Encontrado"}
            },
        )
