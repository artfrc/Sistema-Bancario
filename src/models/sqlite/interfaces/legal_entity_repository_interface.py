from abc import ABC, abstractmethod
from typing import List

from src.models.sqlite.entities.legal_entity import LegalEntityTable

class LegalEntityRepositoryInterface(ABC):
   
   @abstractmethod
   def create_entity(self, legal_entity: LegalEntityTable):
      pass
   
   @abstractmethod
   def get_entity_by_id(self, entity_id: int):
      pass
   
   @abstractmethod
   def list_all(self) -> List[LegalEntityTable]:
      pass
   
   @abstractmethod
   def delete_by_id(self, entity_id: int):
      pass
   

   