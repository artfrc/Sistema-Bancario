import pytest
from .legal_entity_creator_controller import LegalEntityCreatorController

class MockLegalEntityRepository:
   def create_entity(self, billing: float, age: int, trade_name: str, phone_number: str, corporate_email: str, category: str, balance: float):
      pass

def test_create_entity():
      entity_data = {
         'billing': 10000.0,
         'age': 18,
         'trade_name': 'Company Test Create',
         'phone_number': '123456789',
         'corporate_email': 'companytestcreate@contact.com',
         'category': 'Technology',
         'balance': 10000.0
      }
      
      controller = LegalEntityCreatorController(MockLegalEntityRepository())
      response =  controller.create_entity(entity_data)
      
      assert response["data"]["type"] == "Legal Entity"
      assert response["data"]["count"] == 1
      assert response["data"]["attributes"] == entity_data
      
def test_create_entity_error():
      entity_data = {
         'billing': 10000.0,
         'age': 18,
         'trade_name': 'Company Test Create',
         'phone_number': '123456789',
         'corporate_email': 'companytestcreate', # Email inválido
         'category': 'Technology',
         'balance': 10000.0
      }
      
      controller = LegalEntityCreatorController(MockLegalEntityRepository())
      
      with pytest.raises(Exception):
         controller.create_entity(entity_data)     