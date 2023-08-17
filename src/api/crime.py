import logging
from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src import api_config
from src.api import schema
from src.db import crud
from src.db.database import get_db

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/crimes", response_model=List[schema.Crime])
def get_crimes(
    db: Session = Depends(get_db),
    limit: int = api_config.query.limit,
    offset: int = 0,
):
    return crud.fetch_crimes(db, limit=limit, offset=offset)
