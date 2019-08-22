#!/usr/bin/env python3
from sqltables import InfoSite, Domen
from domenrequest import parse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#import schedule
#import time

class Explorer(object):

    def __init__(self, last_id=0, check_twice=False):
        self.last_id = last_id
        self.check_twice = check_twice

    def job(self):
        engine = create_engine('sqlite:///sqlalchemy_example.db')
        session = sessionmaker()
        session.configure(bind=engine)
        s = session()
        if self.check_twice:
            domens = s.query(Domen).all()
        else:
            domens = s.query(Domen).filter(Domen.id>self.last_id).all()

        if domens:
            self.last_id = max([domen.id for domen in domens])
        

        for domen in domens:
            parsed = parse(domen.name_domen)
            infosite = InfoSite(url=parsed[0], title=parsed[1], description=parsed[2], keywords=parsed[3], parent=domen)
            s.add(infosite)
            
        s.commit()
        s.close()


'''
schedule.every().day.do(Explorer.job)
while 1:
    schedule.run_pending()
    time.sleep(1)
'''
if __name__ == "__main__":
    with open('config', 'r') as f:
        last_id = int(f.readline())
    print(last_id)
    e = Explorer(last_id=last_id)#, check_twice=True)
    e.job()
    with open('config', 'w') as f:
        f.write(str(e.last_id))
