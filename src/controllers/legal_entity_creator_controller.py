from typing import Dict
import re
from src.models.sqlite.interfaces.legal_entity_repository_interface import LegalEntityRepositoryInterface

class LegalEntityCreatorController:
   def __init__(self, entity_repository: LegalEntityRepositoryInterface):
      self.__entity_repository = entity_repository
      
   def create_entity(self, entity_data: Dict) -> Dict:
      billing = entity_data.get('billing')
      age = entity_data.get('age')
      trade_name = entity_data.get('trade_name')
      phone_number = entity_data.get('phone_number')
      corporate_email = entity_data.get('corporate_email')
      category = entity_data.get('category')
      balance = entity_data.get('balance')
      
      self.__validate_billing_age_balance(billing, age, balance, phone_number)
      self.__validate_trade_name(trade_name)
      self.__validate_email(corporate_email)
      self.__insert_entity(billing, age, trade_name, phone_number, corporate_email, category, balance)
      
      return self.__format_response(entity_data)
      
   def __validate_billing_age_balance(self, billing: float, age: int, balance: float, phone_number: str):
    if billing < 0 or age < 0 or balance < 0:
        raise Exception('Billing, age and balance must be greater than 0')

    no_valid_characters_age_phone_number = re.compile(r'[^0-9]')
    no_valid_characters_billing_balance = re.compile(r'[^0-9.]')
    
    
    if (no_valid_characters_age_phone_number.search(str(age)) or 
        no_valid_characters_billing_balance.search(str(billing)) or 
        no_valid_characters_billing_balance.search(str(balance)) or 
        no_valid_characters_age_phone_number.search(phone_number)):
        raise Exception('Age, billing, balance and phone number must be numbers')

      
   def __validate_trade_name(self, trade_name: str):
      # Expressão regular para validar se o nome da empresa contém apenas letras
      non_valid_characters = re.compile(r'[^a-zA-Z ]')
      
      if non_valid_characters.search(trade_name):
         raise Exception('Trade name invalid')
      
   def __validate_email(self, email: str):
      email_regex = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
      
      if not email_regex.match(email):
         raise Exception('Email invalid')
      
   def __insert_entity(self, billing: float, age: int, trade_name: str, phone_number: str, corporate_email: str, category: str, balance: float):
      self.__entity_repository.create_entity(billing, age, trade_name, phone_number, corporate_email, category, balance)
      
   def __format_response(self, entity_data: Dict) -> Dict:
      return {
         "data": {
            "type": "Legal Entity",
            "count": 1,
            "attributes": entity_data
         }
      }      