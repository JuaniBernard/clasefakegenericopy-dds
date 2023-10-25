from pydantic import BaseModel
from decimal import Decimal

from models.rating import Rating


class Product(BaseModel):
    title: str
    price: Decimal
    description: str
    category: str
    image: str
    rating: Rating
