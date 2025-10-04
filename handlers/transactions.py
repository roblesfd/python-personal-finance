from datetime import datetime
from functools import reduce
from pprint import pprint

from repositories.transactions import add_transaction, display_transactions, get_transactions, calculate_balance, filter_by_category, filter_by_date, filter_by_type 
from export.export_csv import export_to_csv
from export.export_pdf import export_to_pdf


def handle_add(args):
    """Handler para comando add

    Args:
        args (list[str]): Lista de argumentos de CLI 
    """
    transaction = {
        "tipo": args.tipo,
        "monto": args.monto,
        "categoria": args.categoria,
        "descripcion": args.descripcion,
        "fecha": datetime.now().isoformat()
    }
    add_transaction(transaction)


def handle_list(args):
    """Handler para comando list

    Args:
        args (list[str]): Lista de argumentos de CLI 
    """
    transactions = get_transactions()
    pprint(transactions)


def handle_report(args):
    """Handler para comando report

    Args:
        args (list[str]): Lista de argumentos de CLI 
    """

    start_date = datetime.strptime(args.desde, "%Y-%m-%d") if args.desde else datetime.min
    end_date = datetime.strptime(args.hasta, "%Y-%m-%d") if args.hasta else datetime.max

    filters = [
        (lambda tx: filter_by_category(tx, args.categoria)) if args.categoria else None,
        (lambda tx: filter_by_type(tx, args.tipo)) if args.tipo else None,
        (lambda tx: filter_by_date(tx, start_date, end_date)) if (args.desde or args.hasta) else None,
    ]

    transactions = reduce(lambda acc, f: f(acc) if f else acc, filters, get_transactions())
    
    balance = calculate_balance(transactions)
    print("Reporte de movimientos")
    display_transactions(transactions)
    print(f"Balance total: {balance}")


def handle_export(args):
    """Handler para comando export

    Args:
        args (list[str]): Lista de argumentos de CLI 
    """
    transactions = get_transactions()
    if args.format == "csv":
        export_to_csv(transactions, "movimientos.csv")
    elif args.format == "pdf":
        export_to_pdf(transactions, "movimientos.pdf")


