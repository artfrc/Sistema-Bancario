from typing import List
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.natural_person import NaturalPersonTable
from src.models.sqlite.interfaces.natural_person_repository_interface import NaturalPersonRepositoryInterface

class NaturalPersonRepository(NaturalPersonRepositoryInterface):
   def __init__(self, db_connection):
      self.__db_connection = db_connection
      
   def create_natural_person(self, natural_person: NaturalPersonTable):
      with self.__db_connection as database:
         try:
            database.session.add(natural_person)
            database.session.commit()
         except Exception as exception:
            database.session.rollback()
            raise exception
         
   def get_person_by_id(self, person_id: int) -> NaturalPersonTable: 
      with self.__db_connection as database:
         try:
            person = (
               database.session
               .query(NaturalPersonTable)
               .filter(NaturalPersonTable.id == person_id)
               .first()
            )
            return person
            
         except NoResultFound:
            return None
   
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
         
   def withdraw_money(self, entity_id: int, amount: float) -> NaturalPersonTable:
      with self.__db_connection as database:
         try:
            natural_person = (
               database.session
               .query(NaturalPersonTable)
               .filter(NaturalPersonTable.id == entity_id)
               .first()
            )
            natural_person.balance -= amount
            database.session.commit()
            
            return natural_person
         
         except Exception as exception:
            database.session.rollback()
            raise exception
      