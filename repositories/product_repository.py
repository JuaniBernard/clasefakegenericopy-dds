from typing import List
from fastapi import HTTPException
from pydantic import BaseModel
from base_repository import BaseRepository
from models.product import Product


class ProductRepository(BaseRepository[Product]):
    def search_price_higher_than(self, minimum_price: float) -> List[Product]:
        results = [product for product in self.data if product.price > minimum_price]
        return results

    def search_price_between(self, minimum_price: float, maximum_price: float) -> List[Product]:
        results = [product for product in self.data if minimum_price < product.price < maximum_price]
        return results
