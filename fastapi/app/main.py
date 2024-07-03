from fastapi import FastAPI, Depends, HTTPException, Query, status
from typing import List, Optional
from sqlalchemy.orm import Session
from .models import Car, Subsidiary
from . import schemas
from .database import get_db

app = FastAPI()

@app.get('/')
def get_cars(db: Session = Depends(get_db),skip:int=0,limit:int=100):
    """
    Retrieve all cars.

    Parameters:
    - db: Database session dependency.
    - skip: Number of records to skip. Default is 0.
    - limit: Maximum number of records to return. Default is 100.

    Returns:
    - List of all cars in the database.
    """
    cars = db.query(Car).offset(skip).limit(limit).all()
    print(cars)
    return cars

@app.get('/cars', response_model=List[schemas.CarBase])
def get_cars(brand: Optional[str] = Query(None), 
             subsidiaryName: Optional[str] = Query(None),
             db: Session = Depends(get_db),
             skip: int = 0, limit: int = 100):
    query = db.query(Car)
    
    """
    Retrieve cars with optional filtering by brand and subsidiary name.

    Parameters:
    - brand: Optional filter by car brand.
    - subsidiaryName: Optional filter by subsidiary name.
    - db: Database session dependency.
    - skip: Number of records to skip. Default is 0.
    - limit: Maximum number of records to return. Default is 100.

    Returns:
    - List of cars that match the filtering criteria.
    """
    
    if brand:
        query = query.filter(Car.brand == brand)
    
    if subsidiaryName:
        query = query.join(Subsidiary).filter(Subsidiary.name == subsidiaryName)
    
    cars = query.offset(skip).limit(limit).all()
    return cars

@app.post('/cars', response_model=schemas.CarBase, status_code=status.HTTP_201_CREATED)
def create_car(car: schemas.CreateCar, db: Session = Depends(get_db)):
    """
    Create a new car record.

    Parameters:
    - car: Car data to create a new record.
    - db: Database session dependency.

    Returns:
    - The newly created car record.
    """
    db_car = Car(**car.dict())
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car

@app.post('/subsidiarys', response_model=schemas.SubsidiaryBase, status_code=status.HTTP_201_CREATED)
def create_subsidiary(subsidiary: schemas.CreateSubsidiary, db: Session = Depends(get_db)):
    """
    Create a new subsidiary record.

    Parameters:
    - subsidiary: Subsidiary data to create a new record.
    - db: Database session dependency.

    Returns:
    - The newly created subsidiary record.
    """
    db_subsidiary = Subsidiary(**subsidiary.dict())
    db.add(db_subsidiary)
    db.commit()
    db.refresh(db_subsidiary)
    return db_subsidiary
