from src.models.sqlite.interfaces.legal_entity_repository_interface import LegalEntityRepositoryInterface

class LegalEntityDeleterController:
   def __init__(self, entity_repository: LegalEntityRepositoryInterface):
      self.__entity_repository = entity_repository
      
   def delete(self, entity_id: int):
      self.__entity_repository.delete_by_id(entity_id)