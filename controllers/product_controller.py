from typing import List
from fastapi import APIRouter, HTTPException
from models.product import Product
from repositories.product_repository import ProductRepository
from services.product_service import ProductService

router = APIRouter()
service = ProductService(ProductRepository())


@router.get("/", response_model=List[Product])
def get_all():
    return service.find_all()


@router.get("/{id}", response_model=Product)
def get_one(id: int):
    entity = service.find_by_id(id)
    if entity:
        return entity
    raise HTTPException(status_code=404, detail="Entity not found")


@router.post("/", response_model=Product)
def save(entity: Product):
    return service.save(entity)


@router.put("/{id}", response_model=Product)
def update(id: int, entity: Product):
    updated_entity = service.update(id, entity)
    if updated_entity:
        return updated_entity
    raise HTTPException(status_code=404, detail="Entity not found")


@router.delete("/{id}", response_model=bool)
def delete(id: int):
    result = service.delete(id)
    if result:
        return result
    raise HTTPException(status_code=404, detail="Entity not found")


@router.get("/higher", response_model=List[Product])
def search_price_higher_than(minimumPrice: float):
    return service.search_price_higher_than(minimumPrice)


@router.get("/between", response_model=List[Product])
def search_price_between(minimumPrice: float, maximumPrice: float):
    return service.search_price_between(minimumPrice, maximumPrice)
