from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from base import engine

# Создание базового класса для определения моделей
Base = declarative_base()


class Table1(Base):
    __tablename__ = "devices"
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    config_id = Column(Integer, ForeignKey("configuration.id"))
    rel = relationship("Table2", back_populates="rel")


class Table2(Base):
    __tablename__ = "configuration"
    id = Column(Integer, primary_key=True)
    description = Column(Text)
    attributes = Column(Text)
    rel = relationship("Table1", back_populates="rel")


# Создание таблиц в базе данных
Base.metadata.create_all(bind=engine)
