from models.base import Base
from models.rating import Rating

class Product(Base):
    title: str
    price: float
    description: str
    category: str
    image: str
    rating: Rating
