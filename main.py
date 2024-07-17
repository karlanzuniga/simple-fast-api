from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models,crud
from app.database import engine, get_db

# Create the database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/items/")
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    items = crud.get_all_items(db=db)
    return items

@app.get("/items/{item_id}")
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_item(db=db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@app.post("/items/")
def create_item(name: str, description: str, db: Session = Depends(get_db)):
    return crud.create_item(db=db, name=name, description=description)