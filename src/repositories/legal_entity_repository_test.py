from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from src.models.sqlite.entities.legal_entity import LegalEntityTable
from .legal_entity_repository import LegalEntiytRepository

class MockConnection:
   def __init__(self):
      self.session = UnifiedAlchemyMagicMock(
         data = [
            (
               [mock.call.query(LegalEntityTable)],
               [
                  LegalEntityTable(id=1, trade_name="John Doe"),
                  LegalEntityTable(id=2, trade_name="Jane Doe")
               ]
            )
         ]
      )
      
   def __enter__(self):
      return self
   
   def __exit__(self, exc_type, exc_val, exc_tb):
      pass
   
def test_list_all():
   mock_connection = MockConnection()
   repo = LegalEntiytRepository(mock_connection)
   response = repo.list_all()
   
   mock_connection.session.query.assert_called_once_with(LegalEntityTable)
   mock_connection.session.all.assert_called_once()
   mock_connection.session.filter.assert_not_called()
   
   assert len(response) == 2
   assert response[0].id == 1
   assert response[0].trade_name == "John Doe"
   assert response[1].id == 2
   assert response[1].trade_name == "Jane Doe"
   
def test_delete_by_id():
   mock_connection = MockConnection()
   repo = LegalEntiytRepository(mock_connection)
   repo.delete_by_id(1)
   
   mock_connection.session.query.assert_called_once_with(LegalEntityTable)
   mock_connection.session.filter.assert_called_once_with(LegalEntityTable.id == 1)
   mock_connection.session.delete.assert_called_once()
   
   
   
   
   
