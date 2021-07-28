from pydantic import BaseModel


class PriceTruckLoadBaseSchema(BaseModel):
    price_fixed_cost: float
    price_variable_distance: float
    price_additional_stop: float
    price_return_document: float
    price_additional_staff: float
    price_round_trip_discount: float

    class Config:
        orm_mode = True
