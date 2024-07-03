from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class SubsidiaryBase(BaseModel):
    id: int
    name: str
    created_at: Optional[datetime]
    
    class Config:
        orm_mode = True

class CreateSubsidiary(BaseModel):
    name: str
    
    class Config:
        orm_mode = True

class CarBase(BaseModel):
    id: int
    year: int
    model: str
    brand: str
    created_at: Optional[datetime]
    subsidiary: SubsidiaryBase

    class Config:
        orm_mode = True

class CreateCar(BaseModel):
    year: int
    model: str
    brand: str
    subsidiary_id: int

    class Config:
        orm_mode = True
