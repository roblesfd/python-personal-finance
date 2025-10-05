from cli import transactions_cli, categories_cli, base_cli
from handlers.categories import CategoryHandler
from handlers.transactions import TransactionHandler
# from repositories.json_category_repo import JsonCategoryRepository 
# from repositories.json_transaction_repo import JsonTransactionRepository 
from repositories.sqlite_transaction_repo import SQLiteTransactionRepository
from repositories.sqlite_category_repo import SqliteCategoryRepository

def main():
    """Función principal para ejecutar el programa
    """
    parser, subparsers = base_cli.config_parsers()
    category_handler = CategoryHandler(SqliteCategoryRepository())
    transaction_handler = TransactionHandler(SQLiteTransactionRepository())

    # transaction subparsers
    transactions_cli.config_subparser_add(subparsers)
    transactions_cli.config_subparser_list(subparsers)
    transactions_cli.config_subparser_display(subparsers)
    transactions_cli.config_subparser_export(subparsers)
    transactions_cli.config_subparser_delete(subparsers)

    # category subparsers
    categories_cli.config_subparser_list(subparsers)
    categories_cli.config_subparser_display(subparsers)
    categories_cli.config_subparser_delete(subparsers)

    args = parser.parse_args()

    commands = {
        "add": transaction_handler.handle_add,
        "list": transaction_handler.handle_list,
        "display": transaction_handler.handle_display,
        "export": transaction_handler.handle_export,
        "delete": transaction_handler.handle_delete,
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
