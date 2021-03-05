from fastapi import APIRouter
from typing import List, Optional

from ..config import DETA_BASE_NAME
from ..models import DB, Sensor
from datetime import datetime


router = APIRouter()

__BASE_NAME = DETA_BASE_NAME


@router.get("/nome/{nome}")
def get_one_by_nome(nome: str):
    base = DB.connect(__BASE_NAME)
    find = next(base.fetch({'nome':nome}))
    return find[0] if len(find) > 0 else {}


@router.get("/{key}")
def get_one(key: str):
    return DB.connect(__BASE_NAME).get(key)


@router.get("/", response_model=List[Sensor])
def get_all():
    base = DB.connect(__BASE_NAME)
    return next(base.fetch())


@router.put("/{key}", status_code=203, )
def put(key: str, sensor: Sensor):
    
    base = DB.connect(__BASE_NAME)
    _json = base.get(key)
    to_update = Sensor(**(_json if _json != None else {}))
    update_data = sensor.dict(exclude_unset=True)
    updated = to_update.copy(update=update_data)

    return base.put(updated.dict(), key)


@router.post("/", status_code=201)
def post(sensor: Sensor):
    return DB.connect(__BASE_NAME).insert(sensor.dict())


@router.delete("/{key}", status_code=204)
def delete(key: str):
    base = DB.connect(__BASE_NAME)
    base.delete(key)
