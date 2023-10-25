from typing import List, TypeVar, Generic
from fastapi import HTTPException

ModelType = TypeVar("ModelType")


class BaseRepository(Generic[ModelType]):
    def __init__(self):
        self.data = []
        self.current_id = 1

    def find_all(self) -> List[ModelType]:
        return self.data

    def find_by_id(self, id: int) -> ModelType:
        for item in self.data:
            if item.id == id:
                return item
        raise HTTPException(status_code=404, detail="Entity not found")

    def save(self, entity: ModelType) -> ModelType:
        entity.id = self.current_id
        self.data.append(entity)
        self.current_id += 1
        return entity

    def update(self, id: int, entity: ModelType) -> ModelType:
        for i, item in enumerate(self.data):
            if item.id == id:
                entity.id = item.id
                self.data[i] = entity
                return entity
        raise HTTPException(status_code=404, detail="Entity not found")

    def delete(self, id: int) -> bool:
        for item in self.data:
            if item.id == id:
                self.data.remove(item)
                return True
        raise HTTPException(status_code=404, detail="Entity not found")
