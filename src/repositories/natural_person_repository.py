from typing import List
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.natural_person import NaturalPersonTable

class NaturalPersonRepository:
   def __init__(self, db_connection):
      self.__db_connection = db_connection
   
   def list_all(self) -> List[NaturalPersonTable]:
      with self.__db_connection as database:
         try:
            people = database.session.query(NaturalPersonTable).all()
            return people
         
         except NoResultFound:
            return []
      