import pytest
from .natural_person_creator_controller import NaturalPersonCreatorController

class MockNaturalPersonRepository:
   def create_natural_person(self, monthly_income: float, age: int, name: str, phone_number: str, email: str, category: str, balance: float):
      pass
   
def test_create_entity():
   entity_data = {
      'monthly_income': 10000.0,
      'age': 18,
      'name': 'Natural Test Create',
      'phone_number': '123456789',
      'email': 'naturaltest@example.com',
      'category': 'Technology',
      'balance': 10000.0
   }
   
   controller = NaturalPersonCreatorController(MockNaturalPersonRepository())
   response = controller.create_entity(entity_data)
   
   assert response["data"]["type"] == "Natural Entity"
   assert response["data"]["count"] == 1
   assert response["data"]["attributes"] == entity_data
   
def test_create_entity_error():
   entity_data = {
      'monthly_income': 'a1000',
      'age': 18,
      'name': 'Natural Test Create',
      'phone_number': '123456789',
      'email': 'naturaltest@example.com',
      'category': 'Technology',
      'balance': 10000.0
   }
   
   controller = NaturalPersonCreatorController(MockNaturalPersonRepository())
   with pytest.raises(Exception):
      controller.create_entity(entity_data)