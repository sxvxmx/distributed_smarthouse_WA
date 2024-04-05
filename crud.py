import json

from sqlalchemy.sql import text
from sqlalchemy.orm import Query
from sqlalchemy.orm import Session

from model import Table1, Table2
from base import SessionLocal

from functools import wraps


def db_operation(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        db: Session = SessionLocal()

        try:
            success = func(db, *args, **kwargs)
            return success

        except Exception as e:
            print(f"Exception: {e}")
            db.rollback()
            return False

        finally:
            db.close()

    return wrapper


@db_operation
def set_entity(db, file, entity_class):
    data = json.loads(file)
    uid = data.get("id")
    entity_is_existing = db.query(entity_class).filter(entity_class.id == uid).first()

    if entity_is_existing:
        return False

    entity = entity_class(**data)
    db.add(entity)
    db.commit()
    return True


def set_device(file):
    return set_entity(file, Table1)


def set_config(file):
    return set_entity(file, Table2)


def get_table(table_name):
    db: Session = SessionLocal()
    if Table1.__tablename__ == table_name:
        table = Table1
    elif Table2.__tablename__ == table_name:
        table = Table2
    else:
        return False
    return db.query(table).all()


def get_all():
    db: Session = SessionLocal()
    return True


def get_var():
    db: Session = SessionLocal()
    return True


def set_item(table_name, file):
    db: Session = SessionLocal()
    return True


def del_item(table_name, file):
    db: Session = SessionLocal()
    return True
