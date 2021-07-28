from pydantic import BaseModel


class PriceInterfaceBaseSchema(BaseModel):
    id: int
    origin_area_uid: str
    destination_area_uid: str
    carrier_uid: str
    shipper_uid: str
    vehicle_type_uid: str

    class Config:
        orm_mode = True
