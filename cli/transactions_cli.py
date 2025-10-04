from datetime import datetime
from functools import reduce
from pprint import pprint


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


