import argparse
from datetime import datetime

from models import Movimiento
from transaction.transactions import add_transaction, display_transactions, get_transactions, calculate_balance, filter_by_category, filter_by_date, filter_by_type 
from export.export_csv import export_csv
from export.export_pdf import export_to_pdf


def config_parsers():
    parser = argparse.ArgumentParser(description="CLI Finanzas Personales")
    subparsers = parser.add_subparsers(dest="command")

    return parser, subparsers


def config_subparser_add(subparsers):
    add_parser = subparsers.add_parser("add", help="Agregar un movimiento")
    
    add_parser.add_argument("tipo", choices=["ingreso", "gasto"], help="Tipo de movimiento")  
    add_parser.add_argument("monto", type=float, help="Cantidad de dinero")
    add_parser.add_argument("-c", "--categoria", default="general", help="Categoría de movimiento")
    add_parser.add_argument("-d", "--descripcion", default="", help="Descripción opcional")


def config_subparser_list(subparsers):
    subparsers.add_parser("list", help="Listar todos los movimientos")


def config_subparser_report(subparsers):
    report_parser = subparsers.add_parser("report", help="Mostrar reportes")
    report_parser.add_argument("-c", "--categoria", type=str, help="Filtrar por categoría")
    report_parser.add_argument("-t", "--tipo", type=str, help="Filtrar por tipo")
    report_parser.add_argument("-start", "--desde", type=str, help="Fecha inicio (AAAA-MM-DD)")
    report_parser.add_argument("-end", "--hasta", type=str, help="Fecha fin (AAAA-MM-DD)")


def config_subparser_export(subparsers):
    export_parser = subparsers.add_parser("export", help="Muestra un reporte de todas las transacciones")
    export_parser.add_argument("format", type=str, choices=["csv", "pdf"], help="Tipo de formato a exportar")


def config_args(parser):
    args = parser.parse_args()

    return args


def handle_add(args):
    transaction = {
        "tipo": args.tipo,
        "monto": args.monto,
        "categoria": args.categoria,
        "descripcion": args.descripcion,
        "fecha": datetime.now().isoformat()
    }
    add_transaction(transaction)


def handle_list(args):
    transactions = get_transactions()
    display_transactions(transactions)


def handle_report(args):
    transactions = get_transactions()

    if args.categoria:
        transactions = filter_by_category(transactions, args.categoria)
    if args.tipo:
        transactions = filter_by_type(transactions, args.tipo)
    if args.desde and args.hasta:
        start_date = datetime.strptime(args.desde, "%Y-%m-%d")
        end_date = datetime.strptime(args.hasta, "%Y-%m-%d")
        transactions = filter_by_date(transactions, start_date, end_date)
    
    balance = calculate_balance(transactions)
    print("Reporte")
    display_transactions(transactions)
    print(f"Balance total: {balance}")


def handle_export(args):
    transactions = get_transactions()
    if args.format == "csv":
        export_csv(transactions, "movimientos.csv")
    elif args.format == "pdf":
        export_to_pdf(transactions, "movimientos.pdf")


def main():
    parser, subparsers = config_parsers()
    config_subparser_add(subparsers)
    config_subparser_list(subparsers)
    config_subparser_report(subparsers)
    config_subparser_export(subparsers)
    args = config_args(parser)

    commands = {
        "add": handle_add,
        "list": handle_list,
        "report": handle_report,
        "export": handle_export
    }

    if args.command in commands:
        commands[args.command](args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
