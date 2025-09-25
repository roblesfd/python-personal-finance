from storage import load_data, save_data
from datetime import datetime
from tabulate import tabulate

from models import Movimiento


def add_transaction(tipo, monto, categoria, descripcion):
    data = get_transactions()
    transaction = {
        "tipo": tipo,
        "monto": monto,
        "categoria": categoria,
        "descripcion": descripcion,
        "fecha": datetime.now().isoformat()
    }
    data.append(transaction)
    save_data(data)
    print("✅ Movimiento registrado correctamente.", transaction)


def display_transactions(transactions):
    table = [
        [i + 1, t["fecha"], t["tipo"], t["monto"], t["categoria"], t["descripcion"]]
        for i, t in enumerate(transactions)
    ]
    headers = ["#", "Fecha", "Tipo", "Monto", "Categoría", "Descripción"]

    print(tabulate(table, headers=headers, tablefmt="fancy_grid"))


def get_transactions():
    transactions = load_data()
    if not transactions:
        print("📭 No hay movimientos registrados.")
        return
    return transactions


def calculate_balance(transactions):
    balance = 0

    for t in transactions:
        if t["tipo"] == "ingreso":
            balance += t["monto"]
        elif t["tipo"] == "gasto":
            balance -= t["monto"]
    return balance


def filter_by_category(transactions, category):
    return [t for t in transactions if t["categoria"].lower() == category.lower()]


def filter_by_type(transactions, type):
    return [t for t in transactions if t["tipo"].lower() == type.lower()]


def filter_by_date(transactions, start_date, end_date):
    return [
        t for t in transactions
        if start_date <= datetime.fromisoformat(t['fecha']) <= end_date
    ]
    
