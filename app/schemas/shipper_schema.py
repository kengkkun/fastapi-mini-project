from pydantic import BaseModel
from uuid import UUID


class ShipperBase(BaseModel):
    shipper_id: UUID

    class Config:
        orm_mode = True
