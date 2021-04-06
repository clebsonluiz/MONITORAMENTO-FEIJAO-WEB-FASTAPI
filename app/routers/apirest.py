from fastapi import APIRouter
from typing import List, Optional

from ..config import DETA_BASE_NAME
from ..models import DB, Sensor
from datetime import datetime


router = APIRouter()

__BASE_NAME = DETA_BASE_NAME


@router.get("/nome/{nome}")
def get_one_by_nome(nome: str):
    """
    function to router '/nome/{nome}' on method 'GET' 
    to find a object Sensor by name in Deta Base
    
    :param nome: str name of entry
    :return: a json result
    """
    base = DB.connect(__BASE_NAME)
    find = next(base.fetch({'nome':nome}))
    return find[0] if len(find) > 0 else {}


@router.get("/{key}")
def get_one(key: str):
    """
    function to router '/{key}' on method 'GET' 
    to find one object Sensor in Deta Base
    
    :param key: str unique key of entry
    :return: a json result
    """
    return DB.connect(__BASE_NAME).get(key)


@router.get("/", response_model=List[Sensor])
def get_all():
    """
    function to router '/' on method 'GET' 
    to get all of objects Sensor in Deta Base
    
    :return: a json list result of Sensors
    """
    base = DB.connect(__BASE_NAME)
    return next(base.fetch())


@router.put("/{key}", status_code=201, )
def put(key: str, sensor: Sensor):
    """
    function to router '/{key}' on method 'PUT' 
    to update a previous object Sensor with the new 
    in body http on Deta Base
    
    :param key: str unique key to find and update the entry
    :param sensor: Sensor object like json
    :return: a json result
    """
    base = DB.connect(__BASE_NAME)
    _json = base.get(key)
    to_update = Sensor(**(_json if _json != None else {}))
    update_data = sensor.dict(exclude_unset=True)
    update_data['data_obtencao'] = int(datetime.timestamp(datetime.now()) * 1000)
    updated = to_update.copy(update=update_data)

    return base.put(updated.dict(), key)


@router.post("/", status_code=201)
def post(sensor: Sensor):
    """
    function to router '/' on method 'POST' 
    to Post a new object Sensor in body http on Deta Base
    
    :param sensor: Sensor object like json
    :return: a json result
    """
    return DB.connect(__BASE_NAME).insert(sensor.dict())


@router.delete("/{key}", status_code=204)
def delete(key: str):
    """
    function to router '/{key}' on method 'DELETE' 
    to delete a object on Deta Base
    
    :param key: str unique key to find and delete entry
    """
    base = DB.connect(__BASE_NAME)
    base.delete(key)
