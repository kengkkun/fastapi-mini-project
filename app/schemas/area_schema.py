from pydantic import BaseModel
from uuid import UUID


class AreaBase(BaseModel):
    area_id: UUID

    class Config:
        orm_mode = True
