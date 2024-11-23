from sqlalchemy import Column, String, BIGINT, Float, Integer
from src.models.sqlite.settings.base import Base

class LegalEntityTable(Base):
    __tablename__ = 'legal_entity'

    id = Column(BIGINT, primary_key=True)
    billing = Column(Float, nullable=False)  
    age = Column(Integer, nullable=False)    
    trade_name = Column(String, nullable=False)
    phone_number = Column(String, nullable=False, unique=True)
    corporate_email = Column(String, nullable=False, unique=True)  
    category = Column(String)
    balance = Column(Float, nullable=False)  

    def __repr__(self):
        return f'Legal Entity [ Trade Name: {self.trade_name}, phone number: {self.phone_number}, email: {self.corporate_email}, ]'
