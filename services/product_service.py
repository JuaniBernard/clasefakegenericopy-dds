from typing import List
from models.product import Product
from repositories.product_repository import ProductRepository
from services.base_service import BaseService


class ProductService(BaseService):
    def __init__(self, repository: ProductRepository):
        super().__init__(repository)

    def search_price_higher_than(self, minimum_price: float) -> List[Product]:
        return self.repository.search_price_higher_than(minimum_price)

    def search_price_between(self, minimum_price: float, maximum_price: float) -> List[Product]:
        return self.repository.search_price_between(minimum_price, maximum_price)
