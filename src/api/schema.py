from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class Crime(BaseModel):
    id: str
    datetime: Optional[datetime]
    location: str
    crime_type: str
    name: Optional[str]

    class Config:
        orm_mode = True
