from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.daclarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

class InfoSite(Base):
    id = Column(Integer, primary_key=True)
    url = Column(String(250), nullable=False)
    title = Column(String(250))
    description = Column(String(250))
    keywords = Column(String(250))
    date_of_operation = Column(DateTime, index=True, default=datetime.utcnow)

    
