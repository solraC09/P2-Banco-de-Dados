import json
import pika
from os import getenv
from dotenv import load_dotenv

load_dotenv()

RABBITMQ_HOST = getenv("RABBITMQ_HOST")
RABBITMQ_QUEUE = getenv("RABBITMQ_QUEUE")


def publicar_pedido_criado(pedido_id: str):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=RABBITMQ_HOST)
    )

    channel = connection.channel()

    channel.queue_declare(queue=RABBITMQ_QUEUE, durable=True)

    mensagem = {
        "pedido_id": pedido_id,
        "acao": "pedido_criado"
    }

    channel.basic_publish(
        exchange="",
        routing_key=RABBITMQ_QUEUE,
        body=json.dumps(mensagem),
        properties=pika.BasicProperties(
            delivery_mode=2
        )
    )

    connection.close()