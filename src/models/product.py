import sqlalchemy as _db
import sqlalchemy.orm as _orm
from src.databases import database as _database


class Product(_database.Base):
    __tablename__ = "products"

    id = _db.Column(_db.Integer, primary_key=True)
    title = _db.Column(_db.String, nullable=False)
    price = _db.Column(_db.Numeric(precision=10, scale=2), nullable=False)
    description = _db.Column(_db.String)
    category = _db.Column(_db.String)
    image = _db.Column(_db.String)

    rating = _orm.relationship("Rating", uselist=False)
