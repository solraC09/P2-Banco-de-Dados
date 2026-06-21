from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_criar_pedido():
    response = client.post(
        "/pedidos",
        json={
            "cliente": "Carlos",
            "produto": "Teclado Mecânico",
            "quantidade": 1
        }
    )

    assert response.status_code == 200
    assert "id" in response.json()


def test_listar_pedidos():
    response = client.get("/pedidos")

    assert response.status_code == 200
    assert isinstance(response.json(), list)