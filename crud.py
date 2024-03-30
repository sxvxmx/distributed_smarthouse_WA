from sqlalchemy.orm import Session
from sqlalchemy import insert
import yaml
from sqlalchemy.sql import text
from sqlalchemy.orm import Query
import model
from model import Table1, Table2
import json

def make_filter(file):
    filt = ""
    for i in file:
        filt += str(i) + " = " + f"'{file[i]}'" + " and "
    filt = filt[:-5]
    return filt

def unmap_join(mapper:list[tuple]):
    out = []
    for i in mapper:
        sub = {}
        for o in i:
            sub = sub|o.__dict__
        out.append(sub)
    return out

def notexist(table, session, feature):
    q = Query(table,session=session).all()
    t = True
    for o in q:
        if(feature in o):
            t = False
    return t


def get_table(db: Session, table_name):
    table = model.table_dict[table_name]
    return db.query(table).all()

def get_all(db: Session):
    tables = list(model.table_dict.values())
    qr = Query(tables,session=db).filter(Table1.attribute_name == Table2.name).all()
    return unmap_join(qr)

def get_var(db: Session):
    tables = list(model.table_dict.values())
    qr = Query(tables,session=db).filter(Table1.attribute_name == Table2.name).filter(Table2.variable == True).all()
    return unmap_join(qr)

def set_item(db: Session, table_name, file):
    #unteseted
    file = file.decode('utf-8')
    json_data = json.loads(file)
    file = yaml.dump(data = json_data)
    file = yaml.safe_load(file)
    table = model.table_dict[table_name]
    db.add(table(**file))
    db.commit()
    return True

def set_device(db: Session, file):
    file = file.decode('utf-8')
    json_data = json.loads(file)
    file = yaml.dump(data = json_data)
    file = yaml.safe_load(file)
    for i in file["attributes"]:
        table = model.table_dict["attributes"]
        if(notexist(table.name,db,i["name"])):
            db.add(table(**i))
        table = model.table_dict["peripherals"]
        if(notexist(table.id,db,file["id"])):
            db.add(table(**{"id":file["id"],"name":file["name"],"attribute_name":i["name"]}))
    db.commit()
    return True
        

def del_item(db: Session, table_name, file):
    #unteseted
    file = file.decode('utf-8')
    json_data = json.loads(file)
    file = yaml.dump(data = json_data)
    file = yaml.safe_load(file)
    table = model.table_dict[table_name]

    filt = make_filter(file)
    db.query(table).filter(text(filt)).delete()
    db.commit()
    return True
