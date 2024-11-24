from unittest import mock
import pytest
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from src.models.sqlite.entities.legal_entity import LegalEntityTable
from src.models.sqlite.settings.connection import db_connect_handle
from .legal_entity_repository import LegalEntiytRepository

class MockConnection:
   def __init__(self):
      self.session = UnifiedAlchemyMagicMock(
         data = [
            (
               [mock.call.query(LegalEntityTable)],
               [
                  LegalEntityTable(id=1, trade_name="John Doe", balance=1000)
               ]
            )
         ]
      )
      
   def __enter__(self):
      return self
   
   def __exit__(self, exc_type, exc_val, exc_tb):
      pass
   
@pytest.mark.skip(reason= "Integration test with database")
def test_create_entity_integration():
   db_connect_handle.connect_to_db()
   repo = LegalEntiytRepository(db_connect_handle)
   entity = LegalEntityTable(
      billing=150000, age=30,
      trade_name="Enterprise ABC", phone_number="1234-5678",
      corporate_email="contact@abc.com", category="Category B",
      balance=100000
   )
   repo.create_entity(entity)
   
def test_create_entity():
   mock_connection = MockConnection()
   repo = LegalEntiytRepository(mock_connection)
   entity = LegalEntityTable(
      billing=150000, age=30,
      trade_name="Enterprise ABC", phone_number="1234-5678",
      corporate_email="contact@abc.com", category="Category B",
      balance=100000
   )
   repo.create_entity(entity)
   
   mock_connection.session.add.assert_called_once()
   mock_connection.session.commit.assert_called_once()

def test_get_entity_by_id():
   mock_connection = MockConnection()
   repo  = LegalEntiytRepository(mock_connection)
   reponse = repo.get_entity_by_id(1)
   
   mock_connection.session.query.assert_called_once_with(LegalEntityTable)
   mock_connection.session.filter.assert_called_once_with(LegalEntityTable.id == 1)
   
   assert reponse.id == 1
   assert reponse.trade_name == "John Doe"

def test_list_all():
   mock_connection = MockConnection()
   repo = LegalEntiytRepository(mock_connection)
   response = repo.list_all()
   
   mock_connection.session.query.assert_called_once_with(LegalEntityTable)
   mock_connection.session.all.assert_called_once()
   mock_connection.session.filter.assert_not_called()
   
   assert len(response) == 1
   assert response[0].id == 1
   assert response[0].trade_name == "John Doe"
   
def test_delete_by_id():
   mock_connection = MockConnection()
   repo = LegalEntiytRepository(mock_connection)
   repo.delete_by_id(1)
   
   mock_connection.session.query.assert_called_once_with(LegalEntityTable)
   mock_connection.session.filter.assert_called_once_with(LegalEntityTable.id == 1)
   mock_connection.session.delete.assert_called_once()
   
def test_withdraw_money():
   mock_connection = MockConnection()
   repo = LegalEntiytRepository(mock_connection)
   response = repo.withdraw_money(1, 500)
   
   mock_connection.session.query.assert_called_once_with(LegalEntityTable)
   mock_connection.session.filter.assert_called_once_with(LegalEntityTable.id == 1)
   mock_connection.session.commit.assert_called_once()
   
   assert response.balance == 500