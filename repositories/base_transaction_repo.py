from abc import ABC, abstractmethod 
from typing import List, Dict 

class BaseTransactionRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[Dict]:
        pass 

    @abstractmethod 
    def save(self, transactions: List[Dict]):
        pass 

    @abstractmethod
    def delete(self, nombre: str) -> List[Dict]:
        pass

    @abstractmethod
    def display(self, transactions: List[Dict]) -> None:
        pass




