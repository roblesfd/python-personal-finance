import json 
from typing import List, Dict
from tabulate import tabulate

from .base_category_repo import CategoryRepository 
from db.storage import load_data, save_data
from utils.logger import log_call, log_error, log_time


class JsonCategoryRepository(CategoryRepository):

    FILE = "categories.json"

    @log_call
    @log_error
    @log_time
    def get_all(self) -> List[Dict]:
        return load_data(self.FILE) or []

    @log_call
    @log_error
    @log_time
    def save(self, categories: List[Dict]) -> List[Dict]:
        """Guarda/Actualiza lista de categorias

        Args:
            categories List[Dict]: Nombre de categoria

        Returns:
            List[Dict]: Lista de dict actualizada de categorias
        """
        save_data(categories, self.FILE)
        return categories

    @log_call
    @log_error
    @log_time
    def delete(self, nombre: str) -> List[Dict]:
        """Elimina una categoria

        Args:
            nombre (str): Nombre de la categoría

        Returns:
            List[Dict]: Lista actualizada de categorias
        """
        categories = self.get_all()
        updated = [c for c in categories if c["nombre"] != nombre]
        self.save(updated)
        return updated 

    @log_call
    @log_error
    @log_time
    def display(self, categories: List[Dict]) -> None:
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



