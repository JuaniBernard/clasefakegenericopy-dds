from typing import List
from models.product import Product
from repositories.product_repository import ProductRepository
from services.base_service import BaseService


class ProductService(BaseService):
    data = []  # Inicializa esta lista con objetos Product

    def find_all(self) -> List[Product]:
        return self.data

    def find_by_id(self, id: int) -> Product:
        for product in self.data:
            if product.id == id:
                return product

    def save(self, entity: Product) -> Product:
        entity.id = len(self.data) + 1  # Simula una asignación de ID
        self.data.append(entity)
        return entity

    def update(self, id: int, entity: Product) -> Product:
        for i, product in enumerate(self.data):
            if product.id == id:
                self.data[i] = entity
                return entity

    def delete(self, id: int) -> bool:
        for product in self.data:
            if product.id == id:
                self.data.remove(product)
                return True
        return False

    def search_price_higher_than(self, minimum_price: float) -> List[Product]:
        return [product for product in self.data if product.price > minimum_price]

    def search_price_between(self, minimum_price: float, maximum_price: float) -> List[Product]:
        return [product for product in self.data if minimum_price < product.price < maximum_price]
