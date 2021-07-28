from pydantic import BaseModel
from uuid import UUID


class CarrierBase(BaseModel):
    carrier_party: str


class CarrierSchema(CarrierBase):
    id: UUID

    class Config:
        orm_mode = True
