from sqltables import InfoSite, Domen
from domenrequest import parse
import schedule
import time

def job():
    session = sessionmaker()
    session.configure(bind=engine)
    domens = session.query(Domen).all()
    for domen in domens:
        parsed = parse(domen)
        infosite = InfoSite(url=parsed[0], title=parsed[1], description=parsed[2], keywords=parsed[3])
        session.add(infosite)
        session.commit()
        
    session.add(infosite)
    session.commit()
    



schedule.every().day.do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)
