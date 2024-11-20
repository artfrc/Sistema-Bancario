import pytest
from src.models.sqlite.settings.connection import db_connect_handle
from .natural_person_repository import NaturalPersonRepository

db_connect_handle.connect_to_db()

@pytest.mark.skip(reason="Interaction with the database")
def test_list_all():
   repo = NaturalPersonRepository(db_connect_handle)
   response = repo.list_all()
   print()
   print(response)