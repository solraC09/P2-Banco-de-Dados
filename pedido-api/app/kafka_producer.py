import json
from os import getenv
from dotenv import load_dotenv
from kafka import KafkaProducer

load_dotenv()

KAFKA_BOOTSTRAP_SERVERS = getenv("KAFKA_BOOTSTRAP_SERVERS")
KAFKA_TOPIC = getenv("KAFKA_TOPIC")

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)


def publicar_evento_pedido_criado(pedido_id: str, cliente: str):
    evento = {
        "evento": "PEDIDO_CRIADO",
        "pedido_id": pedido_id,
        "cliente": cliente
    }

    producer.send(KAFKA_TOPIC, evento)
    producer.flush()