from typing import List
from models.base import Base


class BaseService:
    def __init__(self, repository):
        self.repository = repository

    def find_all(self) -> List[Base]:
        return self.repository.find_all()

    def find_by_id(self, id: int) -> Base:
        return self.repository.find_by_id(id)

    def save(self, entity: Base) -> Base:
        return self.repository.save(entity)

    def update(self, id: int, entity: Base) -> Base:
        return self.repository.update(id, entity)

    def delete(self, id: int) -> bool:
        return self.repository.delete(id)
