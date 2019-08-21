from sqltables import InfoSite
from domenrequest import parse
import schedule
import time

def job():

    parsed = parse('domen.com')
    infosite = InfoSite(url = parsed[0])
    session.add(infosite)
    session.commit()
    



schedule.every().day.do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)
