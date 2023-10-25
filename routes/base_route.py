from typing import List

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from services.base_service import BaseService

router = APIRouter()

class BaseRoute:
    def __init__(self, service: BaseService):
        self.service = service

    @router.get("/")
    def get_all(self):
        return self.service.find_all()

    @router.get("/{id}")
    def get_one(self, id: int):
        entity = self.service.find_by_id(id)
        if entity:
            return entity
        raise HTTPException(status_code=404, detail="Entity not found")

    @router.post("/")
    def save(self, entity: BaseModel):
        return self.service.save(entity)

    @router.put("/{id}")
    def update(self, id: int, entity: BaseModel):
        updated_entity = self.service.update(id, entity)
        if updated_entity:
            return updated_entity
        raise HTTPException(status_code=404, detail="Entity not found")

    @router.delete("/{id}", response_model=bool)
    def delete(self, id: int):
        result = self.service.delete(id)
        if result:
            return result
        raise HTTPException(status_code=404, detail="Entity not found")
