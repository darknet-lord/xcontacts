from sqlalchemy import Column, String, JSON
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Contact(Base):
    __tablename__ = "contacts"

    contact_id = Column(String, primary_key=True)
    name = Column(String(length=255), nullable=False)
    phone = Column(String(length=255), nullable=True)
    email = Column(String(length=255), nullable=True)
    info = Column(JSON(), nullable=True)
    photo_id = Column(String(255), nullable=True)
