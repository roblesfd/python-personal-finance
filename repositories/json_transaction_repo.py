from datetime import datetime
from tabulate import tabulate
from typing import List, Dict, Any

from .base_transaction_repo import BaseTransactionRepository
from utils.logger import log_call, log_error, log_time
from repositories.json_category_repo import JsonCategoryRepository
from db.storage import load_data, save_data

json_cat_repo = JsonCategoryRepository()

class JsonTransactionRepository(BaseTransactionRepository):
    @log_call
    @log_error
    @log_time
    def get_all(self) -> List[Dict]:
        """Obtiene todas las transacciones guardadas

        Returns:
            List[Dict]: Lista de dicts de transacciones
        """

        transactions = load_data("data.json")
        if not transactions:
            print("📭 No hay movimientos registrados.")
            return
        return transactions


    @log_call
    @log_error
    @log_time
    def save(self, transactions: List[Dict]):
        """Añade una transacción nueva

        Args:
            transactions (List[Dict]): Lista de dict de transactions
        """

        json_cat_repo.save(transactions[len(transactions)-1]["categoria"])

        save_data(transactions, "data.json")
        print("✅ Movimiento registrado correctamente.")


    @log_call
    @log_error
    @log_time
    def delete(self, id: int) -> List[Dict]:
        pass


    @log_call
    @log_error
    @log_time
    def display(self, data: List[Dict]) -> None:
        """ Muestra todas las transacciones existentes en una tabla

        Args:
            transactions (List[Dict]): Lista de dict transacciones a mostrar
        """

        table = [
            [i + 1, t["fecha"], t["tipo"], t["monto"], t["categoria"], t["descripcion"]]
            for i, t in enumerate(data)
        ]
        headers = ["No.", "Fecha", "Tipo", "Monto", "Categoría", "Descripción"]

        print(tabulate(table, headers=headers, tablefmt="fancy_grid"))


    @log_call
    @log_error
    @log_time
    def filter_by_category(self, transactions: List[Dict[str, Any]], category: str) -> List[Dict]:
        """Filtra categorias por campo 'category'

        Args:
            transactions (List[Dict[str, Any]]): Lista de dicts de transacciones
            category (str): Categoria a filtrar

        Returns:
            List[Dict]: Lista de dicts de transacciones filtradas
        """

        return [t for t in transactions if t["categoria"].lower() == category.lower()]


    @log_call
    @log_error
    @log_time
    def filter_by_type(self, transactions: List[Dict[str, Any]], type: str) -> List[Dict]:
        """Filtra categorias por campo 'type'

        Args:
            transactions (List[Dict[str, Any]]): Lista de dicts de transacciones
            type (str): Tipo a filtrar

        Returns:
            List[Dict]: Lista de dicts de transacciones filtradas
        """

        return [t for t in transactions if t["tipo"].lower() == type.lower()]


    @log_call
    @log_error
    @log_time
    def filter_by_date(self, transactions: List[Dict[str, Any]], start_date: datetime, end_date: datetime) -> List[Any]:
        """Filtra fechas por fecha inicial y fecha final

        Args:
            transactions (List[Dict[str, Any]]): Lista de dicts de transacciones
            start_date (str): Fecha de inicio
            end_date (str): Fecha de fin

        Returns:
            List[Any]: Lista de dicts de transacciones filtradas
        """

        return [
            t for t in transactions
            if start_date <= datetime.fromisoformat(t['fecha']) <= end_date
        ]
        



