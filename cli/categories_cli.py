from datetime import datetime



def config_subparser_list(subparsers):
    """Configura el subparser para comando listcat

    Args:
        subparsers (SubParsersAction): Configura comandos para list categories
    """
    subparsers.add_parser("listcat", help="Lista toda las categorias")


def config_subparser_display(subparsers):
    """Configura el subparser para comando displaycat

    Args:
        subparsers (SubParsersAction): Configura comando para display categories
    """
    subparsers.add_parser("displaycat", help="Muestra toda las categorias en una tabla")
    

def config_subparser_delete(subparsers):
    """Configura el subparser para comando deletecat

    Args:
        subparsers (SubParsersAction): Configura comando para delete categories
    """
    delete_subparser = subparsers.add_parser("deletecat", help="Elimina una categoría")
    delete_subparser.add_argument("category", type=str, help="Nombre de la categoría")
    
