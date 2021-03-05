from pydantic import BaseModel, Field

from typing import Optional
from datetime import datetime


class Monitora(BaseModel):
    monitorando: Optional[str] = None
    temperatura: Optional[str] = None
    umidade: Optional[str] = None

    class Config:
        schema_extra = {
            "example":{
                "monitorando": "Atmosfera Interna",
                "temperatura": "28° C",
                "umidade": "20%"
            }
        }


class Sensor(BaseModel):
    nome: Optional[str] = Field(None, example="Sensor de Temperatura e Umidade (DHT11)")
    monitora: Optional[Monitora] = None
    data_obtencao: int = int(datetime.timestamp(datetime.now()))
