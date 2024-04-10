from sqlalchemy import Boolean, Column, Integer, Identity, Text, ForeignKey
# from sqlalchemy.orm import relationship

from base import Base, engine

class Table1(Base):
    __tablename__ = "peripherals"
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    attributes = Column(Text)
    # attribute_name = Column(Text, ForeignKey("attributes.name"))
    # attribute_rel = relationship("Table2")


# class Table2(Base):
#     __tablename__ = "attributes"
#     name = Column(Text, primary_key=True)
#     variable = Column(Boolean)
#     var_type = Column(Text)
#     upper_limit = Column(Text)
#     lower_limit = Column(Text)
#     is_input = Column(Boolean)
#     is_output = Column(Boolean)


# Создание таблиц в базе данных
Base.metadata.create_all(bind=engine)

table_dict = {"peripherals": Table1}
