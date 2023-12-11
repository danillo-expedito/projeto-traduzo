from .abstract_model import AbstractModel
from database.db import db
from typing import Dict, List
from pymongo.collection import Collection


class LanguageModel(AbstractModel):
    _collection: Collection = db["languages"]

    def __init__(self, data: Dict[str, str]):
        super().__init__(data)

    def to_dict(self) -> Dict[str, str]:
        return {
            "name": self.data["name"],
            "acronym": self.data["acronym"],
        }

    @classmethod
    def list_dicts(cls) -> List[Dict[str, str]]:
        languages = cls.find()
        return [
            language.to_dict()
            for language in languages
        ]
