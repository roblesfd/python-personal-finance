import argparse

def config_parsers():
    """Configura objetos de parser y subparser

    Returns:
        parser  (AgumentParser): Contenedor para especificaciones de argumento
        subparsers (SubParsersAction): Para configurar subcomandos
    """
    parser = argparse.ArgumentParser(description="CLI Finanzas Personales")
    subparsers = parser.add_subparsers(dest="command")

    return parser, subparsers
