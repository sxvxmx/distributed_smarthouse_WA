from sqlalchemy import Boolean, Column, Integer, Identity, Text, ForeignKey
from sqlalchemy.orm import relationship
import base

class Table1(base.Base):
    __tablename__ = "peripherals"
    id = Column(Integer)
    uni_id = Column(Integer,Identity(start=1), primary_key=True)
    name = Column(Text)
    attribute_name = Column(Text, ForeignKey("attributes.name"))
    attribute_rel = relationship("Table2")


class Table2(base.Base):
    __tablename__ = "attributes"

    name = Column(Text, primary_key = True)
    variable = Column(Boolean)
    var_type = Column(Text)
    upper_limit = Column(Text)
    lower_limit = Column(Text)
    is_input = Column(Boolean)
    is_output = Column(Boolean)

table_dict = {"peripherals":Table1, "attributes":Table2}

#database creation by table templates
for i in table_dict:
    (table_dict[i].metadata).create_all(base.engine)

