from storage import load_data, save_data

from logger import log_call
from tabulate import tabulate


@log_call
def add_category(category: str) -> list[dict]:
    """Añade una categoria

    Args:
        category (str): NOmbre de categoria

    Returns:
        list[dict]: Lista de dict actualizada de categorias
    """
    categories = load_data("categories.json")
    if not categories:
        print("📭 No hay categorias registradas.")
        return
    
    if any(cat["nombre"] == category for cat in categories):
        return
    
    categories.append({"nombre": category})
    save_data(categories, "categories.json")

    return categories


@log_call
def display_categories(categories: list[dict]):
    """Muestra todas las categorias en una tabla

    Args:
        categories (list[dict]): Lista de dict de categorias
    """

    table = [
        [i + 1, t["nombre"]]
        for i, t in enumerate(categories)
    ]
    headers = ["No.", "Nombre"]

    print(tabulate(table, headers=headers, tablefmt="fancy_grid"))


@log_call
def get_categories() -> list[dict]:
    """Obtiene un list con todas la categorias

    Returns:
        list[dict]: Lista de dict de categorias
    """
    categories = load_data("categories.json")
    if not categories:
        print("📭 No hay categorias registradas.")
        return
    return categories


@log_call
def delete_category(nombre: str) -> list[dict]:
    """Elimina una categoria

    Args:
        nombre (str): Nombre de la categoría

    Returns:
        list[dict]: Lista actualizada de categorias
    """
    categories = load_data("categories.json")

    if not categories:
        print("📭 No hay categorias para eliminar.")
        return
    
    if all( cat["nombre"] != nombre for cat in categories):
        print(f"No existe una categoria con el nombre {nombre}")
        return
    
    updated_categories = [cat for cat in categories if cat["nombre"] != nombre]
    
    save_data(updated_categories, "categories.json")
    return updated_categories
    

    


