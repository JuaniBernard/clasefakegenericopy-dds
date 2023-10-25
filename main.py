from typing import List

import sqlalchemy.orm as _orm
import fastapi as _fastapi

from src.schemas import schemas as _schemas
from src.services import services as _services

app = _fastapi.FastAPI()

_services.create_database()


@app.on_event("startup")
async def startup_event():
    app.state.base_path = "/fakestoreapi.com"


@app.post("/products", response_model=_schemas.Product)
def create_product(
    product: _schemas.ProductCreate, db: _orm.Session = _fastapi.Depends(_services.get_db)
):
    return _services.create_product(db=db, product=product)


@app.get("/products", response_model=List[_schemas.Product])
def read_products(
    skip: int = 0,
    limit: int = 10,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    products = _services.get_products(db=db, skip=skip, limit=limit)
    return products


@app.get("/products/{product_id}", response_model=_schemas.Product)
def read_product(product_id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    product = _services.get_product(db=db, product_id=product_id)
    if product is None:
        raise _fastapi.HTTPException(
            status_code=404, detail="Sorry, this product does not exist"
        )
    return product


@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    _services.delete_product(db=db, product_id=product_id)
    return {"message": f"Successfully deleted product with id: {product_id}"}


@app.put("/products/{product_id}", response_model=_schemas.Product)
def update_product(
    product_id: int,
    product: _schemas.ProductCreate,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    return _services.update_product(db=db, product=product, product_id=product_id)


@app.get("/products/price_higher_than/{minimum_price}", response_model=List[_schemas.Product])
def search_price_higher_than(
    minimum_price: float, db: _orm.Session = _fastapi.Depends(_services.get_db)
):
    products = _services.search_price_higher_than(db=db, minimum_price=minimum_price)
    return products


@app.get("/products/price_between/{minimum_price}/{maximum_price}", response_model=List[_schemas.Product])
def search_price_between(
    minimum_price: float, maximum_price: float, db: _orm.Session = _fastapi.Depends(_services.get_db)
):
    products = _services.search_price_between(db=db, minimum_price=minimum_price, maximum_price=maximum_price)
    return products


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
