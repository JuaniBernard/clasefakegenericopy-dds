from typing import List
from pydantic import BaseModel

class BaseService:
    def __init__(self, data: List[BaseModel]):
        self.data = data

    def find_all(self) -> List[BaseModel]:
        return self.data

    def find_by_id(self, id: int) -> BaseModel:
        for entity in self.data:
            if entity.id == id:
                return entity
        return None

    def save(self, entity: BaseModel) -> BaseModel:
        entity.id = len(self.data) + 1
        self.data.append(entity)
        return entity

    def update(self, id: int, entity: BaseModel) -> BaseModel:
        for i, existing_entity in enumerate(self.data):
            if existing_entity.id == id:
                self.data[i] = entity
                return entity
        return None

    def delete(self, id: int) -> bool:
        for i, entity in enumerate(self.data):
            if entity.id == id:
                del self.data[i]
                return True
        return False
