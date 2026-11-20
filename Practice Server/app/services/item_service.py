# Services = business logic. Routes call these; these talk to the DB.
from typing import Optional

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.item import Item
from app.schemas.item import ItemCreate, ItemUpdate


def list_items(db: Session) -> list[Item]:
    return list(db.scalars(select(Item).order_by(Item.id)))


def get_item(db: Session, item_id: int) -> Optional[Item]:
    return db.get(Item, item_id)


def create_item(db: Session, data: ItemCreate) -> Item:
    item = Item(**data.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)  # loads the id Postgres generated
    return item


def update_item(db: Session, item_id: int, data: ItemUpdate) -> Optional[Item]:
    item = db.get(Item, item_id)
    if not item:
        return None
    for field, value in data.model_dump().items():
        setattr(item, field, value)
    db.commit()
    db.refresh(item)
    return item


def delete_item(db: Session, item_id: int) -> bool:
    item = db.get(Item, item_id)
    if not item:
        return False
    db.delete(item)
    db.commit()
    return True
