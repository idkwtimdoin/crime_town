from datetime import datetime
from sqlalchemy import Column, DateTime, Float, Integer, String

from src.db.database import Base


class Crime(Base):
    _id = Column(String, primary_key=True)


class Criminal(Base):
    _id = Column(String, primary_key=True)


class Case(Base):
    _id = Column(String, primary_key=True)


class Detective(Base):
    _id = Column(String, primary_key=True)
