from .abstract_model import AbstractModel
from database.db import db
from typing import Dict
from pymongo.collection import Collection


class LanguageModel(AbstractModel):
    _collection: Collection = db["languages"]

    def __init__(self, data: Dict[str, str]):
        super().__init__(data)
