import argparse
from datetime import datetime

from categories import add_category, display_categories, get_categories, delete_category
from .base_cli import config_parsers


def config_subparser_list(subparsers):
    subparsers.add_parser("listcat", help="Lista toda las categorias")


def config_subparser_display(subparsers):
    subparsers.add_parser("displaycat", help="Muestra toda las categorias en una tabla")
    

def config_subparser_delete(subparsers):
    delete_subparser = subparsers.add_parser("deletecat", help="Elimina una categoría")
    delete_subparser.add_argument("category", type=str, help="Nombre de la categoría")
    

def handle_list(args):
    categories = get_categories()
    return categories


def handle_display(args):
    categories = get_categories()
    display_categories(categories)


def handle_delete(args):
    updated_categories = delete_category(args.category)
    return updated_categories
