from sqlalchemy import Column, String, BIGINT, Float, Integer
from src.models.sqlite.settings.base import Base

class NaturalPersonTable(Base):
   __tablename__ = 'natural_person'
   
   id = Column(BIGINT, primary_key=True)
   monthly_income = Column(Float, nullable=False)
   age = Column(Integer, nullable=False)
   name = Column(String, nullable=False)
   phone_number = Column(String, nullable=False, unique=True)
   email = Column(String,nullable=False, unique=True)
   category = Column(String)
   balance = Column(Float, nullable=False)
   
   def __repr__(self):
      return f'Natural Person [name: {self.name}, phone number: {self.phone_number}, email: {self.email} ]'