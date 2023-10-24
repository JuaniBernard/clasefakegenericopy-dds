from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import base_route, product_route

app = FastAPI()

# Configurar el middleware para permitir solicitudes desde cualquier origen (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Definir la ruta base
@app.on_event("startup")
async def startup_event():
    app.state.base_path = "/fakestoreapi.com/products"

base_router = base_route.router
product_router = product_route.router

app.include_router(base_router, prefix="/bases")
app.include_router(product_router, prefix="/products")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
