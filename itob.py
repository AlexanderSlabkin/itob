from sqltables import InfoSite, Domen
from domenrequest import parse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#import schedule
#import time
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

def job():
    engine = create_engine('sqlite:///sqlalchemy_example.db')
    session = sessionmaker()
    session.configure(bind=engine)
    Base.metadata.bind = engine
    s = session()
    domens = s.query(Domen).all()
    for domen in domens:
        parsed = parse(domen.name_domen)
        infosite = InfoSite(url=parsed[0], title=parsed[1], description=parsed[2], keywords=parsed[3])
        s.add(infosite)
        
    s.commit()
    sites = s.query(InfoSite).all()
    for site in sites:
        print(site)
        print(site.url, site.title, site.description, site.keywords, site.date_of_operation)


'''
schedule.every().day.do(job)
while 1:
    schedule.run_pending()
    time.sleep(1)
'''
if __name__ == "__main__":
    job()
