from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
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

    
