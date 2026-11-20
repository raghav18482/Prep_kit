# Routes = HTTP layer only. Validate input, call the service, shape the response.
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.item import ItemCreate, ItemResponse, ItemUpdate
from app.services import item_service

router = APIRouter(prefix="/items", tags=["Items"])


@router.get("/", response_model=list[ItemResponse])
def list_items(db: Session = Depends(get_db)):
    return item_service.list_items(db)


@router.get("/{item_id}", response_model=ItemResponse)
def get_item(item_id: int, db: Session = Depends(get_db)):
    item = item_service.get_item(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.post("/", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
def create_item(data: ItemCreate, db: Session = Depends(get_db)):
    return item_service.create_item(db, data)


@router.put("/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, data: ItemUpdate, db: Session = Depends(get_db)):
    item = item_service.update_item(db, item_id, data)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    if not item_service.delete_item(db, item_id):
        raise HTTPException(status_code=404, detail="Item not found")
