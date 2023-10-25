from fastapi import FastAPI
from routes import routes as product_router

app = FastAPI()

app.include_router(product_router, prefix="/fakestoreapi.com/products", tags=["products"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
