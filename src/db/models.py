import logging
from datetime import datetime
from sqlalchemy import Column, DateTime, Float, String, UUID

from src.db.database import Base, engine


logger = logging.getLogger(__name__)


class Crime(Base):
    __tablename__ = "crime"
    __table_args__ = {"schema": "mkultra"}

    _id = Column(UUID, primary_key=True)
    datetime = Column(DateTime, default=datetime.now())
    location = Column(String(100), nullable=True)
    crime_type = Column(String(40), nullable=True)
    name = Column(String(40), nullable=True)


class Criminal(Base):
    __tablename__ = "criminal"
    __table_args__ = {"schema": "mkultra"}

    _id = Column(UUID, primary_key=True)
    fname = Column(String(20), nullable=True)
    lname = Column(String(20), nullable=True)
    date_birth = Column(DateTime, default=datetime.now())


class Case(Base):
    __tablename__ = "case"
    __table_args__ = {"schema": "mkultra"}

    _id = Column(UUID, primary_key=True)
    crime_name = Column(String(40), nullable=True)
    status = Column(String(40), nullable=True)
    date_open = Column(DateTime, default=datetime.now())
    date_closed = Column(DateTime, default=datetime.now())
    suspects = Column(String(40), nullable=True)
    lead_detective = Column(UUID, nullable=True)
    funds_allocated = Column(Float, nullable=True)


class Detective(Base):
    __tablename__ = "detective"
    __table_args__ = {"schema": "mkultra"}

    _id = Column(UUID, primary_key=True)
    fname = Column(String(20), nullable=True)
    lname = Column(String(20), nullable=True)
    date_birth = Column(DateTime, default=datetime.now())


logger.notice("creating tables ...")
Base.metadata.create_all(engine)
