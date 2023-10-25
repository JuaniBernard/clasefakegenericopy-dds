from typing import List

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from models.rating import Rating
from services.product_service import ProductService

router = APIRouter()
product_service = ProductService()


class ProductIn(BaseModel):
    title: str
    price: float
    description: str
    category: str
    image: str
    rating: Rating


class ProductOut(ProductIn):
    id: int


@router.get("/", response_model=List[ProductOut])
def get_all():
    return product_service.find_all()


@router.get("/{id}", response_model=ProductOut)
def get_one(id: int):
    entity = product_service.find_by_id(id)
    if entity:
        return entity
    raise HTTPException(status_code=404, detail="Entity not found")


@router.post("/", response_model=ProductOut)
def save(entity: ProductIn):
    return product_service.save(entity)


@router.put("/{id}", response_model=ProductOut)
def update(id: int, entity: ProductIn):
    updated_entity = product_service.update(id, entity)
    if updated_entity:
        return updated_entity
    raise HTTPException(status_code=404, detail="Entity not found")


@router.delete("/{id}", response_model=bool)
def delete(id: int):
    result = product_service.delete(id)
    if result:
        return result
    raise HTTPException(status_code=404, detail="Entity not found")


@router.get("/higher", response_model=List[ProductOut])
def search_price_higher_than(minimumPrice: float):
    return product_service.search_price_higher_than(minimumPrice)


@router.get("/between", response_model=List[ProductOut])
def search_price_between(minimumPrice: float, maximumPrice: float):
    return product_service.search_price_between(minimumPrice, maximumPrice)
