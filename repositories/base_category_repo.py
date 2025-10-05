from abc import ABC, abstractmethod 
from typing import List, Dict 

class CategoryRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[Dict]:
        pass 

    @abstractmethod 
    def save(self, categories: List[Dict]):
        pass 

    @abstractmethod
    def delete(self, nombre: str) -> List[Dict]:
        pass




