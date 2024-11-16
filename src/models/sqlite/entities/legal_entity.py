from sqlalchemy import Column, String, BIGINT
from src.models.sqlite.settings.base import Base

class LegalEntity(Base):
   __tablename__ = 'legal_entity'
   
   id = Column(BIGINT, primary_key=True)
   billing = Column(float)
   age = Column(int)
   trade_name = Column(String)
   phone_number = Column(String)
   corpoate_email = Column(String)
   category = Column(String)
   balance = Column(float)
   
   def __repr__(self):
      return f'Legal Entity: Trade Name: {self.trade_name}, phone number: {self.phone_number}, email: {self.corpoate_email}'