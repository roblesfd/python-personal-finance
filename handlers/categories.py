from repositories.categories import add_category, display_categories, get_categories, delete_category


def handle_list(args):
    """Handler para comando listcat

    Args:
        args (list[str]): Lista de argumentos de CLI 
    """
    categories = get_categories()
    return categories


def handle_display(args):
    """Handler para comando displaycat

    Args:
        args (list[str]): Lista de argumentos de CLI 
    """
    categories = get_categories()
    display_categories(categories)


def handle_delete(args):
    """Handler para comando deletecat

    Args:
        args (list[str]): Lista de argumentos de CLI 
    """
    updated_categories = delete_category(args.category)
    return updated_categories
