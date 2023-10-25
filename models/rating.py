from pydantic import BaseModel
from decimal import Decimal


class Rating(BaseModel):
    rate: Decimal
    count: int
