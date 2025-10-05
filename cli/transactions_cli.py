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


def config_subparser_display(subparsers):
    """Configura el subparser para comando display (transactions) con sus argumentos

    Args:
        subparsers (SubParsersAction): Configura comando para display transactions
    """
    display_parser = subparsers.add_parser("display", help="Mostrar movimientos en una tabla")
    display_parser.add_argument("-c", "--categoria", type=str, help="Filtrar por categoría")
    display_parser.add_argument("-t", "--tipo", type=str, help="Filtrar por tipo")
    display_parser.add_argument("-start", "--desde", type=str, default="", help="Fecha inicio (AAAA-MM-DD)")
    display_parser.add_argument("-end", "--hasta", type=str, default="", help="Fecha fin (AAAA-MM-DD)")


def config_subparser_export(subparsers):
    """Configura el subparser para comando export (transactions) con sus argumentos

    Args:
        subparsers (SubParsersAction): Configura comando para export transaction
    """
    export_parser = subparsers.add_parser("export", help="Genera un archivo de reporte de todas las transacciones (csv, pdf)")
    export_parser.add_argument("format", type=str, choices=["csv", "pdf"], help="Tipo de formato a exportar")


def config_subparser_delete(subparsers):
    """Configura el subparser para comando delete (transaction)

    Args:
        subparsers (SubParsersAction): Configura comando para delete
    """
    delete_subparser = subparsers.add_parser("delete", help="Elimina un movimiento")
    delete_subparser.add_argument("id", type=int, help="ID del movimiento")
    
