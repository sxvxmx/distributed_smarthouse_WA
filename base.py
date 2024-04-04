from sqlalchemy import create_engine
from sqlalchemy import Boolean, Column, Integer, Identity, Text, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from config import user, password, host, port

SQLALCHEMY_DATABASE_URL = f"postgresql://{user}:{password}@{host}:{port}/postgres"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Создание базового класса для определения моделей
Base = declarative_base()


class Table1(Base):
    __tablename__ = "peripherals"
    id = Column(Integer)
    uni_id = Column(Integer, Identity(start=1), primary_key=True)
    name = Column(Text)
    attribute_name = Column(Text, ForeignKey("attributes.name"))
    attribute_rel = relationship("Table2")


class Table2(Base):
    __tablename__ = "attributes"
    name = Column(Text, primary_key=True)
    variable = Column(Boolean)
    var_type = Column(Text)
    upper_limit = Column(Text)
    lower_limit = Column(Text)
    is_input = Column(Boolean)
    is_output = Column(Boolean)


# Создание таблицы в базе данных
Base.metadata.create_all(bind=engine)

table_dict = {"peripherals": Table1, "attributes": Table2}
