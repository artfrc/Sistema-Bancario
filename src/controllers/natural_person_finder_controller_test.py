from .natural_person_finder_controller import NaturalEntityFinderController

class MockNaturalPerson:
   def __init__(self, age, name, phone_number, email):
      self.age = age
      self.name = name
      self.phone_number = phone_number
      self.email = email

class MockNaturalPersonRepository:
   def get_entity_by_id(self, entity_id: int): # pylint: disable=W0613, unused-argument
      return MockNaturalPerson(
         age = 25,
         name = 'John Doe',
         phone_number = '1234567890',
         email = 'john@example.com'
      )

def test_find_entity():
   controller = NaturalEntityFinderController(MockNaturalPersonRepository())
   reponse = controller.find_entity(123)
   
   expected_response = {
      'data': {
         'type': 'Natural Person', 
         'count': 1, 
         'attributes': {
            'age': 25, 
            'name': 'John Doe', 
            'phone number': '1234567890'}, 
            'email': 'john@example.com'
      }
   }
   
   assert reponse == expected_response