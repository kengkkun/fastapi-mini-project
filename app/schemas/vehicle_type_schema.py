from pydantic import BaseModel
from uuid import UUID


class VehicleTypeBase(BaseModel):
    vehicle_type_id: UUID

    class Config:
        orm_mode = True
