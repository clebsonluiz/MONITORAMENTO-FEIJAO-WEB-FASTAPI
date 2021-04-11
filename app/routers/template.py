
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
    return templates.TemplateResponse("index.html", {"request": request})

