import sqlalchemy.orm as _orm
from src.models.product import Product
from src.models.rating import Rating
from src.schemas.schemas import ProductCreate
from src.databases import database as _database


def create_database():
    return _database.Base.metadata.create_all(bind=_database.engine)


def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_product(db: _orm.Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()


def get_products(db: _orm.Session, skip: int = 0, limit: int = 100):
    return db.query(Product).offset(skip).limit(limit).all()


def create_product(db: _orm.Session, product: ProductCreate):
    db_product = Product(title=product.title, price=product.price, description=product.description,
                         category=product.category, image=product.image, rating=Rating(rate=product.rating.rate,
                                                                                       count=product.rating.count))
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def update_product(db: _orm.Session, product_id: int, product: ProductCreate):
    db_product = get_product(db=db, product_id=product_id)
    db_product.title = product.title
    db_product.price = product.price
    db_product.description = product.description
    db_product.category = product.category
    db_product.image = product.image
    db_product.rating = Rating(rate=product.rating.rate, count=product.rating.count)
    db.commit()
    db.refresh(db_product)
    return db_product


def delete_product(db: _orm.Session, product_id: int):
    db.query(Product).filter(Product.id == product_id).delete()
    db.commit()


def search_price_higher_than(db: _orm.Session, minimum_price: float):
    products = db.query(Product).filter(Product.price > minimum_price).all()
    return products


def search_price_between(db: _orm.Session, minimum_price: float, maximum_price: float):
    products = db.query(Product).filter(Product.price > minimum_price, Product.price < maximum_price).all()
    return products
