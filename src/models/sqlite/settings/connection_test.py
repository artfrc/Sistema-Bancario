import pytest
from sqlalchemy.engine import Engine
from .connection import db_connect_handle

@pytest.mark.skip(reason="Interaction with the database")
def test_connect_to_db():
   assert db_connect_handle.get_engine() is not None
   
   db_connect_handle.connect_to_db()
   db_engine = db_connect_handle.get_engine()
   
   assert db_engine is not None
   assert isinstance(db_engine, Engine)