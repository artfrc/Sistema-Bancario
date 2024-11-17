from sqlalchemy import Column, String, BIGINT
from src.models.sqlite.settings.base import Base

class LegalEntityTable(Base):
   __tablename__ = 'legal_entity'
   
   id = Column(BIGINT, primary_key=True)
   billing = Column(float, nullable=False)
   age = Column(int, nullable=False)
   trade_name = Column(String, nullable=False)
   phone_number = Column(String, nullable=False, unique=True)
   corpoate_email = Column(String, nullable=False, unique=True)
   category = Column(String)
   balance = Column(float, nullable=False)
   
   def __repr__(self):
      return f'Legal Entity: Trade Name: {self.trade_name}, phone number: {self.phone_number}, email: {self.corpoate_email}'