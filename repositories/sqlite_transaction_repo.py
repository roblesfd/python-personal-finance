import sqlite3 
from typing import List, Dict 
from utils.logger import log_call, log_error, log_time 
from repositories.base_transaction_repo import BaseTransactionRepository

class SQLiteTransactionRepository(BaseTransactionRepository):
    DB_FILE = "./db/data.db"

    def __init__(self):
        self._init_db()


    def _init_db(self):
        """ Crea la tabla si no existe """
        with sqlite3.connect(self.DB_FILE) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS transactions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    fecha TEXT NOT NULL,
                    tipo TEXT NOT NULL,
                    monto REAL NOT NULL,
                    categoria TEXT NOT NULL,
                    descripcion TEXT
                );
            """)
            conn.commit()


    @log_call
    @log_error
    @log_time
    def get_all(self) -> List[Dict]:
        with sqlite3.connect(self.DB_FILE) as conn:
            cursor = conn.execute("SELECT id, fecha, tipo, monto, categoria, descripcion FROM transactions")
            rows = cursor.fetchall()
            return [
                {"id": row[0], "fecha": row[1], "tipo":row[2], "monto": row[3], "categoria": row[4], "descripcion": row[5]}
                for row in rows
            ]


    @log_call
    @log_error
    @log_time
    def save(self, transactions: List[Dict]):
        """Guarda una lista de transacciones en SQLite."""
        with sqlite3.connect(self.DB_FILE) as conn:
            conn.executemany(
                "INSERT INTO transactions (fecha, tipo, monto, categoria, descripcion) VALUES (?, ?, ?, ?, ?)",
                [(t["fecha"], t["tipo"], t["monto"], t["categoria"], t["descripcion"]) for t in transactions]
            )
            conn.commit()
        print("✅ Movimiento guardado en SQLite.")

    @log_call
    @log_error
    @log_time
    def delete(self, id: int) -> List[Dict]:
        with sqlite3.connect(self.DB_FILE) as conn:
            conn.execute("DELETE FROM transactions WHERE id = ?", (id,))
            conn.commit()
        print(f"🗑️  Eliminada transacción con ID '{id}'")
        return self.get_all()


    @log_call
    @log_error
    @log_time
    def display(self, transactions: List[Dict]) -> None:
        from tabulate import tabulate
        table = [
            [t["id"], t["fecha"], t["tipo"], t["monto"], t["categoria"], t["descripcion"]]
            for t in transactions
        ]
        print(tabulate(table, headers=["No.", "Fecha", "Tipo", "Monto", "Categoría", "Descripción"], tablefmt="fancy_grid"))