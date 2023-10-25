import sqlalchemy as _db
import sqlalchemy.orm as _orm
from src.databases import database as _database


class Rating(_database.Base):
    __tablename__ = "ratings"

    id = _db.Column(_db.Integer, primary_key=True)
    rate = _db.Column(_db.Numeric(precision=10, scale=2), nullable=False)
    count = _db.Column(_db.Integer)

    product_id = _db.Column(_db.Integer, _db.ForeignKey('products.id'))

