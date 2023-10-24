from typing import List
from pydantic import BaseModel

class BaseService:
    def find_all(self) -> List[BaseModel]:
        pass

    def find_by_id(self, id: int) -> BaseModel:
        pass

    def save(self, entity: BaseModel) -> BaseModel:
        pass

    def update(self, id: int, entity: BaseModel) -> BaseModel:
        pass

    def delete(self, id: int) -> bool:
        pass
