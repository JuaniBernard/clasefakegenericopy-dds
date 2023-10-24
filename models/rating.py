from models.base import Base

class Rating(Base):
    rate: float
    count: int
