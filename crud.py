import json
import yaml

from sqlalchemy.sql import text
from sqlalchemy.orm import Query
from sqlalchemy import func

from model import Table1

from base import SessionLocal

def notexist(session, dev_id):
    print(Query(func.max(Table1.id),session=session).first())
    val = Query(func.max(Table1.id),session=session).first()[0]
    if val == None:
        return True
    if dev_id > val:
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
    if notexist(db, file["id"]):
        db.add(Table1(**{"id":file["id"],"name":file["name"],"attributes":str(file["attributes"])}))
    db.commit()
    return True


def del_item(num):
    db = SessionLocal()
    db.query(Table1).filter(Table1.id == int(num)).delete()
    db.commit()
    return True
