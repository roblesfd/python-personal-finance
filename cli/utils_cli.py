from utils.docs import open_docs

def config_subparser_open_docs(subparsers):
    """Configura el subparser para comando opendocscon sus argumentos

    Args:
        subparsers (SubParsersAction): Configura comando para opendocs
    """
    subparsers.add_parser("opendocs", help="Ver la documentación del paquete")
    
def handle_open_docs(args):
    open_docs()