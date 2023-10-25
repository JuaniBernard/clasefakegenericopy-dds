from pydantic import BaseModel
from models.rating import Rating


class Product(BaseModel):
    title: str
    price: float
    description: str
    category: str
    image: str
    rating: Rating
