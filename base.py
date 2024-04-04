from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import yaml


with open("connection.yaml", 'r') as file:
    cfg = yaml.safe_load(file)

SQLALCHEMY_DATABASE_URL = f"postgresql://{cfg['user']}:{cfg['password']}@{cfg['host']}:{cfg['port']}/postgres"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
