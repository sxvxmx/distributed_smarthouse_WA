from sqlalchemy.orm import Session
from sqlalchemy import insert
import yaml
from sqlalchemy.sql import text
import base, model

def make_filt(file):
    filt = ""
    for i in file:
        filt += str(i) + " = " + f"'{file[i]}'" + " and "
    filt = filt[:-5]
    return filt

def get_table(db: Session, base_name):
    table = model.table_dict[base_name]
    return db.query(table).all()

#untested ))
def get_all(db: Session):
    tables = list(model.table_dict.values())
    return db.query(*tables).all()

def set_item(db: Session, base_name, file):
    #unteseted
    file = yaml.dump(file)
    table = model.table_dict[base_name]
    db.add(table(**file))
    db.commit()
    return True

def del_item(db: Session, base_name, file):
    #unteseted
    file = yaml.dump(file)
    table = model.table_dict[base_name]

    filt = make_filt(file)
    db.query(table).filter(text(filt)).delete()
    db.commit()
    return True
