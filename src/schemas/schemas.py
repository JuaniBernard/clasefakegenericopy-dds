from pydantic import BaseModel


class _RatingBase(BaseModel):
    rate: float
    count: int


class RatingCreate(_RatingBase):
    pass


class Rating(_RatingBase):
    id: int

    class Config:
        orm_mode = True


class _ProductBase(BaseModel):
    title: str
    price: float
    description: str = None
    category: str = None
    image: str = None
    rating: Rating


class ProductCreate(_ProductBase):
    pass


class Product(_ProductBase):
    id: int
    rating: Rating = None

    class Config:
        orm_mode = True
