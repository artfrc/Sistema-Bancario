from .natural_person_finder_controller import NaturalPersonFinderController

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
   
   def list_all(self):
      return [
         MockNaturalPerson(
            age = 25,
            name = 'John Doe',
            phone_number = '1234567890',
            email = 'john@example.com'
         ),
         MockNaturalPerson(
            age = 30,
            name = 'Jane Doe',
            phone_number = '0987654321',
            email = 'jane@example.com'
         )
      ]

def test_find_entity():
   controller = NaturalPersonFinderController(MockNaturalPersonRepository())
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

def test_find_all_entities():
   controller = NaturalPersonFinderController(MockNaturalPersonRepository())
   response = controller.find_all_entities()
   
   expected_response = {
      'data': {
         'type': 'Natural Person', 
         'count': 2, 
         'attributes': [
            {
               'age': 25, 
               'name': 'John Doe', 
               'phone number': '1234567890', 
               'email': 'john@example.com'}, 
            {
               'age': 30, 
               'name': 'Jane Doe', 
               'phone number': '0987654321', 
               'email': 'jane@example.com'}
            ]
         }
      }
   
   assert response == expected_response