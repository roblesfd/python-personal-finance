from cli import transactions_cli, categories_cli, base_cli
from handlers.categories import CategoryHandler
from handlers import transactions
from repositories.json_category_repo import JsonCategoryRepository 

def main():
    """Función principal para ejecutar el programa
    """
    parser, subparsers = base_cli.config_parsers()
    category_handler = CategoryHandler(JsonCategoryRepository())

    # transaction subparsers
    transactions_cli.config_subparser_add(subparsers)
    transactions_cli.config_subparser_list(subparsers)
    transactions_cli.config_subparser_report(subparsers)
    transactions_cli.config_subparser_export(subparsers)

    # category subparsers
    categories_cli.config_subparser_list(subparsers)
    categories_cli.config_subparser_display(subparsers)
    categories_cli.config_subparser_delete(subparsers)

    args = parser.parse_args()

    commands = {
        "add": transactions.handle_add,
        "list": transactions.handle_list,
        "report": transactions.handle_report,
        "export": transactions.handle_export,
        "listcat": category_handler.handle_list,
        "displaycat": category_handler.handle_display,
        "deletecat": category_handler.handle_delete,
    }

    if args.command in commands:
        commands[args.command](args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
