from models.base import Base
from models.rating import Rating

class Product(Base):
    title: str
    price: float
    description: str
    category: str
    image: str
    rating: Rating

    # Anotaciones SQL
    def __table_args__(cls):
        return (Index('idx_product_price', cls.price),)