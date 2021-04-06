
from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


templates = Jinja2Templates(directory="templates")


router = APIRouter()

@router.get("/", response_class=HTMLResponse)
def index_root(request: Request):
    """
    function to main router '/' on method 'GET'

    
    :return: HTML response
    """
    _json = {
        "Olá povo do grupo": "</Sertão Dev>",
        "Por": "Clébson Luiz :)",
        "Infos": [
            {
                "Micro Serviço Usado Para Deploy": "Deta Micros",
                "Acesse a Documentação com o endpoint": "https://<the_path>.deta.dev/docs",
                "Outrem...": "https://<the_path>.deta.dev/redoc"
            },
            "Aplicação simples desenvolvida em Python " +
            "utilizando o modulo FastApi para fins de teste e aprendizado!",
        ],
        "Para mais informações": "https://docs.deta.sh"
    }
    return templates.TemplateResponse("index.html", {"request": request})

