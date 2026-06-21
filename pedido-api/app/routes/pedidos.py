from fastapi import APIRouter, status

from app.database import pedidos_collection
from app.models import Pedido
from app.schemas import PedidoCreate

from app.rabbitmq import publicar_pedido_criado
from app.kafka_producer import publicar_evento_pedido_criado

router = APIRouter(tags=["Pedidos"])


@router.post("/pedidos", status_code=status.HTTP_200_OK)
def criar_pedido(dados: PedidoCreate):

    pedido = Pedido.criar(
        cliente=dados.cliente,
        produto=dados.produto,
        quantidade=dados.quantidade
    )

    result = pedidos_collection.insert_one(pedido)

    pedido_id = str(result.inserted_id)

    publicar_pedido_criado(pedido_id)

    publicar_evento_pedido_criado(
        pedido_id,
        pedido["cliente"]
    )

    pedido["_id"] = pedido_id

    return pedido


@router.get("/pedidos")
def listar_pedidos():

    pedidos = []

    for pedido in pedidos_collection.find():
        pedido["_id"] = str(pedido["_id"])
        pedidos.append(pedido)

    return pedidos