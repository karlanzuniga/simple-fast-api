from sqlalchemy.orm import Session
from . import models

def get_all_items(db: Session):
    return db.query(models.YourTable).all()

def get_item(db: Session, item_id: int):
    return db.query(models.YourTable).filter(models.YourTable.id == item_id).first()

def create_item(db: Session, name: str, description: str):
    db_item = models.YourTable(name=name, description=description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item