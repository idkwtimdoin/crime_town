from datetime import datetime
from sqlalchemy import Column, DateTime, Float, Integer, String

from src.db.database import Base


class Crime(Base):
    _id = Column(String, primary_key=True)
    # TODO add rest


class Criminal(Base):
    _id = Column(String, primary_key=True)
    # TODO add rest


class Case(Base):
    _id = Column(String, primary_key=True)
    # TODO add rest


class Detective(Base):
    _id = Column(String, primary_key=True)
    # TODO add rest
