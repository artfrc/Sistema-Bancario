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
         
   def delete_by_id(self, person_id: int):
      with self.__db_connection as database:
         try:
            (
               database.session
               .query(NaturalPersonTable)
               .filter(NaturalPersonTable.id == person_id)
               .delete()
            )
            database.session.commit()
         except Exception as exception:
            database.session.rollback()
            raise exception
      