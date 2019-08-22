from sqltables import Domen
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import create_engine
engine = create_engine('sqlite:///sqlalchemy_example.db')

from sqlalchemy.orm import sessionmaker
session = sessionmaker()
session.configure(bind=engine)
Base.metadata.bind = engine

s = session()
domens = ['vk.com', 'youtube.com', 'ok.ru']
for domen in domens:
    do = Domen(name_domen=domen)
    s.add(Domen(name_domen=domen))

s.commit()
s.close()

