from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import base_route, product_route
from models.product import Product  # Asegúrate de importar el modelo Product si no lo has hecho.
from services.base_service import BaseService
from services.product_service import ProductService

app = FastAPI()

# Configurar el middleware para permitir solicitudes desde cualquier origen (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inicializa tu lista de datos, por ejemplo, una lista de objetos Product
data = []

# Crea instancias de tus servicios
base_service = BaseService(data)
product_service = ProductService(data)

base_router = base_route.router
product_router = product_route.router

app.include_router(base_router, prefix="/fakestoreapi.com/bases")
app.include_router(product_router, prefix="/fakestoreapi.com/products")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
