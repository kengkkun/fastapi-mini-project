from typing import List
from fastapi import APIRouter, Depends, Response, status, HTTPException
from schemas.price_schema import CreatePriceSchema, PriceSchema, UpdatePriceSchema
from sqlalchemy.orm import Session

from schemas.carrier_schema import CarrierBase, CarrierSchema
from models.carrier_model import Carrier, VehicleType, Area, Shipper, PriceTruckLoad, Pricing, Price
from services import price_truck_load_service, price_item_service
from uuid import UUID

from configs.deps import get_db
import random

carrier_router = APIRouter()


@carrier_router.get('/carrier', response_model=List[PriceSchema], status_code=status.HTTP_200_OK)
def get_list(db: Session = Depends(get_db)):
    price = db.query(Pricing).all()
    return price


@carrier_router.post('/carrier', response_model=CarrierSchema, status_code=status.HTTP_201_CREATED)
def create_list(carrier: CarrierBase, db: Session = Depends(get_db)):
    carrier_type = Carrier(carrier_party=carrier.carrier_party)
    vehicle = VehicleType()
    area = Area()
    shipper = Shipper()

    db.add(carrier_type)
    db.add(vehicle)
    db.add(area)
    db.add(shipper)
    db.commit()
    db.refresh(carrier_type)
    db.refresh(vehicle)
    db.refresh(area)
    db.refresh(shipper)

    price_truck_load = price_truck_load_service.PriceTruckLoad(variable_distance=random.random() * 100,
                                                               round_trip_discount=random.random())
    price_item = price_item_service.PriceItem(sum_whd=random.random(), weight=random.random() * 10,
                                              volumn=random.randint(1, 10))
    const_volumn = price_item.volumn
    const_weight = price_item.weight
    const_sum_whd = price_item.sum_whd
    price = price_item.get_price()
    price_variable_distance = price_truck_load.variable_distance
    price_return_document = price_truck_load.get_document()
    price_additional_stop = price_truck_load.additional_stop
    price_additional_staff = price_truck_load.additional_staff
    price_fixed_cost = price_truck_load.fixed_cost
    price_round_trip_discount = price_truck_load.round_trip_discount

    price_truck_load = PriceTruckLoad(origin_area_uid=area.id,
                                      destination_area_uid=area.id,
                                      carrier_uid=carrier_type.id,
                                      shipper_uid=shipper.id,
                                      vehicle_type_uid=vehicle.id,
                                      const_volumn=const_volumn,
                                      const_weight=const_weight,
                                      const_sum_whd=const_sum_whd,
                                      price=price,
                                      price_variable_distance=price_variable_distance,
                                      price_return_document=price_return_document,
                                      price_additional_stop=price_additional_stop,
                                      price_additional_staff=price_additional_staff,
                                      price_fixed_cost=price_fixed_cost,
                                      price_round_trip_discount=price_round_trip_discount
                                      )
    db.add(price_truck_load)
    db.commit()
    db.refresh(price_truck_load)

    pricing = Pricing(price=price_truck_load.id,
                      sum_price=price)

    db.add(pricing)
    db.commit()
    db.refresh(pricing)

    return carrier_type


# @carrier_router.put('/carrier/{carrier_id}', response_model=PriceSchema, status_code=status.HTTP_200_OK)
# def update_list(price_id: int, items: UpdatePriceSchema, db: Session = Depends(get_db)):
#     item_to_update = db.query(Pricing).filter(Pricing.id == price_id).first()
#     item_to_update.sum_price = items.sum_price
#     item_to_update.price = items.price
#     item_to_update.job_id = items.job_id
#
#     db.commit()
#
#     return item_to_update


@carrier_router.delete('/carrier/{carrier_id}')
def delete_list(carrier_id : UUID, db: Session = Depends(get_db)):
    item_to_delete = db.query(Pricing).filter(Pricing.id == carrier_id).first()
    # price = db.query().filter(Price.id == price_id).first()

    if item_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource Not Found")

    db.delete(item_to_delete)
    db.commit()

    return item_to_delete
