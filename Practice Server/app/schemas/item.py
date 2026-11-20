# Schemas = what the API accepts and returns (request/response validation).
from typing import Optional

from pydantic import BaseModel, ConfigDict


class ItemCreate(BaseModel):
    name: str
    price: float
    description: Optional[str] = None


class ItemUpdate(ItemCreate):
    pass


class ItemResponse(ItemCreate):
    id: int

    # Lets Pydantic read data straight from SQLAlchemy objects.
    model_config = ConfigDict(from_attributes=True)
