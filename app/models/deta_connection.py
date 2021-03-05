from typing import Dict
from deta import Deta
from deta.base import Base
from ..config import DETA_PROJECT_KEY, DETA_PROJECT_ID


__DETA_DB = Deta(
        project_key=DETA_PROJECT_KEY,
        project_id=DETA_PROJECT_ID
    )

__BASES: Dict[str, Base] = {}


def connect(base: str) -> Base:
    _base = __BASES.get(base)
    if _base == None:
        _base = __BASES[base] = db().Base(base)
    return _base


def db() -> Deta:
    return __DETA_DB

