from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

"""Initiates sqlalchemy to allow database querying"""

engine = create_engine('sqlite:///app/company.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
metadata = MetaData()
Base.query = db_session.query_property()

def init_db(db):
    from app import models
    db.metadata.create_all(bind=engine)
