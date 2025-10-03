import argparse

def config_parsers():
    """Configura objetos de parser y subparser

    Returns:
        AgumentParser: Contenedor para especificaciones de argumento
        SubParsersAction: Para configurar subcomandos
    """
    parser = argparse.ArgumentParser(description="CLI Finanzas Personales")
    subparsers = parser.add_subparsers(dest="command")

    return parser, subparsers
