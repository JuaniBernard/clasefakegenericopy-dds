from typing import List
from models.base import Base


class BaseService:
    def find_all(self) -> List[Base]:
        pass

    def find_by_id(self, id: int) -> Base:
        pass

    def save(self, entity: Base) -> Base:
        pass

    def update(self, id: int, entity: Base) -> Base:
        pass

    def delete(self, id: int) -> bool:
        pass
