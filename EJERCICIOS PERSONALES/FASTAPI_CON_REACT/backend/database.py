from sqlalchemy import crete_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

URL_CONNECTION = 'mysql+pymysql://root:1234@localhost/test'

engine = create_engine(URL_CONNECTION)
localSeccion = sessionmaker(autoflush=False,autocommit=False,bind=engine)