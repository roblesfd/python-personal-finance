from datetime import datetime
from functools import reduce
from pprint import pprint

from model.models import Movimiento
from repositories.transactions import add_transaction, display_transactions, get_transactions, calculate_balance, filter_by_category, filter_by_date, filter_by_type 
from export.export_csv import export_to_csv
from export.export_pdf import export_to_pdf
from .base_cli import config_parsers
from utils.logger import log_error, log_call


def config_subparser_add(subparsers):
    """Configura el subparser para comando add (transaction) con sus argumentos

    Args:
        subparsers (SubParsersAction): Configura comando para add transaction
    """
    add_parser = subparsers.add_parser("add", help="Agregar un movimiento")
    
    add_parser.add_argument("tipo", choices=["ingreso", "gasto"], help="Tipo de movimiento")  
    add_parser.add_argument("monto", type=float, help="Cantidad de dinero")
    add_parser.add_argument("-c", "--categoria", default="general", help="Categoría de movimiento")
    add_parser.add_argument("-d", "--descripcion", default="", help="Descripción opcional")


def config_subparser_list(subparsers):
    """Configura el subparser para comando list (transactions)

    Args:
        subparsers (SubParsersAction): Configura comando para list transactions
    """
    subparsers.add_parser("list", help="Listar todos los movimientos")


def config_subparser_report(subparsers):
    """Configura el subparser para comando report (transactions) con sus argumentos

    Args:
        subparsers (SubParsersAction): Configura comando para report transactions
    """
    report_parser = subparsers.add_parser("report", help="Mostrar reportes")
    report_parser.add_argument("-c", "--categoria", type=str, help="Filtrar por categoría")
    report_parser.add_argument("-t", "--tipo", type=str, help="Filtrar por tipo")
    report_parser.add_argument("-start", "--desde", type=str, default="", help="Fecha inicio (AAAA-MM-DD)")
    report_parser.add_argument("-end", "--hasta", type=str, default="", help="Fecha fin (AAAA-MM-DD)")


def config_subparser_export(subparsers):
    """Configura el subparser para comando export (transactions) con sus argumentos

    Args:
        subparsers (SubParsersAction): Configura comando para export transaction
    """
    export_parser = subparsers.add_parser("export", help="Genera un archivo de reporte de todas las transacciones (csv, pdf)")
    export_parser.add_argument("format", type=str, choices=["csv", "pdf"], help="Tipo de formato a exportar")


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

    print(type(start_date))

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


