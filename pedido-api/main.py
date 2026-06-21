from fastapi import FastAPI

from app.routes.pedidos import router as pedidos_router

app = FastAPI(
    title="API de Gerenciamento de Pedidos",
    version="1.0.0",
    description="API para gerenciamento de pedidos utilizando MongoDB, RabbitMQ e Kafka."
)

app.include_router(pedidos_router)


@app.get("/")
def home():
    return {
        "mensagem": "API de Pedidos em execução"
    }