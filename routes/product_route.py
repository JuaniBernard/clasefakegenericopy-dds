from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

from models.product import Product
from services.product_service import ProductService

router = APIRouter()

class ProductRoute:
    def __init__(self, service: ProductService):
        self.service = service

    @router.get("/higher", response_model=List[Product])
    def search_price_higher_than(self, minimum_price: float):
        return self.service.search_price_higher_than(minimum_price)

    @router.get("/between", response_model=List[Product])
    def search_price_between(self, minimum_price: float, maximum_price: float):
        return self.service.search_price_between(minimum_price, maximum_price)
