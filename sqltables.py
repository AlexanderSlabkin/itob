from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime
import os

Base = declarative_base()

class InfoSite(Base):
    __tablename__ = 'infosite'
    id = Column(Integer, primary_key=True)
    url = Column(String(250), nullable=False)
    domen = relationship("Domen", uselist=False, back_populates="infosite")
    title = Column(String(250), index=True)
    description = Column(String(250))
    keywords = Column(String(250))
    date_of_operation = Column(DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<InfoSite {}>'.format(self.url)

class Domen(Base):
    __tablename__ = 'domen'
    id = Column(Integer, primary_key=True)
    name_domen = Column(String(100), index=True)
    infosite_id = Column(Integer, ForeignKey('infosite.id'))
    infosite = relationship("InfoSite", back_populates="domen")

    def __repr__(self):
        return '<Domen {}>'.format(self.name_domen)

engine = create_engine('sqlite:///sqlalchemy_example.db')    
session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)
