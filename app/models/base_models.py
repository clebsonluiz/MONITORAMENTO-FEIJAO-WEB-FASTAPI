from pydantic import BaseModel, Field

from typing import Optional, List
from datetime import datetime


class Sensor(BaseModel):
    nome: Optional[str] = Field(None, example="Sensor de Temperatura e Umidade (DHT11)")
    monitorando: Optional[str] = None
    status: Optional[List['str']] = Field([], example=[
        "Temperatura: 30.0 ºC", "Umidade: 60%"
        ])
    data_obtencao: int = int(datetime.timestamp(datetime.now()) * 1000)
