from datetime import datetime
from tabulate import tabulate
from typing import List, Dict, Any

from utils.logger import log_call, log_error, log_time
from repositories.categories import add_category
from db.storage import load_data, save_data


@log_call
@log_error
@log_time
def add_transaction(transaction: List[Dict[str, Any]]) -> None:
    """Añade una transacción nueva

    Args:
        transaction (_type_): _description_
    """
    
    transactions = get_transactions()
    transactions.append(transaction)

    add_category(transaction["categoria"])

    save_data(transactions, "data.json")
    print("✅ Movimiento registrado correctamente.", transaction)


@log_call
@log_error
@log_time
def display_transactions(transactions: List[Dict[str, Any]]) -> None:
    """ Muestra todas las transacciones existentes en una tabla

    Args:
        transactions (list[dict]): Lista de dict transacciones a mostrar
    """

    table = [
        [i + 1, t["fecha"], t["tipo"], t["monto"], t["categoria"], t["descripcion"]]
        for i, t in enumerate(transactions)
    ]
    headers = ["No.", "Fecha", "Tipo", "Monto", "Categoría", "Descripción"]

    print(tabulate(table, headers=headers, tablefmt="fancy_grid"))


@log_call
@log_error
@log_time
def get_transactions() -> None:
    """Obtiene todas las transacciones guardadas

    Returns:
        list[dict]: Lista de dicts de transacciones
    """

    transactions = load_data("data.json")
    if not transactions:
        print("📭 No hay movimientos registrados.")
        return
    return transactions


@log_call
@log_error
@log_time
def calculate_balance(transactions: List[Dict[str, Any]]) -> None:
    """Calcula el balance

    Args:
        transactions (list[dict]): Lista de dicts de transacciones

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


@log_call
@log_error
@log_time
def filter_by_category(transactions: List[Dict[str, Any]], category: str) -> None:
    """Filtra categorias por campo 'category'

    Args:
        transactions (list[dict]): Lista de dicts de transacciones
        category (str): Categoria a filtrar

    Returns:
        list[dict]: Lista de dicts de transacciones filtradas
    """

    return [t for t in transactions if t["categoria"].lower() == category.lower()]


@log_call
@log_error
@log_time
def filter_by_type(transactions: List[Dict[str, Any]], type: str) -> None:
    """Filtra categorias por campo 'type'

    Args:
        transactions (list[dict]): Lista de dicts de transacciones
        type (str): Tipo a filtrar

    Returns:
        list[dict]: Lista de dicts de transacciones filtradas
    """

    return [t for t in transactions if t["tipo"].lower() == type.lower()]


@log_call
@log_error
@log_time
def filter_by_date(transactions: List[Dict[str, Any]], start_date: datetime, end_date: datetime) -> List[Any]:
    """Filtra fechas por fecha inicial y fecha final

    Args:
        transactions (list[dict]): Lista de dicts de transacciones
        start_date (str): Fecha de inicio
        end_date (str): Fecha de fin

    Returns:
        list[dict]: Lista de dicts de transacciones filtradas
    """

    return [
        t for t in transactions
        if start_date <= datetime.fromisoformat(t['fecha']) <= end_date
    ]
    
