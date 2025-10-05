import sqlite3
from typing import List, Dict
from tabulate import tabulate
from utils.logger import log_call, log_error, log_time
from .base_category_repo import BaseCategoryRepository


class SqliteCategoryRepository(BaseCategoryRepository):
    DB_FILE = "./db/data.db"

    def __init__(self):
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.DB_FILE) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS categories (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT UNIQUE NOT NULL
                )
            """)

    @log_call
    @log_error
    @log_time
    def get_all(self) -> List[Dict]:
        with sqlite3.connect(self.DB_FILE) as conn:
            cursor = conn.execute("SELECT id, nombre FROM categories")
            rows = cursor.fetchall()
            return [{"id": r[0], "nombre": r[1]} for r in rows]

    @log_call
    @log_error
    @log_time
    def save(self, categories: List[Dict]) -> List[Dict]:
        with sqlite3.connect(self.DB_FILE) as conn:
            for cat in categories:
                conn.execute(
                    "INSERT OR IGNORE INTO categories (nombre) VALUES (?)",
                    (cat["nombre"],)
                )
            conn.commit()
        return self.get_all()

    @log_call
    @log_error
    @log_time
    def delete(self, nombre: str) -> List[Dict]:
        with sqlite3.connect(self.DB_FILE) as conn:
            conn.execute("DELETE FROM categories WHERE nombre = ?", (nombre,))
            conn.commit()
        return self.get_all()

    @log_call
    @log_error
    @log_time
    def display(self, categories: List[Dict]) -> None:
        table = [[c["id"], c["nombre"]] for c in categories]
        print(tabulate(table, headers=["ID", "Nombre"], tablefmt="fancy_grid"))
