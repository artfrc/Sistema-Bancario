from .legal_entity_finder_controller import LegalEntityFinderController

class MockEntity:
   def __init__(self, age, trade_name, phone_number, corporate_email, category):
      self.age = age
      self.trade_name = trade_name
      self.phone_number = phone_number
      self.corporate_email = corporate_email,
      self.category = category

class MockEntityRepository:
   def get_entity_by_id(self, entity_id: int): # pylint: disable=W0613, unused-argument
      return MockEntity(
         age = 25,
         trade_name = 'John Doe',
         phone_number = '1234567890',
         corporate_email = 'john@example.com',
         category = 'Natural Person'
      )

def test_find_entity():
   controller = LegalEntityFinderController(MockEntityRepository())
   reponse = controller.find_entity(123)
   
   expected_response = {
      'data': {
         'type': 'Legal Entity', 
         'count': 1, 
         'attributes': {
            'age': 25, 
            'trade name': 'John Doe', 
            'phone number': '1234567890', 
            'corporate email': ('john@example.com',), 
            'category': 'Natural Person'
         }
      }
   }
   
   assert reponse == expected_response