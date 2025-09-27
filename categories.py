from storage import load_data, save_data

from logger import log_call
from tabulate import tabulate


@log_call
def add_category(category):
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
def display_categories(categories):
    table = [
        [i + 1, t["nombre"]]
        for i, t in enumerate(categories)
    ]
    headers = ["No.", "Nombre"]

    print(tabulate(table, headers=headers, tablefmt="fancy_grid"))


@log_call
def get_categories():
    categories = load_data("categories.json")
    if not categories:
        print("📭 No hay categorias registradas.")
        return
    return categories

@log_call
def delete_category(nombre):
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
    

    


