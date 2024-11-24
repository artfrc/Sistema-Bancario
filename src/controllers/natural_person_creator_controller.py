from typing import Dict
import re
from src.models.sqlite.interfaces.natural_person_repository_interface import NaturalPersonRepositoryInterface

class NaturalPersonCreatorController:
   def __init__(self, entity_repository: NaturalPersonRepositoryInterface):
      self.__entity_repository = entity_repository
      
   def create_entity(self, entity_data: Dict) -> Dict:
      monthly_income = entity_data.get('monthly_income')
      age = entity_data.get('age')
      name = entity_data.get('name')
      phone_number = entity_data.get('phone_number')
      email = entity_data.get('email')
      category = entity_data.get('category')
      balance = entity_data.get('balance')
      
      self.__validate_monthly_income_age_phone_number_balance(monthly_income, age, balance, phone_number)
      self.__validate_name(name)
      self.__validate_email(email)
      self.__insert_entity(monthly_income, age, name, phone_number, email, category, balance)
      
      return self.__format_response(entity_data)
      
      
   def __validate_monthly_income_age_phone_number_balance(self, monthly_income: float, age: int, balance: float, phone_number: str):
      if monthly_income < 0 or age < 0 or balance < 0:
         raise Exception('Monthly income, age and balance must be greater than 0')
      
      no_valid_characters_only_numbers = re.compile(r'[^0-9]')
      no_valid_characters_only_numbers_and_dot = re.compile(r'[^0-9.]')
      
      if (
            no_valid_characters_only_numbers.search(phone_number) or no_valid_characters_only_numbers.search(str(age)) or no_valid_characters_only_numbers_and_dot.search(str(monthly_income)) or 
            no_valid_characters_only_numbers_and_dot.search(str(balance))
      ):
         raise Exception('Age, monthly income, balance and phone number must be numbers')
      
   def __validate_name(self, name: str):
      # Expressão regular para validar se o nome da empresa contém apenas letras
      non_valid_characters = re.compile(r'[^a-zA-Z ]')
      
      if non_valid_characters.search(name):
         raise Exception('Name invalid')
      
   def __validate_email(self, email: str):
      email_regex = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
      
      if not email_regex.match(email):
         raise Exception('Email invalid')
      
   def __insert_entity(self, monthly_income: float, age: int, name: str, phone_number: str, email: str, category: str, balance: float):
      self.__entity_repository.create_natural_person(monthly_income, age, name, phone_number, email, category, balance)
      
   def __format_response(self, entity_data: Dict) -> Dict:
      return {
         "data": {
            "type": "Natural Entity",
            "count": 1,
            "attributes": entity_data
         }
      }