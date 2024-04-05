import json
import yaml

from sqlalchemy.sql import text
from sqlalchemy.orm import Query
from sqlalchemy import func

from model import table_dict, Table1

from base import SessionLocal


def make_filter(file):
    filt = ""
    for i in file:
        filt += str(i) + " = " + f"'{file[i]}'" + " and "
    filt = filt[:-5]
    return filt


def notexist(session, id):
    if id > Query(func.max(Table1.id),session=session):
        return True
    return False


def get_table():
    db = SessionLocal()
    return db.query(Table1).all()


def set_device(file):
    db = SessionLocal()
    file = file.decode('utf-8')
    json_data = json.loads(file)
    file = yaml.dump(data=json_data)
    file = yaml.safe_load(file)
    if notexist(db, file):
        db.add(**{"name":file["name"],"attributes":str(file["attributes"])})
    db.commit()
    return True


def del_item(file):
    db = SessionLocal()
    file = file.decode('utf-8')
    json_data = json.loads(file)
    file = yaml.dump(data=json_data)
    file = yaml.safe_load(file)
    table = table_dict["peripherals"]
    filt = make_filter(file)
    db.query(table).filter(text(filt)).delete()
    db.commit()
    return True
