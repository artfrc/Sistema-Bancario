from unittest import mock
import pytest
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from src.models.sqlite.entities.natural_person import NaturalPersonTable
from src.models.sqlite.settings.connection import db_connect_handle
from .natural_person_repository import NaturalPersonRepository

class MockConnection:
   def __init__(self):
      self.session = UnifiedAlchemyMagicMock(
         data = [
            (
               [mock.call.query(NaturalPersonTable)],
               [
                  NaturalPersonTable(id=1, name="John Doe"),
                  NaturalPersonTable(id=2, name="Jane Doe")
               ]
            )
         ]
      )
   
   def __enter__(self):
      return self
   
   def __exit__(self, exc_type, exc_val, exc_tb):
      pass
   
@pytest.mark.skip(reason= "Integration test with database")
def test_create_natural_person_integration():
   db_connect_handle.connect_to_db()
   repo = NaturalPersonRepository(db_connect_handle)
   entity = NaturalPersonTable(
      monthly_income=150000, age=30,
      name="John Doe", phone_number="1234-5678",
      email="john@example.com", category="Category D",
      balance=100000
   )
   repo.create_natural_person(entity)
   
def test_create_entity():
   mock_connection = MockConnection()
   repo = NaturalPersonRepository(mock_connection)
   entity = NaturalPersonTable(
      monthly_income=150000, age=30,
      name="John Doe", phone_number="1234-5678",
      email="john@example.com", category="Category D",
      balance=100000
   )
   repo.create_natural_person(entity)
   
   mock_connection.session.add.assert_called_once()
   mock_connection.session.commit.assert_called_once()

def test_list_all():
   mock_connection = MockConnection()
   repo = NaturalPersonRepository(mock_connection)
   response = repo.list_all()
   
   mock_connection.session.query.assert_called_once_with(NaturalPersonTable)
   mock_connection.session.all.assert_called_once()
   mock_connection.session.filter.assert_not_called()
   
   assert len(response) == 2
   assert response[0].id == 1
   assert response[0].name == "John Doe"
   assert response[1].id == 2
   assert response[1].name == "Jane Doe"
   
def test_delete_by_id():
   mock_connection = MockConnection()
   repo = NaturalPersonRepository(mock_connection)
   repo.delete_by_id(1)
   mock_connection.session.query.assert_called_once_with(NaturalPersonTable)
   mock_connection.session.filter.assert_called_once_with(NaturalPersonTable.id == 1)
   mock_connection.session.delete.assert_called_once()