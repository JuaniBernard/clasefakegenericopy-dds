from pydantic import BaseModel


class Rating(BaseModel):
    rate: float
    count: int
