from abc import ABC, abstractmethod 
from typing import List, Dict, Any

from utils.logger import log_call, log_error, log_time

class BaseTransactionRepository(ABC):

    @abstractmethod
    def get_all(self) -> List[Dict]:
        pass 

    @abstractmethod 
    def save(self, transactions: List[Dict]):
        pass 

    @abstractmethod
    def delete(self, id: str) -> List[Dict]:
        pass

    @abstractmethod
    def display(self, transactions: List[Dict]) -> None:
        pass

    @log_call
    @log_error
    @log_time
    def calculate_balance(self, transactions: List[Dict[str, Any]]) -> None:
        """Calcula el balance

        Args:
            transactions (List[Dict[str, Any]]): Lista de dicts de transacciones

        Returns:
            float: Balance total de transacciones
        """

        balance = 0

        for t in transactions:
            if t["tipo"] == "ingreso":
                balance += t["monto"]
            elif t["tipo"] == "gasto":
                balance -= t["monto"]
        return balance




