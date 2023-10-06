from sqlalchemy import Boolean, Column, Integer, Identity, Text
from sqlalchemy.orm import relationship
import base

class Table1(base.Base):
    __tablename__ = "peripherals"

    id = Column(Integer,Identity(start=1), primary_key=True)
    name = Column(Text)
    attribute_name = Column(Text)


class Table2(base.Base):
    __tablename__ = "attributes"

    attribute_name = Column(Text, primary_key= True)
    var_type = Column(Text)
    up_limit = Column(Text)
    down_limit = Column(Text)
    context = Column(Text)
    alterability = Column(Text)

table_dict = {"peripherals":Table1, "attributes":Table2}