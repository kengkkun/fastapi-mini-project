from sqlalchemy import  Column, Float, ForeignKey, DateTime, func, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from configs.db import Base


class Pricing(Base):
    __tablename__ = 'pricing'
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)
    price = Column(UUID(as_uuid=True), ForeignKey('price.id', ondelete="CASCADE"))
    job_id = Column(UUID(as_uuid=True), default=uuid4)
    date = Column(DateTime, default=func.now())
    sum_price = Column(Float)

    pricing = relationship('Price', back_populates="prices")


class Price(Base):
    __tablename__ = 'price'
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)
    origin_area_uid = Column(UUID(as_uuid=True), ForeignKey('area.id', ondelete="CASCADE"))
    destination_area_uid = Column(UUID(as_uuid=True), ForeignKey('area.id', ondelete="CASCADE"))
    carrier_uid = Column(UUID(as_uuid=True), ForeignKey('carrier.id', ondelete="CASCADE"))
    shipper_uid = Column(UUID(as_uuid=True), ForeignKey('shipper.id', ondelete="CASCADE"))
    vehicle_type_uid = Column(UUID(as_uuid=True), ForeignKey('vehicle_type.id', ondelete="CASCADE"))

    prices = relationship("Pricing", back_populates="pricing")


class Carrier(Base):
    __tablename__ = 'carrier'
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)
    carrier_party = Column(String(50), unique=True, index=True)


class Shipper(Base):
    __tablename__ = 'shipper'
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)


class VehicleType(Base):
    __tablename__ = 'vehicle_type'
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)


class Area(Base):
    __tablename__ = 'area'
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)


class PriceItem(Price):
    __mapper_args__ = {'polymorphic_identity': 'price_item'}
    const_sum_whd = Column(Float)
    const_weight = Column(Float)
    const_volumn = Column(Float)
    price = Column(Float)


class PriceTruckLoad(PriceItem):
    __mapper_args__ = {'polymorphic_identity': 'price_truck_load'}
    price_fixed_cost = Column(Float)
    price_variable_distance = Column(Float)
    price_additional_stop = Column(Float)
    price_return_document = Column(Float)
    price_additional_staff = Column(Float)
    price_round_trip_discount = Column(Float)
