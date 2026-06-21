from uuid import uuid4


class Pedido:
    @staticmethod
    def criar(cliente: str, produto: str, quantidade: int):
        return {
            "id": str(uuid4()),
            "cliente": cliente,
            "produto": produto,
            "quantidade": quantidade,
            "status": "PENDENTE"
        }