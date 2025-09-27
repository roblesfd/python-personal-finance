import argparse

def config_parsers():
    parser = argparse.ArgumentParser(description="CLI Finanzas Personales")
    subparsers = parser.add_subparsers(dest="command")

    return parser, subparsers
