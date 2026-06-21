from pydantic import BaseModel, Field


class PedidoCreate(BaseModel):
    cliente: str = Field(..., min_length=1)
    produto: str = Field(..., min_length=1)
    quantidade: int = Field(..., gt=0)


class PedidoResponse(BaseModel):
    id: str
    cliente: str
    produto: str
    quantidade: int
    status: str