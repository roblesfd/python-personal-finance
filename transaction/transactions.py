from storage import load_data, save_data
from datetime import datetime
from tabulate import tabulate

from models import Movimiento
from logger import log_call

@log_call
def add_transaction(transaction):
    data = get_transactions()
    data.append(transaction)
    save_data(data)
    print("✅ Movimiento registrado correctamente.", transaction)


@log_call
def display_transactions(transactions):
    table = [
        [i + 1, t["fecha"], t["tipo"], t["monto"], t["categoria"], t["descripcion"]]
        for i, t in enumerate(transactions)
    ]
    headers = ["#", "Fecha", "Tipo", "Monto", "Categoría", "Descripción"]

    print(tabulate(table, headers=headers, tablefmt="fancy_grid"))


@log_call
def get_transactions():
    transactions = load_data()
    if not transactions:
        print("📭 No hay movimientos registrados.")
        return
    return transactions


@log_call
def calculate_balance(transactions):
    balance = 0

    for t in transactions:
        if t["tipo"] == "ingreso":
            balance += t["monto"]
        elif t["tipo"] == "gasto":
            balance -= t["monto"]
    return balance


@log_call
def filter_by_category(transactions, category):
    return [t for t in transactions if t["categoria"].lower() == category.lower()]


@log_call
def filter_by_type(transactions, type):
    return [t for t in transactions if t["tipo"].lower() == type.lower()]


@log_call
def filter_by_date(transactions, start_date, end_date):
    return [
        t for t in transactions
        if start_date <= datetime.fromisoformat(t['fecha']) <= end_date
    ]
    
