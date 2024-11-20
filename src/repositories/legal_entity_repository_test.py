import pytest
from src.models.sqlite.settings.connection import db_connect_handle
from .legal_entity_repository import LegalEntiytRepository

db_connect_handle.connect_to_db()

@pytest.mark.skip(reason="Interaction with the database")
def test_list_all():
   repo  = LegalEntiytRepository(db_connect_handle)
   response = repo.list_all()
   print()
   print(response)