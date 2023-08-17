import logging
from typing import List
from sqlalchemy.orm import Session

from src.db.models import Crime

logger = logging.getLogger(__name__)


def fetch_crimes(db: Session, limit: int, offset: int) -> List[Crime]:
    return db.query(
        Crime.id,
        Crime.datetime,
        Crime.location,
        Crime.crime_type,
        Crime.name
    ).limit(limit).offset(offset).all()
