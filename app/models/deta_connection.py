from typing import Dict
from deta import Deta
from deta.base import Base
from ..config import DETA_PROJECT_KEY, DETA_PROJECT_ID


# Deta Project Base
__DETA_DB = Deta(
        project_key=DETA_PROJECT_KEY,
        project_id=DETA_PROJECT_ID
    )

# Active bases find
__BASES: Dict[str, Base] = {}


def connect(base: str) -> Base:
    """
    function to connect on a existing Deta Base, 
    if doesn't extist, will be created
    
    :param base: str base name
    :return: Base deta
    """
    _base = __BASES.get(base)
    if _base == None:
        _base = __BASES[base] = db().Base(base)
    return _base


def db() -> Deta:
    """
    function to access deta project

    :return: Deta project
    """
    return __DETA_DB

