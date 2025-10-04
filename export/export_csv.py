import csv

DIR_PATH = "static/"

def export_to_csv(transactions: list[dict], file: str) -> None:
    """Exporta la list de transacciones a un archivo (file) .csv 

    Args:
        transactions (list[dict]): Lista de transacciones a exportar
        file (str): Nombre del archivo .csv
    """

    file_path = DIR_PATH + file

    if not transactions:
        return
    
    with open(file_path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=transactions[0].keys())
        writer.writeheader()
        writer.writerows(transactions)