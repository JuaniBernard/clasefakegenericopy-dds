from models.product import Product
from services.base_service import BaseService
from typing import List

class ProductService(BaseService):
    def search_price_higher_than(self, minimum_price: float) -> List[Product]:
        pass

    def search_price_between(self, minimum_price: float, maximum_price: float) -> List[Product]:
        pass
