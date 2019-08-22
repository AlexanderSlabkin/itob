from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime

Base = declarative_base()

class InfoSite(Base):
    __tablename__ = 'infosite'
    id = Column(Integer, primary_key=True)
    url = Column(String(250), nullable=False)
    title = Column(String(250), index=True)
    description = Column(String(250))
    keywords = Column(String(250))
    date_of_operation = Column(DateTime, index=True, default=datetime.utcnow)
    domen_id = Column(Integer, ForeignKey('domen.id'))

    def __repr__(self):
        return '<InfoSite {}>'.format(self.url)

class Domen(Base):
    __tablename__ = 'domen'
    id = Column(Integer, primary_key=True)
    name_domen = Column(String(100), index=True)
    infos = relationship('InfoSite', backref='parent')


    def __repr__(self):
        return '<Domen {}>'.format(self.name_domen)


engine = create_engine('sqlite:///sqlalchemy_example.db')    
session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)
