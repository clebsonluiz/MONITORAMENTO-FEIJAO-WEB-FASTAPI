
from fastapi import APIRouter
from typing import Optional

router = APIRouter()

@router.get("/")
def read_root(opitional_param: Optional[str] = None):
    """
    function to router '/' on method 'GET'

    :param opitional_param: str to test response
    :return: JSON response
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
    if opitional_param:
        _temp = _json.copy()
        _temp["Parametro Opcional foi..."] = opitional_param
        return _temp
    return _json

