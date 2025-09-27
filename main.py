from cli import transactions_cli, categories_cli, base_cli

def main():
    parser, subparsers = base_cli.config_parsers()

    # trasanction subparsers
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
        "add": transactions_cli.handle_add,
        "list": transactions_cli.handle_list,
        "report": transactions_cli.handle_report,
        "export": transactions_cli.handle_export,
        "listcat": categories_cli.handle_list,
        "displaycat": categories_cli.handle_display,
        "deletecat": categories_cli.handle_delete,
    }

    if args.command in commands:
        commands[args.command](args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
