from typing import List
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.legal_entity import LegalEntityTable

class LegalEntiytRepository:
   def __init__(self, db_connection):
      self.__db_connection = db_connection
      
   def list_all(self) -> List[LegalEntityTable]:
      with self.__db_connection as database:
         try:
            entities = database.session.query(LegalEntityTable).all()
            return entities
         
         except NoResultFound:
            return []
            