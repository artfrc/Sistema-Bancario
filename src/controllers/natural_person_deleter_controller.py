from src.models.sqlite.interfaces.natural_person_repository_interface import NaturalPersonRepositoryInterface

class NaturalPersonDeleterController:
   def __init__(self, entity_repository: NaturalPersonRepositoryInterface):
      self.__entity_repository = entity_repository
      
   def delete(self, entity_id: int):
      self.__entity_repository.delete_by_id(entity_id)