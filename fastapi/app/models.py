from .database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, text
from sqlalchemy.orm import relationship


class Car(Base):
    
    __tablename__ = 'cars'

    id = Column(Integer,primary_key=True,nullable=False)
    year = Column(Integer,nullable=False)
    model = Column(String,nullable=False)
    brand = Column(String,nullable=False)
    subsidiary_id = Column(Integer, ForeignKey('subsidiarys.id'), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
    
    subsidiary = relationship("Subsidiary", back_populates="cars")

class Subsidiary(Base):
    
    __tablename__ = 'subsidiarys'

    id = Column(Integer,primary_key=True,nullable=False)
    name = Column(String,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
    
    cars = relationship("Car", back_populates="subsidiary")

