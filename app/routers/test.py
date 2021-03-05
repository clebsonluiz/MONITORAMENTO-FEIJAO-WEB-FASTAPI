
from fastapi import APIRouter
from typing import Optional

router = APIRouter()

@router.get("/")
def read_root(opitional_param: Optional[str] = None):
    if opitional_param:
        return {
            "Message": {"Hello": "World"},  
            "Optional Param": opitional_param
        }
    return {"Hello": "World"}

