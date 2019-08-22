from sqltables import Domen, InfoSite

from sqlalchemy import create_engine
engine = create_engine('sqlite:///sqlalchemy_example.db')

from sqlalchemy.orm import sessionmaker
session = sessionmaker()
session.configure(bind=engine)

s = session()
domens = s.query(Domen).all()
sites = s.query(InfoSite).all()
for domen in domens:
    print(domen.name_domen, [info.date_of_operation.strftime("%Y-%m-%d %H:%M") for info in domen.infos])

for site in sites:
    print(site.parent)

s.close()
