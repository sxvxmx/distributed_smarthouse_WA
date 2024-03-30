from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#connect to database
user = "postgres"
password = "1111"
host = "localhost"
port = "5432"

SQLALCHEMY_DATABASE_URL = f"postgresql://{user}:{password}@{host}:{port}/postgres"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()