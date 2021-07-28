from pydantic import BaseModel
import datetime as _dt
from uuid import UUID


class PriceBaseSchema(BaseModel):
    price: UUID
    job_id: UUID
    sum_price: float


class CreatePriceSchema(PriceBaseSchema):
    pass


class UpdatePriceSchema(PriceBaseSchema):
    pass


class PriceSchema(PriceBaseSchema):
    id: UUID
    date: _dt.datetime

    class Config:
        orm_mode = True
