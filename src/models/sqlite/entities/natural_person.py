from sqlalchemy import Column, String, BIGINT
from src.models.sqlite.settings.base import Base

class NaturalPerson(Base):
   __tablename__ = 'natural_person'
   
   id = Column(BIGINT, primary_key=True)
   monthly_income = Column(float)
   age = Column(int)
   name = Column(String)
   phone_number = Column(String)
   email = Column(String)
   category = Column(String)
   balance = Column(float)
   
   def __repr__(self):
      return f'Natural Person: name: {self.name}, phone number: {self.phone_number}, email: {self.email}'