from sqlalchemy import create_engine, Column, Float, ForeignKey, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4

Base = declarative_base()


class Pricing(Base):
    __tablename__ = 'pricing'
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)
    price = Column(UUID(as_uuid=True), ForeignKey('price.id'))
    job_id = Column(UUID(as_uuid=True), default=uuid4)
    date = Column(DateTime, default=func.now())
    sum_price = Column(Float)

    pricing = relationship('Price', back_populates="prices")


class Price(Base):
    __tablename__ = 'price'
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)
    origin_area_uid = Column(UUID(as_uuid=True), ForeignKey('area.id'))
    destination_area_uid = Column(UUID(as_uuid=True), ForeignKey('area.id'))
    carrier_uid = Column(UUID(as_uuid=True), ForeignKey('carrier.id'))
    shipper_uid = Column(UUID(as_uuid=True), ForeignKey('shipper.id'))
    vehicle_type_uid = Column(UUID(as_uuid=True), ForeignKey('vehicle_type.id'))

    prices = relationship("Pricing", back_populates="pricing")


class Carrier(Base):
    __tablename__ = 'carrier'
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)
    carrier_party = Column(UUID(as_uuid=True))


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


class PriceTruckLoad(Price):
    __mapper_args__ = {'polymorphic_identity': 'price_truck_load'}
    price_fixed_cost = Column(Float)
    price_variable_distance = Column(Float)
    price_additional_stop = Column(Float)
    price_return_document = Column(Float)
    price_additional_staff = Column(Float)
    price_round_trip_discount = Column(Float)


engine = create_engine('postgresql://postgres:1234@localhost:5432/mini_project')
Base.metadata.drop_all(bind=engine)
# Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

session = Session()
session.close()


